#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta GIFs a partir das capturas REAIS do Studio.
   O cursor é desenhado por cima; as telas são fotografias do aplicativo."""
import os, math
from PIL import Image, ImageDraw

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aula1")
OUT = os.path.join(D, "gifs")
os.makedirs(OUT, exist_ok=True)


def cursor(im, x, y, escala=1.0):
    """Desenha uma seta de mouse em (x,y)."""
    d = ImageDraw.Draw(im, "RGBA")
    s = 34 * escala
    p = [(x, y), (x, y + s), (x + .26*s, y + .74*s), (x + .46*s, y + 1.12*s),
         (x + .62*s, y + 1.03*s), (x + .43*s, y + .66*s), (x + .72*s, y + .64*s)]
    d.polygon(p, fill=(255, 255, 255, 255), outline=(20, 20, 24, 255))
    d.line(p + [p[0]], fill=(20, 20, 24, 255), width=max(1, int(2*escala)), joint="curve")
    return im


def mouse(im, x, y, botao="esq", escala=1.0, apertado=True):
    """Desenha um mouse pequeno ao lado do cursor, com o botao APERTADO aceso.

       A aula e para crianca de 10 anos: 'clique' e 'clique com o botao
       direito' sao gestos diferentes, e ninguem adivinha qual e qual por uma
       seta. O desenho mostra qual dos dois botoes afunda."""
    d = ImageDraw.Draw(im, "RGBA")
    L, A = 34 * escala, 52 * escala          # corpo do mouse
    x0, y0 = x - L - 16 * escala, y - A - 10 * escala
    corpo = [x0, y0, x0 + L, y0 + A]
    d.rounded_rectangle(corpo, radius=int(L * 0.45),
                        fill=(250, 250, 252, 240), outline=(28, 30, 38, 255),
                        width=max(2, int(2.4 * escala)))
    meio_y = y0 + A * 0.42
    aceso = (232, 60, 60, 255) if apertado else (210, 214, 220, 255)
    if botao == "esq":
        d.pieslice([x0, y0, x0 + L, y0 + A * 0.84], 180, 270, fill=aceso)
    else:
        d.pieslice([x0, y0, x0 + L, y0 + A * 0.84], 270, 360, fill=aceso)
    d.line([x0 + L / 2, y0 + 2, x0 + L / 2, meio_y], fill=(28, 30, 38, 255),
           width=max(2, int(2 * escala)))
    d.line([x0, meio_y, x0 + L, meio_y], fill=(28, 30, 38, 255),
           width=max(2, int(2 * escala)))
    d.rounded_rectangle(corpo, radius=int(L * 0.45), outline=(28, 30, 38, 255),
                        width=max(2, int(2.4 * escala)))
    return im


def anel(im, x, y, r, alpha=220, larg=7):
    d = ImageDraw.Draw(im, "RGBA")
    d.ellipse([x-r, y-r, x+r, y+r], outline=(232, 60, 60, alpha), width=larg)
    return im


def _prep(caminho, box, larg):
    im = Image.open(caminho).convert("RGB")
    if box:
        im = im.crop(box)
    if larg and im.width != larg:
        im = im.resize((larg, round(im.height * larg / im.width)), Image.LANCZOS)
    return im


def gesto(nome, antes, depois, alvo, box=None, larg=900,
          origem=None, n_mov=9, n_clique=3, n_fim=7, ms=110, botao="esq"):
    """antes/depois = arquivos; alvo = (x,y) em pixels da captura ORIGINAL."""
    a0 = Image.open(os.path.join(D, antes)).convert("RGB")
    esc = larg / (box[2]-box[0] if box else a0.width)
    ox, oy = (box[0], box[1]) if box else (0, 0)
    ax, ay = (alvo[0]-ox)*esc, (alvo[1]-oy)*esc
    A = _prep(os.path.join(D, antes), box, larg)
    B = _prep(os.path.join(D, depois), box, larg)
    if origem is None:
        origem = (max(20, ax - 240), min(A.height - 40, ay + 200))
    q = []
    # cursor andando
    for k in range(n_mov):
        t = k / max(1, n_mov - 1)
        t = t*t*(3-2*t)                      # suaviza
        f = A.copy()
        cursor(f, origem[0] + (ax-origem[0])*t, origem[1] + (ay-origem[1])*t)
        q.append(f)
    # clique: anel + o mouse com o botao aceso
    for k in range(n_clique):
        f = A.copy()
        anel(f, ax, ay, 14 + k*14, alpha=220 - k*60)
        cursor(f, ax, ay)
        mouse(f, ax, ay, botao=botao)
        q.append(f)
    # resultado
    for k in range(n_fim):
        f = B.copy()
        if k < 2:
            anel(f, ax, ay, 44 + k*16, alpha=150 - k*60, larg=5)
            mouse(f, ax, ay, botao=botao, apertado=(k == 0))
        cursor(f, ax, ay)
        q.append(f)
    return _grava(nome, q, ms)


def _grava(nome, quadros, ms, cores=200):
    """Paleta unica + disposal=1: o PIL grava so o retangulo que mudou.
       A paleta se calcula sobre quadros ESPALHADOS pelo clipe — amostrar so
       o primeiro e o ultimo deixava a paleta de cores do Studio acinzentada."""
    n = len(quadros)
    amostras = sorted({0, n//5, 2*n//5, 3*n//5, 4*n//5, n-1})
    w, h = quadros[0].size
    tira = Image.new("RGB", (w, h*len(amostras)))
    for k, i in enumerate(amostras):
        tira.paste(quadros[i], (0, h*k))
    base = tira.quantize(colors=cores, method=Image.MEDIANCUT)
    pal = [q.quantize(palette=base, dither=Image.NONE) for q in quadros]
    cam = os.path.join(OUT, nome)
    pal[0].save(cam, save_all=True, append_images=pal[1:], duration=ms,
                loop=0, optimize=True, disposal=1)
    return cam, len(pal), os.path.getsize(cam)


def arraste(nome, antes, depois, de, ate, box=None, larg=900, n=12, ms=110,
            botao="esq"):
    """Arrasto: o cursor pressionado vai de 'de' ate 'ate' sobre a tela ANTES,
       deixando um rastro; a tela DEPOIS entra so no fim (nada de fantasma).

       ⛔ `botao` existe porque girar a camera no Tinkercad e arrasto com o
          botao DIREITO. Desenhado como arrasto comum, a crianca segura o
          esquerdo, arrasta a peca para fora do lugar e perde o trabalho."""
    a0 = Image.open(os.path.join(D, antes)).convert("RGB")
    esc = larg / (box[2]-box[0] if box else a0.width)
    ox, oy = (box[0], box[1]) if box else (0, 0)
    dx, dy = (de[0]-ox)*esc, (de[1]-oy)*esc
    tx, ty = (ate[0]-ox)*esc, (ate[1]-oy)*esc
    A = _prep(os.path.join(D, antes), box, larg)
    B = _prep(os.path.join(D, depois), box, larg)
    q = []
    for _ in range(4):
        f = A.copy(); cursor(f, dx, dy); mouse(f, dx, dy, botao=botao, apertado=False)
        q.append(f)
    for k in range(n):
        t = (k+1)/n
        f = A.copy()
        d = ImageDraw.Draw(f, "RGBA")
        cx, cy = dx + (tx-dx)*t, dy + (ty-dy)*t
        d.line([dx, dy, cx, cy], fill=(232,60,60,210), width=6)
        cursor(f, cx, cy)
        mouse(f, cx, cy, botao=botao, apertado=True)   # o botao segue APERTADO
        q.append(f)
    for k in range(8):
        f = B.copy()
        if k < 2:
            anel(f, tx, ty, 30 + k*16, alpha=170 - k*70, larg=5)
        cursor(f, tx, ty)
        q.append(f)
    return _grava(nome, q, ms)


def sequencia(nome, passos, box=None, larg=900, ms=110, n_mov=8, n_fim=8,
              origem=None, extras=None):
    """passos = [(arquivo, alvo|None), ...]. O cursor caminha ate o alvo do passo,
       clica, e so entao a tela do passo SEGUINTE aparece.
       extras = arquivos extras exibidos no fim (ex.: jogo rodando)."""
    prim = Image.open(os.path.join(D, passos[0][0]))
    esc = larg / (box[2]-box[0] if box else prim.width)
    ox, oy = (box[0], box[1]) if box else (0, 0)
    conv = lambda p: ((p[0]-ox)*esc, (p[1]-oy)*esc)
    telas = [_prep(os.path.join(D, a), box, larg) for a, _ in passos]
    q = []
    cur = conv(origem) if origem else None
    for i, (_, alvo) in enumerate(passos):
        if alvo is None:
            continue
        ax, ay = conv(alvo)
        if cur is None:
            cur = (max(20, ax-260), min(telas[i].height-40, ay+220))
        for k in range(n_mov):
            t = k/max(1, n_mov-1); t = t*t*(3-2*t)
            f = telas[i].copy()
            cursor(f, cur[0]+(ax-cur[0])*t, cur[1]+(ay-cur[1])*t)
            q.append(f)
        for k in range(3):                       # o clique
            f = telas[i].copy()
            anel(f, ax, ay, 14+k*14, alpha=220-k*60)
            cursor(f, ax, ay)
            q.append(f)
        cur = (ax, ay)
    fim = telas[-1]
    for k in range(n_fim):
        f = fim.copy()
        if k < 2 and cur:
            anel(f, cur[0], cur[1], 44+k*16, alpha=150-k*60, larg=5)
        if cur: cursor(f, *cur)
        q.append(f)
    for extra in (extras or []):
        e = _prep(os.path.join(D, extra), box, larg)
        for _ in range(4):
            f = e.copy()
            if cur: cursor(f, *cur)
            q.append(f)
    return _grava(nome, q, ms)


# ─────────────────────────── gesto de TECLADO ───────────────────────────────
#
# ⛔ Clipe de tecla não pode ser desenhado como clique. Os dois gestos de
#    teclado da Aula 1 (Ctrl + ↓ para descer o furo, Ctrl + A para selecionar
#    tudo) saíram na primeira montagem com a seta caminhando até a peça e um
#    anel vermelho de clique em cima dela. A criança que copia a animação
#    clica ali e não acontece nada — e a animação é a única parte da página
#    que ela realmente imita. Aqui a tecla aparece como TECLA, e o anel só
#    MARCA onde o efeito acontece; ninguém clica nele.

def _teclas_img(im, teclas, aceso, escala=1.0):
    from anota import _fonte
    d = ImageDraw.Draw(im, "RGBA")
    f = _fonte(int(34 * escala))
    cxs, alt = [], int(62 * escala)
    larg = []
    for t in teclas:
        bb = d.textbbox((0, 0), t, font=f)
        larg.append(max(int(58 * escala), bb[2] - bb[0] + int(34 * escala)))
    folga = int(14 * escala)
    total = sum(larg) + folga * (len(teclas) - 1) + int(26 * escala) * (len(teclas) - 1)
    x = (im.width - total) / 2
    y = im.height - alt - int(26 * escala)
    for i, t in enumerate(teclas):
        w = larg[i]
        dy = int(5 * escala) if aceso else 0
        sombra = (190, 196, 206, 255) if aceso else (120, 126, 138, 255)
        d.rounded_rectangle([x, y + dy, x + w, y + alt + int(7*escala)],
                            radius=int(12*escala), fill=sombra)
        d.rounded_rectangle([x, y + dy, x + w, y + alt],
                            radius=int(12*escala),
                            fill=(255, 226, 190, 255) if aceso else (252, 252, 254, 255),
                            outline=(28, 30, 38, 255), width=max(2, int(2.6*escala)))
        bb = d.textbbox((0, 0), t, font=f)
        d.text((x + (w - (bb[2]-bb[0]))/2, y + dy + (alt - (bb[3]-bb[1]))/2 - int(6*escala)),
               t, font=f, fill=(20, 20, 24, 255))
        x += w + folga
        if i < len(teclas) - 1:
            d.text((x, y + dy + alt*0.18), "+", font=f, fill=(60, 64, 74, 255))
            x += int(26 * escala)
    return im


def tecla(nome, antes, depois, teclas, box=None, larg=900, onde=None,
          n_antes=4, n_aperto=4, n_fim=8, ms=110):
    """Clipe de atalho de teclado. `onde` só MARCA onde o efeito aparece."""
    a0 = Image.open(os.path.join(D, antes)).convert("RGB")
    esc = larg / (box[2]-box[0] if box else a0.width)
    ox, oy = (box[0], box[1]) if box else (0, 0)
    A = _prep(os.path.join(D, antes), box, larg)
    B = _prep(os.path.join(D, depois), box, larg)
    px = ((onde[0]-ox)*esc, (onde[1]-oy)*esc) if onde else None
    q = []
    for _ in range(n_antes):
        f = A.copy(); _teclas_img(f, teclas, False); q.append(f)
    for _ in range(n_aperto):
        f = A.copy(); _teclas_img(f, teclas, True); q.append(f)
    for k in range(n_fim):
        f = B.copy()
        if px and k < 3:
            anel(f, px[0], px[1], 34 + k*18, alpha=190 - k*55, larg=6)
        _teclas_img(f, teclas, k < 2)
        q.append(f)
    return _grava(nome, q, ms)
