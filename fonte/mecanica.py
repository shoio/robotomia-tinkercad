# -*- coding: utf-8 -*-
"""Mecânicas do editor do Tinkercad que valem para MAIS DE UMA aula.

Medidas na tela, nunca combinadas de cabeça (ver PADRAO.md §2): as alças de uma
forma, os números de tamanho, as bolinhas do «Alinhar» e as setas de girar são
desenhadas no CANVAS — não existem no DOM — e por isso se acham pela imagem.
Só os números de tamanho viram DOM (um `<input>`) quando alguém clica neles.
"""
import numpy as np
from PIL import Image
from scipy import ndimage

from bancada import Falhou

CINZA_ALCA = 220           # o miolo da alça quadrada (o contorno é 51)
LIMITE_PAINEL = 880        # à direita disto fica o painel de propriedades
TOPO_UTIL = 100            # acima disto é a barra de ferramentas
PAINEL_ATE_Y = 548         # o painel de propriedades (o do Tórulo é o mais alto) acaba aqui


def _caixas(mascara, wmin, wmax, hmin, hmax, preench=0.7):
    lab, n = ndimage.label(mascara)
    achados = []
    for i in range(1, n + 1):
        ys, xs = np.nonzero(lab == i)
        w, h = xs.max() - xs.min() + 1, ys.max() - ys.min() + 1
        if wmin <= w <= wmax and hmin <= h <= hmax and len(xs) >= preench * w * h:
            achados.append((int(xs.mean()), int(ys.mean())))
    return achados


def acha_alcas(captura):
    """As alças QUADRADAS (redimensionar) da forma selecionada: [(x, y)].

    O miolo delas é cinza 220, ~8 px. A alça que o mouse está segurando fica
    VERMELHA e some desta lista — por isso se acha de novo a cada clique."""
    im = np.asarray(Image.open(captura).convert("RGB"), dtype=int)
    m = (np.abs(im - CINZA_ALCA) <= 3).all(axis=2)
    # o painel de propriedades só ocupa a faixa de CIMA da direita (até y ~545,
    # no do Tórulo); mais embaixo há plano de trabalho, e uma peça solta ali
    # tem alça à direita de x = 880 (medido com o anel solto em x = 902)
    m[:PAINEL_ATE_Y, LIMITE_PAINEL:] = False
    m[:TOPO_UTIL] = False
    achadas = _caixas(m, 6, 11, 6, 11, 0.75)
    # a alça que acabou de ser usada FICA VERMELHA até o próximo clique: sem
    # contá-la, depois de mexer na altura a lista vinha com 4 alças e a de
    # cima sumia (medido: a forma tinha 50 mm e a alça de altura estava lá)
    v = (im[:, :, 0] > 190) & (im[:, :, 1] < 90) & (im[:, :, 2] < 90)
    v[:PAINEL_ATE_Y, LIMITE_PAINEL:] = False
    v[:TOPO_UTIL] = False
    return achadas + _caixas(v, 6, 12, 6, 12, 0.6)


def classifica_alcas(alcas):
    """{'topo', 'esq_tras', 'dir_tras', 'esq_frente', 'dir_frente'} -> (x, y).

    Na vista inicial a base da forma é um paralelogramo: duas alças atrás (mais
    acima na tela) e duas na frente; a de ALTURA fica no meio, por cima de tudo."""
    if len(alcas) < 5:
        raise Falhou(f"esperava 5 alças e achei {len(alcas)}: {alcas}")
    # ⛔ A de ALTURA é a do MEIO em x — e não a de menor y. Num cilindro baixo e
    #    largo a alça do centro da tampa fica ABAIXO das duas de trás, e a
    #    regra «a mais alta na tela» escolhia o canto: o clique ia no canto e o
    #    passo «altura» pedia um número que não existia.
    por_x = sorted(alcas, key=lambda p: p[0])
    topo = por_x[len(por_x) // 2]
    resto = [p for p in alcas if p != topo]
    por_y = sorted(resto, key=lambda p: p[1])
    tras = sorted(por_y[:2], key=lambda p: p[0])
    frente = sorted(por_y[2:], key=lambda p: p[0])
    return {"topo": topo, "esq_tras": tras[0], "dir_tras": tras[1],
            "esq_frente": frente[0], "dir_frente": frente[1]}


def rotulos_de_medida(pg):
    """Os números de tamanho visíveis no canvas: [(texto, x, y)] (centros)."""
    # ⛔ O transferidor de girar (`0°`) usa a MESMA classe dos números de tamanho e
    #    fica no DOM, invisível, em (0, 0): só vale o que é número puro.
    return pg.evaluate("""() => [...document.querySelectorAll('.dimension-label-view.visible')]
        .map(e => { const r = e.getBoundingClientRect();
                    return [(e.textContent||'').trim(), r.x + r.width/2, r.y + r.height/2]; })
        .filter(t => /^-?\\d+(\\.\\d+)?$/.test(t[0]))""")


def _campo_em(pg, x, y, tol=45):
    n = pg.locator("input").count()
    for i in range(n):
        bb = pg.locator("input").nth(i).bounding_box()
        if bb and \
           abs(bb["x"] + bb["width"] / 2 - x) < tol and abs(bb["y"] + bb["height"] / 2 - y) < tol:
            return pg.locator("input").nth(i)
    return None


def digita_no_rotulo(b, x, y, valor):
    """Clica no número de tamanho em (x, y), escreve `valor` e confirma.

    ⛔ `fill()`, e não `keyboard.type()`: digitado, o número virava outro (uma
    peça de 20 saiu com a altura de um poste). O mesmo vale para os campos do
    painel (PADRAO.md §3)."""
    b.pg.mouse.click(x, y)
    b.pg.wait_for_timeout(700)
    campo = _campo_em(b.pg, x, y)
    if campo is None:
        raise Falhou(f"cliquei no número de tamanho em {(int(x), int(y))} e nenhum campo abriu")
    campo.fill(str(valor))
    campo.press("Enter")
    b.pg.wait_for_timeout(1200)
    return (x, y)


def seleciona_forma(b, ponto):
    b.pg.mouse.click(*ponto)
    b.pg.wait_for_timeout(900)


def alcas_agora(b, nome="_alcas"):
    cam = b.cap(nome)          # ponteiro no canto: parado numa alça ela fica VERMELHA e some da lista
    return classifica_alcas(acha_alcas(cam))


# ───────────────────────────── a ferramenta Alinhar ─────────────────────────────

def acha_bolinhas_alinhar(captura):
    """As bolinhas do «Alinhar», em três grupos de até três.

    Na vista inicial: embaixo, a fileira que alinha em X (esquerda, centro,
    direita); na coluna da esquerda, as de Y (frente, meio, atrás); na da
    direita, as de Z (base, meio, topo).

    ⛔ São de um cinza EXATO (51,51,51), que nada mais na tela tem — o contorno
    da peça e os fios saíam de «qualquer coisa escura» e prendiam bolinhas
    umas nas outras (a do meio da esquerda sumia, colada no contorno). E, com a
    peça larga, a bolinha da direita de X e a de BASE de Z caem uma em cima da
    outra: o objeto largo (≥ 19 px) vale por DUAS."""
    im = np.asarray(Image.open(captura).convert("RGB"), dtype=int)
    # (51 exato é o miolo; as bordas e o pedaço riscado pela caixa pontilhada
    #  saem 26 — por isso «escuro e sem cor», e não só 51)
    m = (im < 62).all(axis=2) & ((im.max(axis=2) - im.min(axis=2)) < 14)
    m[:TOPO_UTIL + 40] = False
    m[:280, 890:] = False                 # o painel de propriedades (só o alto)
    m[860:] = False
    # ⛔ a linha pontilhada da caixa pode CORTAR uma bolinha em duas fatias de 4 px
    #    (a de trás à esquerda sumia por isso); fecha-se na vertical antes de abrir
    m = ndimage.binary_closing(m, structure=np.ones((7, 3), bool))
    m = ndimage.binary_opening(m, structure=np.ones((5, 5), bool))
    lab, n = ndimage.label(m)
    pts = []
    for i in range(1, n + 1):
        ys, xs = np.nonzero(lab == i)
        w, h = xs.max() - xs.min() + 1, ys.max() - ys.min() + 1
        if not (9 <= w <= 36 and 7 <= h <= 20):
            continue
        cx, cy = int(xs.mean()), int(ys.mean())
        if w >= 27:               # duas coladas (as de uma bolinha medem 13 a 22)
            pts += [(cx - 6, cy), (cx + 6, cy)]
        else:
            pts.append((cx, cy))
    if len(pts) < 7:
        raise Falhou(f"esperava as bolinhas de alinhar e achei só {len(pts)}: {pts}")
    # ⛔ a bolinha que ACABOU de ser clicada fica CINZA e some desta lista; a
    #    classificação tolera falta e devolve None no lugar.
    ymax = max(p[1] for p in pts)
    baixo = sorted([p for p in pts if abs(p[1] - ymax) <= 8], key=lambda p: p[0])
    resto = [p for p in pts if p not in baixo]
    # a coluna da esquerda: tudo o que está a ≤ 60 px do ponto mais à esquerda
    # (as três ficam alinhadas em x). Pegar «as três mais à esquerda» levava a
    # bolinha de Z para dentro do grupo quando uma de Y já tinha sido clicada.
    x0 = min(p[0] for p in resto) if resto else 0
    esq = sorted([p for p in resto if p[0] <= x0 + 60], key=lambda p: -p[1])
    dir_ = sorted([p for p in resto if p not in esq], key=lambda p: -p[1])

    def tres(lista, nomes):
        if len(lista) == 3:
            return dict(zip(nomes, lista))
        if len(lista) == 2:                      # sumiu a do meio (a recém-clicada)
            return {nomes[0]: lista[0], nomes[1]: None, nomes[2]: lista[1]}
        return {n: None for n in nomes}

    # o grupo de baixo tem 3 (X); se a de BASE de Z veio junto, ela é a última
    # do grupo e a coluna da direita fica com 2 (meio e topo)
    return {"x": tres(baixo[:3], ("esq", "centro", "dir")),
            "y": tres(esq, ("frente", "centro", "atras")),
            "z": tres(dir_ if len(dir_) == 3 else [None] + dir_ if len(dir_) == 2 else dir_,
                      ("base", "centro", "topo")) if dir_ else {n: None for n in ("base", "centro", "topo")}}


def alinha(b, eixo, qual, captura="_alinha"):
    """Clica numa bolinha do Alinhar. Devolve o ponto clicado.

    ⛔ Depois de CADA clique a caixa das formas muda e as bolinhas andam: a
    próxima tem de ser achada de novo, na captura de agora. Clicar no lugar da
    anterior errava o alvo e ainda DESSELECIONAVA as formas."""
    cam = b.cap(captura)
    g = acha_bolinhas_alinhar(cam)
    ponto = g[eixo][qual]
    if ponto is None:
        raise Falhou(f"a bolinha {eixo}/{qual} do Alinhar não está visível ({g})")
    b.pg.mouse.move(*ponto); b.pg.wait_for_timeout(300)
    b.pg.mouse.click(*ponto); b.pg.wait_for_timeout(1300)
    return ponto


# ───────────────────────────────── girar ─────────────────────────────────────

def acha_setas_de_girar(captura, alcas, quer=("cima", "baixo")):
    """As duas setas curvas de girar: {'cima': (x, y), 'baixo': (x, y)}.

    Não ficam a uma distância fixa das alças (a de cima já foi 8 e já foi 23 px
    acima do cone de «subir», conforme a peça) — por isso se acham pela FORMA:
    um traço cinza de ~30 × 14 px, acima de tudo (cima) ou abaixo de tudo
    (baixo), perto do meio da peça."""
    im = np.asarray(Image.open(captura).convert("RGB"), dtype=int)
    m = (im < 150).all(axis=2) & ((im.max(axis=2) - im.min(axis=2)) < 30)
    m[:PAINEL_ATE_Y, LIMITE_PAINEL:] = False
    m[:TOPO_UTIL] = False
    m = ndimage.binary_dilation(m, iterations=2)
    lab, n = ndimage.label(m)
    topo, frente = alcas["topo"], alcas["esq_frente"]
    mais_alta = min(p[1] for p in alcas.values())      # a seta de cima fica ACIMA de todas as alças
    cima = baixo = None
    for i in range(1, n + 1):
        ys, xs = np.nonzero(lab == i)
        w, h = xs.max() - xs.min() + 1, ys.max() - ys.min() + 1
        if not (20 <= w <= 45 and 10 <= h <= 24):
            continue
        cx, cy = float(xs.mean()), float(ys.mean())
        if abs(cx - topo[0]) > 60:
            continue
        if cy < mais_alta - 12 and (cima is None or cy > cima[1]):
            cima = (cx, cy)                     # a mais PERTO da peça, por cima
        if cy > frente[1] + 8 and (baixo is None or cy < baixo[1]):
            baixo = (cx, cy)
    achadas = {"cima": cima, "baixo": baixo}
    faltam = [q for q in quer if achadas[q] is None]
    if faltam:
        raise Falhou(f"não achei a seta de girar {faltam} (cima {cima}, baixo {baixo})")
    return achadas


def graus_agora(pg):
    """O número do transferidor enquanto se gira («-90°»), ou None."""
    r = pg.evaluate("""() => [...document.querySelectorAll('*')].filter(e => !e.children.length
        && /^-?\\d+(\\.\\d+)?°$/.test((e.textContent||'').trim())).map(e => (e.textContent||'').trim())""")
    return r[0] if r else None


def gira(b, seta, graus, passo=(4, 3), maximo=60):
    """Segura a seta de girar e a leva até o transferidor mostrar `graus`.

    ⛔ O ângulo NÃO se pede por número: a seta gira conforme o ponteiro anda, e
    o transferidor mostra o ângulo ao vivo. Então o robô anda de pouquinho em
    pouquinho e PARA quando o número que a criança vai ver é o do passo — foi
    assim que o −90° saiu exato, em vez de −87° ou −112°."""
    pg = b.pg
    pg.mouse.move(*seta); pg.wait_for_timeout(400)
    pg.mouse.down(); pg.wait_for_timeout(450)
    alvo = {f"{graus}°", f"-{graus}°"}
    visto = None
    for i in range(1, maximo + 1):
        pg.mouse.move(seta[0] + i * passo[0], seta[1] + i * passo[1])
        pg.wait_for_timeout(70)
        visto = graus_agora(pg)
        if visto in alvo:
            break
    else:
        pg.mouse.up()
        raise Falhou(f"girei {maximo} passos e o transferidor nunca mostrou {graus}° (último: {visto})")
    pg.wait_for_timeout(300)
    meio = b.cap("_girando", parar=False)
    pg.mouse.up(); pg.wait_for_timeout(1200)
    return visto, meio


def gira_em_arco(b, seta, graus, sentido=1, rx=110, ry=70, passo_graus=3, maximo=60):
    """Gira pela seta de BAIXO (em torno do eixo vertical).

    ⛔ Essa seta mede o ÂNGULO do ponteiro em volta do centro da peça no plano,
    então um arrasto em linha reta nunca chega a 90° (só se aproxima): o
    transferidor travou em 43°. O ponteiro tem de andar num ARCO, em volta do
    centro — e, como o plano está de lado para a câmera, o arco é uma
    ELIPSE (mais larga que alta)."""
    import math
    pg = b.pg
    cx, cy = seta[0], seta[1] - ry
    pg.mouse.move(*seta); pg.wait_for_timeout(400)
    pg.mouse.down(); pg.wait_for_timeout(450)
    alvo = {f"{graus}°", f"-{graus}°"}
    visto = None
    for i in range(1, maximo + 1):
        t = math.radians(i * passo_graus) * sentido
        pg.mouse.move(cx + rx * math.sin(t), cy + ry * math.cos(t))
        pg.wait_for_timeout(70)
        visto = graus_agora(pg)
        if visto in alvo:
            break
    else:
        pg.mouse.up()
        raise Falhou(f"girei em arco {maximo} passos e o transferidor nunca mostrou {graus}° (último: {visto})")
    pg.wait_for_timeout(300)
    meio = b.cap("_girando", parar=False)
    pg.mouse.up(); pg.wait_for_timeout(1200)
    return visto, meio


# ───────────────────────────── medidas pelas alças ───────────────────────────

def muda_planta(b, largura=None, comprimento=None, nome="_alcasP"):
    """Clica na alça do canto de cima à esquerda e escreve a largura (o número
    de CIMA) e/ou o comprimento (o da ESQUERDA). Devolve o ponto da alça."""
    h = alcas_agora(b, nome)
    alvo = h["esq_tras"]
    b.pg.mouse.click(*alvo); b.pg.wait_for_timeout(900)
    rot = rotulos_de_medida(b.pg)
    if len(rot) != 2:
        raise Falhou(f"esperava 2 números de tamanho e vi {rot}")
    if comprimento is not None:
        comp = min(rot, key=lambda t: t[1])
        digita_no_rotulo(b, comp[1], comp[2], comprimento)
        rot = rotulos_de_medida(b.pg)
    if largura is not None:
        larg = min(rot, key=lambda t: t[2])
        digita_no_rotulo(b, larg[1], larg[2], largura)
    return alvo


def muda_altura(b, valor, nome="_alcasA"):
    """Clica na alça do MEIO da tampa e escreve a altura. Devolve o ponto da alça."""
    h = alcas_agora(b, nome)
    alvo = h["topo"]
    b.pg.mouse.click(*alvo); b.pg.wait_for_timeout(900)
    rot = rotulos_de_medida(b.pg)
    if len(rot) != 1:
        raise Falhou(f"esperava 1 número de altura e vi {rot}")
    digita_no_rotulo(b, rot[0][1], rot[0][2], valor)
    return alvo
