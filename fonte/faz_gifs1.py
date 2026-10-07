#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta os clipes da Aula 1 a partir das capturas REAIS do Tinkercad.

O enquadramento não é escolhido no olho: cada clipe recorta a janela que
CONTÉM o gesto inteiro (de onde a seta sai até onde ela chega), com margem.
Assim nenhum clipe pode cortar justamente o botão que o passo manda apertar —
que é o defeito que o olho não pega quando o recorte vem de números a dedo.

    python3 fonte/faz_gifs1.py
"""
import json, os, sys
from PIL import Image, ImageSequence

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import gif as G

PASTA  = os.path.join(AQUI, "aula1")
TELA   = (1440, 900)
MARGEM = 240          # folga em volta do gesto
MIN_L  = 920          # largura mínima da janela, para o recorte não ficar apertado
PROP   = 10 / 16      # altura / largura


def janela(pontos):
    """A menor janela 16:10 que contém todos os pontos com margem, na tela."""
    xs = [p[0] for p in pontos]; ys = [p[1] for p in pontos]
    x0, x1 = min(xs) - MARGEM, max(xs) + MARGEM
    y0, y1 = min(ys) - MARGEM, max(ys) + MARGEM
    larg = max(MIN_L, x1 - x0, (y1 - y0) / PROP)
    alt  = larg * PROP
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    larg = min(larg, TELA[0]); alt = min(alt, TELA[1])
    x0 = min(max(0, cx - larg/2), TELA[0] - larg)
    y0 = min(max(0, cy - alt/2),  TELA[1] - alt)
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
        box  = janela([alvo] + ([ate] if ate else []))

        # o invariante do enquadramento, conferido e não confiado
        for nome, p in (("a seta", alvo), ("o fim do arrasto", ate)):
            if p and not dentro(box, p):
                erros.append(f"{chave}: {nome} {p} ficou FORA do recorte {box}")

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
