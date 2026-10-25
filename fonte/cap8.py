"""Aula 8 — Dado: cinco furinhos redondos na face de cima, por Orifício, Ctrl + D e repetir.

O que é novo: Ctrl + D (duplica a seleção no mesmo lugar), mover a cópia com
Shift + seta, e DUPLICAR UM PAR (a cópia do par anda o mesmo que se andou).
Reaproveita o que as aulas 2–4 deram: medidas, girar em pé, Alinhar com forma
fixa e Shift + clique.

Uso:  ./pwenv/bin/python fonte/cap8.py
"""
import os, shutil, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou
import cap1
import mecanica as M

PASTA  = os.path.join(AQUI, "aula8")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
PROJ   = cap1.PROJ
BATIZADO = "Dado da ANA"

LADO = 60
SOLTAR_DADO = (600, 600)
AFUNDA = 10                       # Ctrl+↓ ×10: o centro da esfera desce até a superfície
PASSO = (3, 2)                    # Shift ×3 + seta ×2 = 32 mm: de um canto ao outro
MEIO = (1, 6)                     # Shift ×1 + seta ×6 = 16 mm: do centro a um canto


def copia_dos_passos_do_site():
    os.makedirs(PASTA, exist_ok=True)
    for nome in ("d02_antes.jpg", "d02_depois.jpg", "d03_marcado.jpg", "d03_menu.jpg",
                 "alvos0.json", "painel.txt"):
        for de in ("aula2", "aula1"):
            o = os.path.join(AQUI, de, nome)
            if os.path.exists(o):
                shutil.copy2(o, os.path.join(PASTA, nome)); break
    os.makedirs(os.path.join(PASTA, "gifs"), exist_ok=True)
    o = os.path.join(AQUI, "aula2", "gifs", "criar.gif")
    if os.path.exists(o):
        shutil.copy2(o, os.path.join(PASTA, "gifs", "criar.gif"))


def teclas(pg, vezes, tecla):
    for _ in range(vezes):
        pg.keyboard.press(tecla); pg.wait_for_timeout(300)


def prova_dos_furos(b, captura):
    """Vista de cima: TRÊS furos na diagonal da tampa? Mede o brilho no centro e nos
    dois cantos (±16 mm) contra a tampa lisa nos outros dois cantos (controle)."""
    import numpy as np
    im = np.asarray(Image.open(captura).convert("RGB"), dtype=int)
    m = (im[:, :, 0] > 150) & (im[:, :, 1] < 90) & (im[:, :, 2] < 90)
    m[:, 880:] = False; m[:100] = False
    ys, xs = np.nonzero(m)
    if len(xs) < 2000:
        raise Falhou("não achei o dado vermelho na vista de cima")
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    cx, cy, esc = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / LADO

    def variacao(x, y, r=20):
        """Desvio-padrão do canal vermelho: tampa lisa = 0; furo = sombreado (≈ 10)."""
        reg = im[int(y) - r:int(y) + r, int(x) - r:int(x) + r, 0]
        return float(reg.std())
    # (na imagem o y cresce para BAIXO: o furo da frente-esquerda tem dy positivo)
    furos = [variacao(cx + dx * esc, cy + dy * esc) for dx, dy in ((0, 0), (-16, 16), (16, -16))]
    lisa = [variacao(cx + dx * esc, cy + dy * esc) for dx, dy in ((-16, -16), (16, 16))]
    print(f"     sombreado nos 3 furos {[round(v, 1) for v in furos]}; tampa lisa {[round(v, 1) for v in lisa]}", flush=True)
    if max(lisa) > 1.0:
        raise Falhou("controle negativo falhou: a tampa nos outros dois cantos devia ser lisa")
    if min(furos) < 5.0:
        raise Falhou(f"os três furos não aparecem na vista de cima: {[round(v, 1) for v in furos]}")


def prova_do_furo_da_frente(captura):
    """Vista inicial: o furo do UM está no meio da face da frente? A face da frente é o
    vermelho ESCURO (R ≈ 178); mede o sombreado no meio e em dois cantos lisos."""
    import numpy as np
    im = np.asarray(Image.open(captura).convert("RGB"), dtype=int)
    m = (np.abs(im[:, :, 0] - 178) <= 8) & (im[:, :, 1] < 60) & (im[:, :, 2] < 70)
    m[:, 880:] = False; m[:100] = False
    ys, xs = np.nonzero(m)
    if len(xs) < 4000:
        raise Falhou("não achei a face da frente do dado")
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    esc = (x1 - x0) / LADO

    def variacao(x, y, r=14):
        return float(im[int(y) - r:int(y) + r, int(x) - r:int(x) + r, 0].std())
    meio = variacao(cx, cy)
    cantos = [variacao(cx + dx * esc, cy + dy * esc) for dx, dy in ((-20, -20), (20, 20), (-20, 20), (20, -20))]
    print(f"     de frente: sombreado no meio {meio:.1f}; cantos lisos {[round(v, 1) for v in cantos]}", flush=True)
    if max(cantos) > 1.0:
        raise Falhou("controle negativo falhou: os cantos da face da frente deviam ser lisos")
    if meio < 4.0:
        raise Falhou(f"o furo do um não aparece no meio da face da frente ({meio:.1f})")


def principal():
    copia_dos_passos_do_site()
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            PERFIL, headless=True, viewport={"width": 1440, "height": 900}, locale="pt-BR")
        pg = ctx.pages[0] if ctx.pages else ctx.new_page()
        b = Bancada(pg, PASTA)
        feitos = []

        def passo(n, desc, fn):
            t0 = time.time()
            try:
                fn()
            except Falhou as e:
                print(f"\n⛔ passo {n} ({desc}) PAROU: {e}", flush=True)
                b.grava_alvos()
                print(f"   passos prontos até aqui: {feitos}", flush=True)
                ctx.close()
                sys.exit(1)
            feitos.append(n)
            print(f"  ✓ {n:2}. {desc}  ({time.time()-t0:.1f}s)", flush=True)

        def par(nome):
            return f"{nome}_antes.jpg", f"{nome}_depois.jpg"

        def fecha(nome):
            b.jpg(f"{nome}_antes"); b.jpg(f"{nome}_depois")

        def alinha_passo(n, eixo, qual, gesto, rotulo):
            a = b.cap(f"g{n:02}_antes")
            ponto = M.alinha(b, eixo, qual, captura=f"_alinha{n}")
            d = b.cap(f"g{n:02}_depois", parar=False)
            b.mudou(a, d, 0.03, oque=f"alinhar {eixo}")
            b.reg(gesto, *par(f"g{n:02}"), ponto, rotulo)
            fecha(f"g{n:02}")

        print(f"abrindo {PROJ}", flush=True)
        pg.goto(PROJ, wait_until="domcontentloaded", timeout=60000)
        cap1.espera_editor(pg)
        cap1.limpa(b)
        with open(os.path.join(PASTA, "projeto.txt"), "w") as f:
            f.write(f"{PROJ}\n{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("plano limpo, vista inicial. começando os passos:\n", flush=True)

        pt = {}

        def p1():
            b.cap("p01_vazio"); b.jpg("p01_vazio")
        passo(1, "o projeto novo, vazio", p1)

        def p2():
            a = b.cap("g02_antes")
            cx = b.acha("Caixa", 30)
            b.arrasta(cx, SOLTAR_DADO)
            d = b.cap("g02_depois")
            b.mudou(a, d, 0.8, oque="soltar a Caixa")
            b.reg("caixa", *par("g02"), cx, "Caixa", ate=SOLTAR_DADO)
            fecha("g02")
        passo(2, "arrastar a Caixa", p2)

        def p3():
            a = b.cap("g03_antes")
            b.escreve_campo("Comprimento", LADO)
            b.escreve_campo("Largura", LADO)
            alvo = b.escreve_campo("Altura", LADO)
            d = b.cap("g03_depois")
            b.mudou(a, d, 0.5, oque="medidas do dado")
            b.reg("medidas", *par("g03"), alvo, "Altura")
            fecha("g03")
            h = M.alcas_agora(b, "_dado")
            pt["topo"] = ((h["esq_tras"][0] + h["dir_tras"][0]) // 2, h["topo"][1])
            pt["frente"] = ((h["esq_frente"][0] + h["dir_frente"][0]) // 2, h["esq_frente"][1] - 40)
            pt["face"] = (pt["frente"][0], h["esq_frente"][1] - 98)
            print(f"     dado: tampa em {pt['topo']}, clique na frente em {pt['frente']}", flush=True)
        passo(3, "dado 60 × 60 × 60", p3)

        def p4():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g04_antes")
            esf = b.acha("Esfera", 30)
            b.arrasta(esf, pt["topo"])
            d = b.cap("g04_depois")
            b.mudou(a, d, 0.3, oque="soltar a Esfera")
            b.reg("esfera", *par("g04"), esf, "Esfera", ate=pt["topo"])
            fecha("g04")
        passo(4, "arrastar a Esfera para a tampa", p4)

        def p5():
            a = b.cap("g05_antes")
            alvo = b.acha("Orifício", 8)
            b.clica(alvo, 1800)
            d = b.cap("g05_depois")
            b.mudou(a, d, 0.05, oque="virar Orifício")
            b.reg("orificio", *par("g05"), alvo, "Orifício")
            fecha("g05")
        passo(5, "virar Orifício", p5)

        def p6():
            a = b.cap("g06_antes")
            teclas(pg, AFUNDA, "Control+ArrowDown")
            pg.wait_for_timeout(900)
            d = b.cap("g06_depois")
            b.mudou(a, d, 0.05, oque="afundar a esfera")
            b.reg("afunda", *par("g06"), pt["topo"], "Ctrl + ↓",
                  tipo="tecla", teclas=["Ctrl", "↓"])
            fecha("g06")
        passo(6, "afundar a esfera 10 mm (Ctrl + ↓)", p6)

        def p7():
            a = b.cap("g07_antes")
            teclas(pg, 1, "Shift+ArrowLeft"); teclas(pg, 6, "ArrowLeft")
            teclas(pg, 1, "Shift+ArrowDown"); teclas(pg, 6, "ArrowDown")
            pg.wait_for_timeout(900)
            d = b.cap("g07_depois")
            b.mudou(a, d, 0.03, oque="empurrar a esfera para o canto")
            b.reg("canto", *par("g07"), pt["frente"], "Shift + ←",
                  tipo="tecla", teclas=["Shift", "←"])
            fecha("g07")
        passo(7, "levar a esfera ao canto da frente (Shift + ← e Shift + ↓)", p7)

        def p8():
            a = b.cap("g08_antes")
            pg.keyboard.press("Control+d"); pg.wait_for_timeout(1500)
            teclas(pg, 1, "Shift+ArrowRight"); teclas(pg, 6, "ArrowRight")
            teclas(pg, 1, "Shift+ArrowUp"); teclas(pg, 6, "ArrowUp")
            pg.wait_for_timeout(900)
            d = b.cap("g08_depois")
            b.mudou(a, d, 0.03, oque="copiar e empurrar")
            b.reg("copia", *par("g08"), pt["frente"], "Ctrl + D",
                  tipo="tecla", teclas=["Ctrl", "D"])
            fecha("g08")
        passo(8, "Ctrl + D e empurrar a cópia para o meio", p8)

        def p9():
            a = b.cap("g09_antes")
            pg.keyboard.press("Control+d"); pg.wait_for_timeout(1800)
            d = b.cap("g09_depois")
            b.mudou(a, d, 0.03, oque="repetir")
            b.reg("repete", *par("g09"), pt["frente"], "Ctrl + D",
                  tipo="tecla", teclas=["Ctrl", "D"])
            fecha("g09")
        passo(9, "Ctrl + D de novo: a cópia se repete sozinha", p9)

        def p10():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g10_antes")
            esf = b.acha("Esfera", 30)
            b.arrasta(esf, pt["face"])
            d = b.cap("g10_depois")
            b.mudou(a, d, 0.3, oque="soltar a Esfera na face da frente")
            b.reg("esfera2", *par("g10"), esf, "Esfera", ate=pt["face"])
            fecha("g10")
        passo(10, "arrastar a Esfera para a face da frente", p10)

        def p11():
            a = b.cap("g11_antes")
            alvo = b.acha("Orifício", 8)
            b.clica(alvo, 1800)
            d = b.cap("g11_depois")
            b.mudou(a, d, 0.05, oque="virar Orifício")
            b.reg("orificio2", *par("g11"), alvo, "Orifício")
            fecha("g11")
        passo(11, "virar Orifício", p11)

        def p12():
            a = b.cap("g12_antes")
            teclas(pg, AFUNDA, "Control+ArrowDown")
            pg.wait_for_timeout(900)
            d = b.cap("g12_depois")
            b.mudou(a, d, 0.03, oque="afundar a esfera da frente")
            b.reg("afunda2", *par("g12"), pt["face"], "Ctrl + seta para baixo",
                  tipo="tecla", teclas=["Ctrl", "↓"])
            fecha("g12")
        passo(12, "afundar a esfera (Ctrl + ↓)", p12)

        def p16():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g16_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap("g16_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg("seleciona", *par("g16"), (600, 520), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            fecha("g16")
        passo(16, "Ctrl + A", p16)

        def p17():
            a = b.cap("g17_antes")
            alvo = b.acha_por_dica("Grupo de união")
            b.clica(alvo, 2800)
            d = b.cap("g17_depois")
            b.mudou(a, d, 0.2, oque="agrupar")
            b.reg("uniao", *par("g17"), alvo, "Grupo de união")
            fecha("g17")
        passo(17, "Grupo de união", p17)

        def p18():
            b.clica((250, 790), 900)
            a = b.cap("g18_antes")
            alvo = (63, 139)
            b.clica(alvo, 2400)
            d = b.cap("g18_depois")
            b.mudou(a, d, 1.0, oque="vista de cima")
            prova_dos_furos(b, d)
            b.reg("vista_cima", *par("g18"), alvo, "cubo SUPERIOR")
            fecha("g18")
        passo(18, "olhar de cima (os três furos)", p18)

        def p18b():
            a = b.cap("g18b_antes")
            b.clica(cap1.CASINHA, 2400)
            d = b.cap("g18b_depois")
            b.mudou(a, d, 1.0, oque="voltar à vista inicial")
            prova_do_furo_da_frente(d)
            b.reg("vista_inicial", *par("g18b"), cap1.CASINHA, "casinha")
            fecha("g18b")
        passo(18, "voltar à vista inicial (o furo do um)", p18b)

        def p18d():
            a = b.cap("g18d_antes")
            de, ate = (600, 760), (600 + 12 * 14, 760 - 12 * 5)
            pg.mouse.move(*de)
            pg.mouse.down(button="right"); pg.wait_for_timeout(300)
            for i in range(1, 13):
                pg.mouse.move(de[0] + i * 14, de[1] - i * 5); pg.wait_for_timeout(60)
            pg.mouse.up(button="right"); pg.wait_for_timeout(1600)
            d = b.cap("g18d_depois")
            b.mudou(a, d, 1.0, oque="girar a câmera")
            b.reg("girar", *par("g18d"), de, "plano de trabalho", ate=ate, botao="dir")
            fecha("g18d")
        passo(18, "girar a câmera (botão direito)", p18d)

        def p18c():
            a = b.cap("g18c_antes")
            alvo = b.acha("Aumentar o zoom" if False else "", 5) if False else (34, 352)
            for _ in range(2):
                pg.mouse.click(*alvo); pg.wait_for_timeout(900)
            pg.wait_for_timeout(900)
            d = b.cap("g18c_depois")
            b.mudou(a, d, 1.0, oque="aproximar")
            b.reg("zoom", *par("g18c"), alvo, "+", abre_janela=True)
            fecha("g18c")
        passo(18, "aproximar com o botão +", p18c)

        def p19():
            b.clica(cap1.CASINHA, 1800)
            a = b.cap("g19_antes")
            alvo = b.renomeia(BATIZADO)
            d = b.cap("g19_depois")
            b.mudou(a, d, 0.02, box=(0, 0, 500, 50), oque="trocar o nome")
            b.reg("batiza", *par("g19"), alvo, "nome do projeto")
            fecha("g19")
        passo(19, f"dar nome ao projeto ({BATIZADO})", p19)

        b.grava_alvos()
        print(f"\nalvos.json com {len(b.alvos)} gestos", flush=True)
        ctx.close()


if __name__ == "__main__":
    principal()
