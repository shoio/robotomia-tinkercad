# Folha de revisao: por passo, ANTES|DEPOIS (do clipe) ou a foto do passo, e o texto ao lado no terminal.
import sys, os, re, json, importlib
from PIL import Image, ImageDraw
n = sys.argv[1]
mod = importlib.import_module(f"conteudo_a{n}")
A = mod.AULA
alvos = {}
for arq in ("alvos.json", "alvos0.json"):
    c = f"aula{n}/{arq}"
    if os.path.exists(c): alvos.update(json.load(open(c)))
def limpa(t): return re.sub(r"<[^>]+>", "", t).replace("&nbsp;", " ")
passos = A["passos"]
linhas = []
imgs = []
for p in passos:
    cl = p.get("clipe")
    nome = None
    if isinstance(cl, str): nome = cl[:-4]
    elif isinstance(cl, list): nome = cl[0][1][:-4]
    print(f"\n#{p['n']} {p['titulo']}  [clipe {nome}]")
    print("  CORPO:", limpa(p["corpo"]))
    print("  VERDE:", limpa(p["ck"]))
    d = alvos.get(nome) if nome else None
    a = Image.open(d["antes"] if False else f"aula{n}/{d['antes']}") if d else None
    b = Image.open(f"aula{n}/{d['depois']}") if d else Image.open(p["img"])
    ims = [x.convert("RGB").resize((560, 350)) for x in ([a] if a else []) + [b]]
    cv = Image.new("RGB", (1130, 372), "white"); dr = ImageDraw.Draw(cv)
    dr.text((4, 2), f"#{p['n']} {p['titulo'][:70]}  (antes | depois)", fill="black")
    for i, im in enumerate(ims): cv.paste(im, (i * 570, 20))
    imgs.append(cv)
# 4 passos por folha
for k in range(0, len(imgs), 4):
    fo = Image.new("RGB", (1130, 372 * len(imgs[k:k+4])), "white")
    for j, im in enumerate(imgs[k:k+4]): fo.paste(im, (0, j * 372))
    fo.save(f"/tmp/rev{n}_{k//4}.png")
print("\nfolhas:", (len(imgs) + 3) // 4)
