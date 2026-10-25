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
    m[:, LIMITE_PAINEL:] = False
    m[:TOPO_UTIL] = False
    achadas = _caixas(m, 6, 11, 6, 11, 0.75)
    # a alça que acabou de ser usada FICA VERMELHA até o próximo clique: sem
    # contá-la, depois de mexer na altura a lista vinha com 4 alças e a de
    # cima sumia (medido: a forma tinha 50 mm e a alça de altura estava lá)
    v = (im[:, :, 0] > 190) & (im[:, :, 1] < 90) & (im[:, :, 2] < 90)
    v[:, LIMITE_PAINEL:] = False
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
    return pg.evaluate("""() => [...document.querySelectorAll('.dimension-label-view.visible')]
        .map(e => { const r = e.getBoundingClientRect();
                    return [(e.textContent||'').trim(), r.x + r.width/2, r.y + r.height/2]; })""")


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
    """As 9 bolinhas pretas do «Alinhar», em três grupos de três.

    Na vista inicial: embaixo, a fileira que alinha em X (esquerda, centro,
    direita); na coluna da esquerda, as que alinham em Y (frente, meio, atrás);
    na da direita, as que alinham em Z (base, meio, topo)."""
    im = np.asarray(Image.open(captura).convert("RGB"), dtype=int)
    m = (im < 70).all(axis=2)
    m[:, LIMITE_PAINEL + 160:] = False
    m[:TOPO_UTIL + 40] = False
    m[860:] = False
    # as bolinhas ficam LIGADAS por linhas finas da mesma cor escura; sem abrir
    # a máscara (3x3 -> some o fio de 1-2 px, fica o disco de ~15 px) duas das
    # nove sumiam, coladas numa linha, e o guarda dizia «achei 7»
    m = ndimage.binary_opening(m, structure=np.ones((5, 5), bool))
    pts = _caixas(m, 9, 26, 7, 20, 0.6)
    if len(pts) < 7:
        raise Falhou(f"esperava as bolinhas de alinhar e achei só {len(pts)}: {pts}")
    # ⛔ a bolinha que ACABOU de ser clicada fica CINZA (e não passa no limite
    #    de «escuro»): depois de alinhar em X o centro de X some da lista — e a
    #    próxima que se quer é de OUTRO eixo. Por isso a classificação tolera
    #    falta e devolve None no lugar.
    ymax = max(p[1] for p in pts)
    baixo = sorted([p for p in pts if abs(p[1] - ymax) <= 8], key=lambda p: p[0])
    resto = [p for p in pts if p not in baixo]
    esq = sorted(sorted(resto, key=lambda p: p[0])[:3], key=lambda p: -p[1])
    dir_ = sorted([p for p in resto if p not in esq], key=lambda p: -p[1])

    def tres(lista, nomes):
        if len(lista) == 3:
            return dict(zip(nomes, lista))
        if len(lista) == 2:                      # sumiu a do meio (a recém-clicada)
            return {nomes[0]: lista[0], nomes[1]: None, nomes[2]: lista[1]}
        return {n: None for n in nomes}

    return {"x": tres(baixo, ("esq", "centro", "dir")),
            "y": tres(esq, ("frente", "centro", "atras")),
            "z": tres(dir_, ("base", "centro", "topo"))}


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
