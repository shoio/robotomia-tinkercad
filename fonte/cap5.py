"""Aula 5 — Carrinho: quatro rodas iguais por DUPLICAR (Ctrl + D) e REPETIR.

O que é novo: Ctrl + D (duplica a seleção no mesmo lugar), mover a cópia com
Shift + seta, e DUPLICAR UM PAR (a cópia do par anda o mesmo que se andou).
Reaproveita o que as aulas 2–4 deram: medidas, girar em pé, Alinhar com forma
fixa e Shift + clique.

Uso:  ./pwenv/bin/python fonte/cap5.py
"""
import os, shutil, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou
import cap1
import mecanica as M

PASTA  = os.path.join(AQUI, "aula5")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
PROJ   = cap1.PROJ
BATIZADO = "Carrinho da ANA"

CARRO = dict(comprimento=60, largura=30, altura=16)      # comprido na PROFUNDIDADE
RODA = dict(largura=20, comprimento=20, altura=6)        # cilindro: 6 mm de grosso
SOLTAR_CARRO = (600, 560)
SOLTAR_RODA = (330, 650)
X_ESQ = (1, 7)        # Shift+← ×1 e ← ×7  = 17 mm para a esquerda
Y_FRENTE = 2          # Shift+↓ ×2         = 20 mm para a frente
X_DIREITA = (3, 4)    # Shift+→ ×3 e → ×4  = 34 mm: a roda do outro lado
Y_TRAS = 4            # Shift+↑ ×4         = 40 mm: o par de trás


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

        print(f"abrindo {PROJ}", flush=True)
        pg.goto(PROJ, wait_until="domcontentloaded", timeout=60000)
        cap1.espera_editor(pg)
        cap1.limpa(b)
        with open(os.path.join(PASTA, "projeto.txt"), "w") as f:
            f.write(f"{PROJ}\n{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("plano limpo, vista inicial. começando os passos:\n", flush=True)

        corpo = {}

        def p1():
            b.cap("p01_vazio"); b.jpg("p01_vazio")
        passo(1, "o projeto novo, vazio", p1)

        def p2():
            a = b.cap("g02_antes")
            cx = b.acha("Caixa", 30)
            b.arrasta(cx, SOLTAR_CARRO)
            d = b.cap("g02_depois")
            b.mudou(a, d, 0.8, oque="soltar a Caixa")
            b.reg("caixa", *par("g02"), cx, "Caixa", ate=SOLTAR_CARRO)
            fecha("g02")
        passo(2, "arrastar a Caixa", p2)

        def p3():
            a = b.cap("g03_antes")
            b.escreve_campo("Comprimento", CARRO["comprimento"])
            b.escreve_campo("Largura", CARRO["largura"])
            alvo = b.escreve_campo("Altura", CARRO["altura"])
            d = b.cap("g03_depois")
            b.mudou(a, d, 0.3, oque="medidas do carro")
            b.reg("medidas_carro", *par("g03"), alvo, "Altura")
            fecha("g03")
            h = M.alcas_agora(b, "_carro")
            corpo["ponto"] = ((h["esq_frente"][0] + h["dir_frente"][0]) // 2,
                              (h["esq_tras"][1] + h["esq_frente"][1]) // 2)
            print(f"     o carro: ponto de clique {corpo['ponto']}", flush=True)
        passo(3, "carro 30 × 60 × 16", p3)

        def p4():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g04_antes")
            cil = b.acha("Cilindro", 30)
            b.arrasta(cil, SOLTAR_RODA)
            d = b.cap("g04_depois")
            b.mudou(a, d, 0.3, oque="soltar o Cilindro")
            b.reg("cilindro", *par("g04"), cil, "Cilindro", ate=SOLTAR_RODA)
            fecha("g04")
        passo(4, "arrastar o Cilindro", p4)

        def p5():
            a = b.cap("g05_antes")
            alvo = M.muda_planta(b, RODA["largura"], RODA["comprimento"], nome="_alcasR")
            M.muda_altura(b, RODA["altura"], nome="_alcasR2")
            d = b.cap("g05_depois")
            b.mudou(a, d, 0.1, oque="medidas da roda")
            b.reg("medidas_roda", *par("g05"), alvo, "alça do canto")
            fecha("g05")
        passo(5, "roda 20 × 20 × 6", p5)

        def p6():
            # depois de digitar numa alça, ela continua ATIVA (vermelha) e a seta
            # de girar não responde: um clique na própria roda a solta
            hh = M.alcas_agora(b, "_h6a")
            pg.mouse.click((hh["esq_tras"][0] + hh["dir_frente"][0]) // 2,
                           (hh["esq_tras"][1] + hh["dir_frente"][1]) // 2 + 6)
            pg.wait_for_timeout(900)
            h = M.alcas_agora(b, "_h6")
            seta = M.acha_setas_de_girar(os.path.join(PASTA, "_h6.png"), h, quer=("cima",))["cima"]
            a = b.cap("g06_antes")
            visto, _ = M.gira(b, seta, 90)
            d = b.cap("g06_depois")
            b.mudou(a, d, 0.1, oque="girar a roda em pé")
            print(f"     transferidor: {visto}", flush=True)
            b.reg("gira", *par("g06"), seta, "seta curva de cima",
                  ate=(seta[0] + 60, seta[1] + 45))
            fecha("g06")
        passo(6, "girar a roda em pé", p6)

        def p7():
            a = b.cap("g07_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap("g07_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg("seleciona", *par("g07"), (600, 520), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            fecha("g07")
        passo(7, "Ctrl + A", p7)

        def p8():
            a = b.cap("g08_antes")
            alvo = b.acha_por_dica("Alinhar")
            b.clica(alvo, 1500)
            d = b.cap("g08_depois")
            b.mudou(a, d, 0.3, oque="abrir o Alinhar")
            b.reg("alinhar", *par("g08"), alvo, "Alinhar")
            fecha("g08")
        passo(8, "abrir o Alinhar", p8)

        def p9():
            a = b.cap("g09_antes")
            b.clica(corpo["ponto"], 1000)
            d = b.cap("g09_depois")
            b.mudou(a, d, 0.01, oque="fixar o carro")
            b.reg("fixa", *par("g09"), corpo["ponto"], "carro")
            fecha("g09")
        passo(9, "fixar o carro", p9)

        def alinha_passo(n, eixo, qual, gesto, rotulo):
            a = b.cap(f"g{n:02}_antes")
            ponto = M.alinha(b, eixo, qual, captura=f"_alinha{n}")
            d = b.cap(f"g{n:02}_depois", parar=False)
            b.mudou(a, d, 0.05, oque=f"alinhar {eixo}")
            b.reg(gesto, *par(f"g{n:02}"), ponto, rotulo)
            fecha(f"g{n:02}")

        passo(10, "centro em Y", lambda: alinha_passo(10, "y", "centro", "alinha_y", "bolinha do meio esquerda"))
        passo(11, "centro em Z", lambda: alinha_passo(11, "z", "centro", "alinha_z", "bolinha do meio direita"))
        passo(12, "centro em X", lambda: alinha_passo(12, "x", "centro", "alinha_x", "bolinha do meio embaixo"))

        def p13():
            pg.keyboard.press("Escape"); pg.wait_for_timeout(900)
            a = b.cap("g13_antes")
            pg.keyboard.down("Shift")
            b.clica(corpo["ponto"], 1000)
            pg.keyboard.up("Shift"); pg.wait_for_timeout(500)
            d = b.cap("g13_depois")
            b.mudou(a, d, 0.05, oque="tirar o carro da seleção")
            b.reg("so_a_roda", *par("g13"), corpo["ponto"], "carro",
                  tipo="tecla", teclas=["Shift", "clique"])
            fecha("g13")
        passo(13, "Shift + clique no carro", p13)

        def p14():
            a = b.cap("g14_antes")
            teclas(pg, X_ESQ[0], "Shift+ArrowLeft"); teclas(pg, X_ESQ[1], "ArrowLeft")
            teclas(pg, Y_FRENTE, "Shift+ArrowDown")
            pg.wait_for_timeout(900)
            d = b.cap("g14_depois")
            b.mudou(a, d, 0.1, oque="empurrar a roda")
            b.reg("empurra", *par("g14"), corpo["ponto"], "Shift + seta para a esquerda",
                  tipo="tecla", teclas=["Shift", "←"])
            fecha("g14")
        passo(14, "empurrar a roda (esquerda e frente)", p14)

        def p16():
            a = b.cap("g16_antes")
            # Ctrl + D sozinho NÃO muda nada na tela (a cópia nasce em cima da
            # original): por isso ele e o empurrão são UM clipe só
            pg.keyboard.press("Control+d"); pg.wait_for_timeout(1500)
            teclas(pg, X_DIREITA[0], "Shift+ArrowRight"); teclas(pg, X_DIREITA[1], "ArrowRight")
            pg.wait_for_timeout(900)
            d = b.cap("g16_depois")
            b.mudou(a, d, 0.1, oque="empurrar a cópia")
            b.reg("duplica", *par("g16"), corpo["ponto"], "Ctrl + D",
                  tipo="tecla", teclas=["Ctrl", "D"])
            fecha("g16")
        passo(16, "Ctrl + D e empurrar a cópia", p16)

        def rodas_na_tela(captura):
            """Os centros das rodas LARANJA na captura, da esquerda para a direita."""
            import numpy as np
            from scipy import ndimage
            im = np.asarray(Image.open(captura).convert("RGB"), dtype=int)
            m = (im[:, :, 0] > 190) & (im[:, :, 1] > 90) & (im[:, :, 1] < 170) & (im[:, :, 2] < 90)
            m[:, 880:] = False; m[:100] = False
            m = ndimage.binary_opening(m, structure=np.ones((3, 3), bool))
            lab, n = ndimage.label(m)
            r = []
            for i in range(1, n + 1):
                ys, xs = np.nonzero(lab == i)
                if len(xs) >= 60:
                    r.append((int(xs.mean()), int(ys.mean()), len(xs)))
            return sorted(r)

        duas = {}

        def p17():
            pg.mouse.click(250, 790); pg.wait_for_timeout(600)
            rodas = rodas_na_tela(b.cap("_rodas"))
            print(f"     rodas na tela: {rodas}", flush=True)
            if len(rodas) != 2:
                raise Falhou(f"esperava 2 rodas laranja e achei {len(rodas)}: {rodas}")
            duas["p"] = [(r[0], r[1]) for r in rodas]
            a = b.cap("g17_antes")
            pg.mouse.click(*duas["p"][0]); pg.wait_for_timeout(800)
            pg.keyboard.down("Shift")
            pg.mouse.click(*duas["p"][1]); pg.keyboard.up("Shift"); pg.wait_for_timeout(900)
            d = b.cap("g17_depois")
            b.mudou(a, d, 0.05, oque="duas rodas selecionadas")
            b.reg("duas_rodas", *par("g17"), duas["p"][1], "roda",
                  tipo="tecla", teclas=["Shift", "clique"])
            fecha("g17")
        passo(17, "escolher as duas rodas", p17)

        def p18():
            a = b.cap("g18_antes")
            pg.keyboard.press("Control+d"); pg.wait_for_timeout(1500)
            teclas(pg, Y_TRAS, "Shift+ArrowUp")
            pg.wait_for_timeout(900)
            d = b.cap("g18_depois")
            b.mudou(a, d, 0.3, oque="duplicar o par")
            b.reg("duplica_par", *par("g18"), duas["p"][1], "Ctrl + D",
                  tipo="tecla", teclas=["Ctrl", "D"])
            fecha("g18")
        passo(18, "Ctrl + D no par e Shift + ↑", p18)

        def p19():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            b.tecla("Meta+A", 900)
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
            alvo = (63, 139)                      # a face SUPERIOR do cubo
            b.clica(alvo, 2200)
            d = b.cap("g20_depois")
            b.mudou(a, d, 1.0, oque="vista de cima")
            b.reg("vista_cima", *par("g20"), alvo, "cubo SUPERIOR")
            fecha("g20")
        passo(20, "olhar de cima", p20)

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
