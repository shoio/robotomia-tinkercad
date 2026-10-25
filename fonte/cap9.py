"""Aula 9 — Porta-celular: uma base, um encosto INCLINADO e um batente.

O que é novo: a seta curva do LADO (inclinar para trás: gira em torno do eixo
esquerda-direita) e o Alinhar 'atrás'/'frente' com a base FIXA. Reaproveita
medidas, Shift + clique, Alinhar, união e a câmera.

Uso:  ./pwenv/bin/python fonte/cap9.py
"""
import os, shutil, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou
import cap1
import mecanica as M

PASTA  = os.path.join(AQUI, "aula9")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
PROJ   = cap1.PROJ
BATIZADO = "Porta-celular da ANA"

BASE = dict(comprimento=60, largura=60, altura=6)
ENCOSTO = dict(comprimento=6, largura=60, altura=70)
BATENTE = dict(comprimento=6, largura=60, altura=14)
SOLTAR_BASE = (600, 600)
INCLINA_MIN = 20          # graus (em módulo) — vai para trás


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

        def ctrl_a(n, gesto):
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap(f"g{n:02}_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap(f"g{n:02}_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg(gesto, *par(f"g{n:02}"), (600, 520), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            fecha(f"g{n:02}")

        def abre_alinhar(n, gesto):
            a = b.cap(f"g{n:02}_antes")
            alvo = b.acha_por_dica("Alinhar")
            b.clica(alvo, 1500)
            d = b.cap(f"g{n:02}_depois")
            b.mudou(a, d, 0.3, oque="abrir o Alinhar")
            b.reg(gesto, *par(f"g{n:02}"), alvo, "Alinhar")
            fecha(f"g{n:02}")

        def fixa(n, gesto, ponto, rotulo):
            a = b.cap(f"g{n:02}_antes")
            b.clica(ponto, 1000)
            d = b.cap(f"g{n:02}_depois")
            b.mudou(a, d, 0.01, oque="fixar a base")
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
            b.arrasta(cx, SOLTAR_BASE)
            d = b.cap("g02_depois")
            b.mudou(a, d, 0.8, oque="soltar a Caixa")
            b.reg("caixa", *par("g02"), cx, "Caixa", ate=SOLTAR_BASE)
            fecha("g02")
        passo(2, "arrastar a Caixa (a base)", p2)

        def p3():
            a = b.cap("g03_antes")
            b.escreve_campo("Comprimento", BASE["comprimento"])
            b.escreve_campo("Largura", BASE["largura"])
            alvo = b.escreve_campo("Altura", BASE["altura"])
            d = b.cap("g03_depois")
            b.mudou(a, d, 0.3, oque="medidas da base")
            b.reg("medidas_base", *par("g03"), alvo, "Altura")
            fecha("g03")
            h = M.alcas_agora(b, "_base")
            # a base fica ESCONDIDA atrás do batente e debaixo do encosto: só a faixa
            # da tampa entre os dois (97 px acima da quina da frente) é dela
            pt["base"] = ((h["esq_frente"][0] + h["dir_frente"][0]) // 2, h["esq_frente"][1] - 97)
            pt["frente_bat"] = ((h["esq_frente"][0] + h["dir_frente"][0]) // 2, h["esq_frente"][1] - 35)
            pt["tampa"] = ((h["esq_tras"][0] + h["dir_tras"][0]) // 2, (h["esq_tras"][1] + h["esq_frente"][1]) // 2)
            pt["tampa_tras"] = (pt["tampa"][0], h["esq_tras"][1] + 40)
            pt["tampa_frente"] = (pt["tampa"][0], h["esq_frente"][1] - 30)
            print(f"     base: clique {pt['base']}, tampa {pt['tampa']}", flush=True)
        passo(3, "base 60 × 60 × 6", p3)

        def p4():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g04_antes")
            cx = b.acha("Caixa", 30)
            b.arrasta(cx, pt["tampa_tras"])
            d = b.cap("g04_depois")
            b.mudou(a, d, 0.3, oque="soltar a Caixa do encosto")
            b.reg("caixa_encosto", *par("g04"), cx, "Caixa", ate=pt["tampa_tras"])
            fecha("g04")
        passo(4, "arrastar outra Caixa para a base (o encosto)", p4)

        def p5():
            a = b.cap("g05_antes")
            b.escreve_campo("Comprimento", ENCOSTO["comprimento"])
            b.escreve_campo("Largura", ENCOSTO["largura"])
            alvo = b.escreve_campo("Altura", ENCOSTO["altura"])
            d = b.cap("g05_depois")
            b.mudou(a, d, 0.3, oque="medidas do encosto")
            b.reg("medidas_encosto", *par("g05"), alvo, "Altura")
            fecha("g05")
        passo(5, "encosto 60 × 6 × 70", p5)

        def p6():
            h = M.alcas_agora(b, "_h6")
            seta = M.acha_seta_do_lado(os.path.join(PASTA, "_h6.png"), h)
            a = b.cap("g06_antes")
            visto, _ = M.inclina(b, seta, INCLINA_MIN, sinal=-1)
            d = b.cap("g06_depois")
            b.mudou(a, d, 0.3, oque="inclinar o encosto")
            print(f"     transferidor: {visto}", flush=True)
            b.reg("inclina", *par("g06"), seta, "seta curva do lado",
                  ate=(seta[0], seta[1] - 60))
            fecha("g06")
        passo(6, "inclinar o encosto para trás", p6)

        passo(7, "Ctrl + A", lambda: ctrl_a(7, "seleciona"))
        passo(8, "abrir o Alinhar", lambda: abre_alinhar(8, "alinhar"))
        passo(9, "fixar a base", lambda: fixa(9, "fixa", pt["base"], "base"))
        passo(10, "encosto: encostar atrás", lambda: alinha_passo(10, "y", "atras", "alinha_atras", "bolinha de cima esquerda"))

        def p11():
            pg.keyboard.press("Escape"); pg.wait_for_timeout(700)
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g11_antes")
            cx = b.acha("Caixa", 30)
            b.arrasta(cx, pt["tampa_frente"])
            d = b.cap("g11_depois")
            b.mudou(a, d, 0.3, oque="soltar a Caixa do batente")
            b.reg("caixa_batente", *par("g11"), cx, "Caixa", ate=pt["tampa_frente"])
            fecha("g11")
        passo(11, "arrastar mais uma Caixa para a frente da base (o batente)", p11)

        def p12():
            a = b.cap("g12_antes")
            b.escreve_campo("Comprimento", BATENTE["comprimento"])
            b.escreve_campo("Largura", BATENTE["largura"])
            alvo = b.escreve_campo("Altura", BATENTE["altura"])
            d = b.cap("g12_depois")
            b.mudou(a, d, 0.2, oque="medidas do batente")
            b.reg("medidas_batente", *par("g12"), alvo, "Altura")
            fecha("g12")
            pt["batente"] = pt["frente_bat"]
        passo(12, "batente 60 × 6 × 14", p12)

        def p13():
            a = b.cap("g13_antes")
            pg.mouse.click(250, 790); pg.wait_for_timeout(400)
            pg.mouse.click(*pt["base"]); pg.wait_for_timeout(800)
            pg.keyboard.down("Shift")
            pg.mouse.click(*pt["batente"]); pg.keyboard.up("Shift"); pg.wait_for_timeout(900)
            d = b.cap("g13_depois")
            b.mudou(a, d, 0.03, oque="base e batente selecionados")
            b.reg("duas", *par("g13"), pt["batente"], "batente",
                  tipo="tecla", teclas=["Shift", "clique"])
            fecha("g13")
        passo(13, "clicar na base e Shift + clique no batente", p13)

        passo(14, "abrir o Alinhar de novo", lambda: abre_alinhar(14, "alinhar2"))
        passo(15, "fixar a base", lambda: fixa(15, "fixa2", pt["base"], "base"))
        passo(16, "batente: rente à frente", lambda: alinha_passo(16, "y", "frente", "alinha_frente", "bolinha de baixo esquerda"))

        def p17():
            pg.keyboard.press("Escape"); pg.wait_for_timeout(700)
            ctrl_a(17, "seleciona3")
        passo(17, "Esc e Ctrl + A", p17)

        def p18():
            a = b.cap("g18_antes")
            alvo = b.acha_por_dica("Grupo de união")
            b.clica(alvo, 2800)
            d = b.cap("g18_depois")
            b.mudou(a, d, 0.2, oque="agrupar")
            b.reg("uniao", *par("g18"), alvo, "Grupo de união")
            fecha("g18")
        passo(18, "Grupo de união", p18)

        def p19():
            b.clica((250, 790), 900)
            a = b.cap("g19_antes")
            de, ate = (600, 780), (600 + 12 * 14, 780 - 12 * 5)
            pg.mouse.move(*de)
            pg.mouse.down(button="right"); pg.wait_for_timeout(300)
            for i in range(1, 13):
                pg.mouse.move(de[0] + i * 14, de[1] - i * 5); pg.wait_for_timeout(60)
            pg.mouse.up(button="right"); pg.wait_for_timeout(1600)
            d = b.cap("g19_depois")
            b.mudou(a, d, 1.0, oque="girar a câmera")
            b.reg("girar", *par("g19"), de, "plano de trabalho", ate=ate, botao="dir")
            fecha("g19")
        passo(19, "girar a câmera (botão direito)", p19)

        def p20():
            b.clica(cap1.CASINHA, 1800)
            a = b.cap("g20_antes")
            alvo = b.renomeia(BATIZADO)
            d = b.cap("g20_depois")
            b.mudou(a, d, 0.02, box=(0, 0, 500, 50), oque="trocar o nome")
            b.reg("batiza", *par("g20"), alvo, "nome do projeto")
            fecha("g20")
        passo(20, f"dar nome ao projeto ({BATIZADO})", p20)

        b.grava_alvos()
        print(f"\nalvos.json com {len(b.alvos)} gestos", flush=True)
        ctx.close()


if __name__ == "__main__":
    principal()
