#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta os clipes de uma aula a partir das capturas REAIS do Tinkercad.

O enquadramento não é escolhido no olho: cada clipe recorta a janela que
CONTÉM o gesto inteiro (de onde a seta sai até onde ela chega), com margem.
Assim nenhum clipe pode cortar justamente o botão que o passo manda apertar —
que é o defeito que o olho não pega quando o recorte vem de números a dedo.

    python3 fonte/faz_gifs.py N        # N = numero da aula (padrao 1)
"""
import json, os, sys
import numpy as np
from PIL import Image, ImageSequence

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
os.environ["GIF_AULA"] = sys.argv[1] if len(sys.argv) > 1 else "1"
import gif as G

N      = sys.argv[1] if len(sys.argv) > 1 else "1"
PASTA  = os.path.join(AQUI, f"aula{N}")
TELA   = (1440, 900)
MARGEM = 190          # folga em volta do que o clipe tem de mostrar
MIN_L  = 920          # largura mínima da janela, para o recorte não ficar apertado
PROP   = 10 / 16      # altura / largura
SOBRA  = 70           # o quanto a janela pode passar da borda da captura


def caixa_mudanca(antes, depois, bloco=8, minimo=12, lim=30):
    """Onde a tela MUDOU entre os dois quadros, em blocos de 8 px.

    ⛔ Em blocos, e não pixel a pixel, para um respingo solto de compressão
    não esticar a caixa até o outro canto da tela.
    """
    A = np.asarray(Image.open(os.path.join(PASTA, antes)).convert("L"), dtype=int)
    B = np.asarray(Image.open(os.path.join(PASTA, depois)).convert("L"), dtype=int)
    if A.shape != B.shape:
        return None
    dif = np.abs(A - B) > lim
    h, w = (s // bloco for s in dif.shape)
    g = dif[:h*bloco, :w*bloco].reshape(h, bloco, w, bloco).sum(axis=(1, 3))
    ys, xs = np.nonzero(g >= minimo)
    if not len(xs):
        return None
    return (int(xs.min())*bloco, int(ys.min())*bloco,
            int(xs.max()+1)*bloco, int(ys.max()+1)*bloco)


def janela(pontos):
    """A menor janela 16:10 que contém todos os pontos com margem, na tela."""
    xs = [p[0] for p in pontos]; ys = [p[1] for p in pontos]
    x0, x1 = min(xs) - MARGEM, max(xs) + MARGEM
    y0, y1 = min(ys) - MARGEM, max(ys) + MARGEM
    larg = max(MIN_L, x1 - x0, (y1 - y0) / PROP)
    alt  = larg * PROP
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    # ⛔ A janela NÃO é presa dentro da captura. Presa, o alvo colado na quina
    #    da tela (o nome do projeto, a casinha) ficava a ~21 px da borda e o
    #    anel de clique saía cortado. O que passar da tela vira margem cinza.
    larg = min(larg, TELA[0] + 2*SOBRA); alt = min(alt, TELA[1] + 2*SOBRA)
    x0, y0 = cx - larg/2, cy - alt/2
    x0 = min(max(-SOBRA, x0), TELA[0] + SOBRA - larg)
    y0 = min(max(-SOBRA, y0), TELA[1] + SOBRA - alt)
    cx0, cy0 = round(x0), round(y0)
    return (cx0, cy0, cx0 + round(larg), cy0 + round(alt))


def dentro(box, p):
    return box[0] <= p[0] <= box[2] and box[1] <= p[1] <= box[3]


def recorte_proprio():
    """Os quadros do passo 2/3 já vêm recortados (só o canto do botão Criar).

    ⛔ Para eles o recorte é a imagem inteira: aplicar a janela de 1440×900
    deslocaria o alvo para fora do quadro. E o item «Projeto 3D» não vira
    clipe — vira CÍRCULO numa foto parada, porque clicar nele criaria um
    projeto novo na conta do dono a cada execução.
    """
    import anota
    cam = os.path.join(PASTA, "alvos0.json")
    if not os.path.exists(cam):
        return []
    feitos = []
    for chave, d in sorted(json.load(open(cam)).items()):
        if d.get("tipo") == "marca":
            im = Image.open(os.path.join(PASTA, d["em"])).convert("RGB")
            anota.moldura(im, *d["caixa"])
            saida = os.path.join(PASTA, "d03_marcado.jpg")
            im.save(saida, "JPEG", quality=92)
            print(f"  {chave:<14} marca    moldura em {d['caixa']} -> d03_marcado.jpg")
            feitos.append(chave)
            continue
        cam_g, n, tam = G.gesto(f"{chave}.gif", d["antes"], d["depois"],
                                tuple(d["alvo"]), box=None, larg=900)
        print(f"  {chave:<14} clique   {n:>3} quadros  {tam/1024:>6.0f} KB  "
              f"(quadro já recortado)")
        feitos.append(chave)
    return feitos


def principal():
    alvos = json.load(open(os.path.join(PASTA, "alvos.json")))
    feitos, erros = [], []
    for chave, d in sorted(alvos.items()):
        alvo = tuple(d["alvo"])
        ate  = tuple(d["ate"]) if d.get("ate") else None

        # ⛔ O recorte NÃO sai só do ponto do clique. Saía, e por isso os clipes
        #    de encolher a caixinha e de virar Orifício mostravam o painel
        #    inteiro com a PLAQUINHA cortada ao meio pela borda esquerda — e a
        #    peça é justamente o que a criança precisa ver mudar. A janela tem
        #    de conter o gesto E a região onde a tela mudou.
        mud = caixa_mudanca(d["antes"], d["depois"])
        if mud is None:
            erros.append(f"{chave}: não achei região mudada entre os quadros")
            mud = (alvo[0], alvo[1], alvo[0], alvo[1])
        pontos = [alvo] + ([ate] if ate else []) + [(mud[0], mud[1]), (mud[2], mud[3])]
        box = janela(pontos)

        # o invariante do enquadramento, conferido e não confiado
        for nome, p in (("a seta", alvo), ("o fim do arrasto", ate),
                        ("o canto da região que mudou", (mud[0], mud[1])),
                        ("o outro canto da região que mudou", (mud[2], mud[3]))):
            if p and not dentro(box, p):
                erros.append(f"{chave}: {nome} {p} ficou FORA do recorte {box}")

        # ⛔ Clamp no desenho resolve o anel CORTADO, mas pode devolver um anel
        #    minúsculo — que é o mesmo defeito disfarçado de certo. O alvo tem
        #    de ter folga de verdade dentro do quadro de saída.
        esc = 900 / (box[2] - box[0])
        ax, ay = (alvo[0]-box[0])*esc, (alvo[1]-box[1])*esc
        alt_saida = (box[3]-box[1]) * esc
        folga = min(ax, ay, 900-ax, alt_saida-ay)
        if folga < 26:
            erros.append(f"{chave}: a seta fica a {folga:.0f} px da borda do "
                         f"recorte — o anel de clique não cabe inteiro")

        tipo = d.get("tipo", "arrasto" if ate else "clique")
        if tipo == "tecla":
            cam, n, tam = G.tecla(f"{chave}.gif", d["antes"], d["depois"],
                                  d["teclas"], box=box, larg=900, onde=alvo)
        elif tipo == "arrasto":
            cam, n, tam = G.arraste(f"{chave}.gif", d["antes"], d["depois"],
                                    alvo, ate, box=box, larg=900,
                                    botao=d.get("botao", "esq"))
        else:
            cam, n, tam = G.gesto(f"{chave}.gif", d["antes"], d["depois"],
                                  alvo, box=box, larg=900,
                                  botao=d.get("botao", "esq"))

        # o clipe tem de MOSTRAR a mudança: primeiro e último quadro diferentes
        with Image.open(cam) as im:
            qs = [f.convert("RGB") for f in ImageSequence.Iterator(im)]
        dif = sum(1 for a, b in zip(qs[0].getdata(), qs[-1].getdata()) if a != b)
        if dif < 2000:
            erros.append(f"{chave}: o clipe começa e termina igual ({dif} px) "
                         "— animação que não anima")
        feitos.append((chave, n, tam, box, dif))
        print(f"  {chave:<14} {tipo:<8} {n:>3} quadros  {tam/1024:>6.0f} KB  "
              f"recorte {box}  mudou {dif} px", flush=True)

    feitos += [(c, 0, 0, None, 0) for c in recorte_proprio()]
    print(f"\n{len(feitos)} clipe(s) em {os.path.join(PASTA,'gifs')}")
    for e in erros:
        print("  !!", e)
    return 1 if erros else 0


if __name__ == "__main__":
    raise SystemExit(principal())
