"""Aula 6 — Foguete: corpo, ponta (Cone) e aletas em cruz por DUPLICAR e GIRAR.

O que é novo: Ctrl + D (duplica a seleção no mesmo lugar), mover a cópia com
Shift + seta, e DUPLICAR UM PAR (a cópia do par anda o mesmo que se andou).
Reaproveita o que as aulas 2–4 deram: medidas, girar em pé, Alinhar com forma
fixa e Shift + clique.

Uso:  ./pwenv/bin/python fonte/cap6.py
"""
import os, shutil, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou
import cap1
import mecanica as M

PASTA  = os.path.join(AQUI, "aula6")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
PROJ   = cap1.PROJ
BATIZADO = "Foguete da ANA"

CORPO = dict(largura=20, comprimento=20, altura=50)
PONTA = dict(largura=20, comprimento=20, altura=20)
ALETA = dict(comprimento=6, largura=40, altura=16)      # uma tira que ATRAVESSA o corpo: 2 aletas
SOLTAR_CORPO = (600, 560)
SOLTAR_ALETA = (820, 700)


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


def vermelho(captura):
    """Os blocos VERMELHOS (a aleta) na captura: [(x, y, area)], da esquerda p/ direita."""
    import numpy as np
    from scipy import ndimage
    im = np.asarray(Image.open(captura).convert("RGB"), dtype=int)
    m = (im[:, :, 0] > 150) & (im[:, :, 1] < 80) & (im[:, :, 2] < 90)
    m[:, 880:] = False; m[:100] = False
    m = ndimage.binary_opening(m, structure=np.ones((3, 3), bool))
    lab, n = ndimage.label(m)
    r = []
    for i in range(1, n + 1):
        ys, xs = np.nonzero(lab == i)
        if len(xs) >= 60:
            r.append((int(xs.mean()), int(ys.mean()), len(xs)))
    return sorted(r)


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
            b.mudou(a, d, 0.05, oque=f"alinhar {eixo}")
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
            cil = b.acha("Cilindro", 30)
            b.arrasta(cil, SOLTAR_CORPO)
            d = b.cap("g02_depois")
            b.mudou(a, d, 0.8, oque="soltar o Cilindro")
            b.reg("cilindro", *par("g02"), cil, "Cilindro", ate=SOLTAR_CORPO)
            fecha("g02")
        passo(2, "arrastar o Cilindro", p2)

        def p3():
            a = b.cap("g03_antes")
            alvo = M.muda_planta(b, CORPO["largura"], CORPO["comprimento"], nome="_alcasC")
            M.muda_altura(b, CORPO["altura"], nome="_alcasC2")
            d = b.cap("g03_depois")
            b.mudou(a, d, 0.3, oque="medidas do corpo")
            b.reg("medidas_corpo", *par("g03"), alvo, "alça do canto")
            fecha("g03")
            h = M.alcas_agora(b, "_corpo")
            pt["topo"] = h["topo"]
            pt["corpo"] = (h["topo"][0], (h["topo"][1] + h["esq_frente"][1]) // 2)
            print(f"     corpo: tampa em {pt['topo']}, ponto de clique {pt['corpo']}", flush=True)
        passo(3, "corpo 20 × 20 × 50", p3)

        def p4():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g04_antes")
            cone = b.acha("Cone", 20)
            b.arrasta(cone, pt["topo"])
            d = b.cap("g04_depois")
            b.mudou(a, d, 0.3, oque="soltar o Cone")
            b.reg("cone", *par("g04"), cone, "Cone", ate=pt["topo"])
            fecha("g04")
        passo(4, "arrastar o Cone para a tampa", p4)

        def p5():
            a = b.cap("g05_antes")
            alvo = M.muda_planta(b, PONTA["largura"], PONTA["comprimento"], nome="_alcasP")
            M.muda_altura(b, PONTA["altura"], nome="_alcasP2")
            d = b.cap("g05_depois")
            b.mudou(a, d, 0.1, oque="medidas da ponta")
            b.reg("medidas_ponta", *par("g05"), alvo, "alça do canto")
            fecha("g05")
        passo(5, "ponta 20 × 20 × 20", p5)

        def p10():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g10_antes")
            cx = b.acha("Caixa", 30)
            b.arrasta(cx, SOLTAR_ALETA)
            d = b.cap("g10_depois")
            b.mudou(a, d, 0.3, oque="soltar a Caixa da aleta")
            b.reg("caixa", *par("g10"), cx, "Caixa", ate=SOLTAR_ALETA)
            fecha("g10")
        passo(10, "arrastar uma Caixa (a aleta)", p10)

        def p11():
            a = b.cap("g11_antes")
            b.escreve_campo("Comprimento", ALETA["comprimento"])
            b.escreve_campo("Largura", ALETA["largura"])
            alvo = b.escreve_campo("Altura", ALETA["altura"])
            d = b.cap("g11_depois")
            b.mudou(a, d, 0.2, oque="medidas da aleta")
            b.reg("medidas_aleta", *par("g11"), alvo, "Altura")
            fecha("g11")
            h = M.alcas_agora(b, "_aleta")
            pt["aleta"] = ((h["esq_frente"][0] + h["dir_frente"][0]) // 2,
                           (h["esq_tras"][1] + h["esq_frente"][1]) // 2)
        passo(11, "aleta 40 × 6 × 16", p11)

        def p12():
            a = b.cap("g12_antes")
            pg.mouse.click(*pt["corpo"]); pg.wait_for_timeout(800)
            pg.keyboard.down("Shift")
            pg.mouse.click(*pt["aleta"]); pg.keyboard.up("Shift"); pg.wait_for_timeout(900)
            d = b.cap("g12_depois")
            b.mudou(a, d, 0.05, oque="corpo e aleta selecionados")
            b.reg("duas", *par("g12"), pt["aleta"], "aleta",
                  tipo="tecla", teclas=["Shift", "clique"])
            fecha("g12")
        passo(12, "clique no corpo e Shift + clique na aleta", p12)

        def p12b():
            a = b.cap("g12b_antes")
            alvo = b.acha_por_dica("Alinhar")
            b.clica(alvo, 1500)
            d = b.cap("g12b_depois")
            b.mudou(a, d, 0.3, oque="abrir o Alinhar")
            b.reg("alinhar2", *par("g12b"), alvo, "Alinhar")
            fecha("g12b")
        passo(12, "abrir o Alinhar", p12b)

        def p13():
            a = b.cap("g13_antes")
            b.clica(pt["corpo"], 1000)
            d = b.cap("g13_depois")
            b.mudou(a, d, 0.01, oque="fixar o corpo")
            b.reg("fixa2", *par("g13"), pt["corpo"], "corpo")
            fecha("g13")
        passo(13, "fixar o corpo", p13)

        passo(14, "aleta: centro em X", lambda: alinha_passo(14, "x", "centro", "alinha_x2", "bolinha do meio embaixo"))
        passo(15, "aleta: centro em Y", lambda: alinha_passo(15, "y", "centro", "alinha_y2", "bolinha do meio esquerda"))

        def p17():
            pg.keyboard.press("Escape"); pg.wait_for_timeout(700)
            pg.mouse.click(250, 790); pg.wait_for_timeout(600)
            vs = vermelho(b.cap("_vermelho"))
            print(f"     pontas vermelhas da aleta: {vs}", flush=True)
            if len(vs) < 2:
                raise Falhou(f"esperava as duas pontas vermelhas da aleta e vi {vs}")
            pt["ponta"] = (vs[0][0], vs[0][1])
            a = b.cap("g17_antes")
            pg.mouse.click(*pt["ponta"]); pg.wait_for_timeout(900)
            pg.keyboard.press("Control+d"); pg.wait_for_timeout(1500)
            d = b.cap("g17_depois")
            b.reg("duplica", *par("g17"), pt["ponta"], "Ctrl + D",
                  tipo="tecla", teclas=["Ctrl", "D"])
            fecha("g17")
        passo(17, "clicar na aleta e Ctrl + D", p17)

        def p18():
            h = M.alcas_agora(b, "_h18")
            seta = M.acha_setas_de_girar(os.path.join(PASTA, "_h18.png"), h, quer=("baixo",))["baixo"]
            a = b.cap("g18_antes")
            visto, _ = M.gira_em_arco(b, seta, 90)
            d = b.cap("g18_depois")
            b.mudou(a, d, 0.2, oque="girar a cópia")
            print(f"     transferidor: {visto}", flush=True)
            b.reg("gira", *par("g18"), seta, "seta curva de baixo",
                  ate=(seta[0] + 110, seta[1] - 70))
            fecha("g18")
        passo(18, "girar a cópia 90° (seta de baixo)", p18)

        def p19a():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g19a_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap("g19a_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg("seleciona", *par("g19a"), (600, 520), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            fecha("g19a")
        passo(19, "Ctrl + A", p19a)

        def p19():
            a = b.cap("g19_antes")
            alvo = b.acha_por_dica("Grupo de união")
            b.clica(alvo, 2800)
            d = b.cap("g19_depois")
            b.mudou(a, d, 0.2, oque="agrupar")
            b.reg("uniao", *par("g19"), alvo, "Grupo de união")
            fecha("g19")
        passo(19, "Grupo de união", p19)

        def p20():
            b.clica((250, 790), 900)
            a = b.cap("g20_antes")
            alvo = (63, 139)
            b.clica(alvo, 2200)
            d = b.cap("g20_depois")
            b.mudou(a, d, 1.0, oque="vista de cima")
            b.reg("vista_cima", *par("g20"), alvo, "cubo SUPERIOR")
            fecha("g20")
        passo(20, "olhar de cima (a cruz das aletas)", p20)

        def p20f():
            a = b.cap("g20f_antes")
            alvo = (63, 180)
            b.clica(alvo, 2200)
            d = b.cap("g20f_depois")
            b.mudou(a, d, 1.0, oque="vista de frente")
            b.reg("vista_frente", *par("g20f"), alvo, "cubo FRONTAL")
            fecha("g20f")
        passo(20, "olhar de frente", p20f)

        def p21():
            b.clica(cap1.CASINHA, 1800)
            a = b.cap("g21_antes")
            alvo = b.renomeia(BATIZADO)
            d = b.cap("g21_depois")
            b.mudou(a, d, 0.02, box=(0, 0, 500, 50), oque="trocar o nome")
            b.reg("batiza", *par("g21"), alvo, "nome do projeto")
            fecha("g21")
        passo(21, f"dar nome ao projeto ({BATIZADO})", p21)

        b.grava_alvos()
        print(f"\nalvos.json com {len(b.alvos)} gestos", flush=True)
        ctx.close()


if __name__ == "__main__":
    principal()
