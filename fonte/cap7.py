"""Aula 7 — Robô de formas: CORES, formas soltas na FACE de outra e o que agrupar faz com a cor.

O que é novo: Ctrl + D (duplica a seleção no mesmo lugar), mover a cópia com
Shift + seta, e DUPLICAR UM PAR (a cópia do par anda o mesmo que se andou).
Reaproveita o que as aulas 2–4 deram: medidas, girar em pé, Alinhar com forma
fixa e Shift + clique.

Uso:  ./pwenv/bin/python fonte/cap7.py
"""
import os, shutil, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou
import cap1
import mecanica as M

PASTA  = os.path.join(AQUI, "aula7")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
PROJ   = cap1.PROJ
BATIZADO = "Robô da ANA"

CORPO = dict(comprimento=40, largura=80, altura=36)
CABECA = dict(comprimento=36, largura=70, altura=30)
SOLTAR_CORPO = (600, 580)
OLHO_DX = 16          # mm para cada lado do centro da cabeça
PX_MM = 4.25          # pixels por mm na vista inicial (medido)


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
            b.mudou(a, d, 0.05, oque=f"alinhar {eixo}")
            b.reg(gesto, *par(f"g{n:02}"), ponto, rotulo)
            fecha(f"g{n:02}")

        def fecha_paleta():
            pg.mouse.click(976, 200); pg.wait_for_timeout(900)

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
            b.arrasta(cx, SOLTAR_CORPO)
            d = b.cap("g02_depois")
            b.mudou(a, d, 0.8, oque="soltar a Caixa")
            b.reg("caixa", *par("g02"), cx, "Caixa", ate=SOLTAR_CORPO)
            fecha("g02")
        passo(2, "arrastar a Caixa (o corpo)", p2)

        def p3():
            a = b.cap("g03_antes")
            b.escreve_campo("Comprimento", CORPO["comprimento"])
            b.escreve_campo("Largura", CORPO["largura"])
            alvo = b.escreve_campo("Altura", CORPO["altura"])
            d = b.cap("g03_depois")
            b.mudou(a, d, 0.3, oque="medidas do corpo")
            b.reg("medidas_corpo", *par("g03"), alvo, "Altura")
            fecha("g03")
            h = M.alcas_agora(b, "_corpo")
            pt["topo_corpo"] = ((h["esq_tras"][0] + h["dir_tras"][0]) // 2, h["topo"][1])
            pt["corpo"] = ((h["esq_frente"][0] + h["dir_frente"][0]) // 2,
                           (h["esq_tras"][1] + h["esq_frente"][1]) // 2 + 20)
        passo(3, "corpo 80 × 40 × 36", p3)

        def p4():
            a = b.cap("g04_antes")
            alvo = M.abre_paleta(b)
            d = b.cap("g04_depois", parar=False)
            b.mudou(a, d, 0.3, oque="abrir a paleta de cores")
            b.reg("paleta", *par("g04"), alvo, "Sólido", abre_janela=True)
            fecha("g04")
        passo(4, "abrir a paleta de cores", p4)

        def p5():
            a = b.cap("g05_antes", parar=False)
            alvo = M.pinta(b, "azul")
            d = b.cap("g05_depois", parar=False)
            b.mudou(a, d, 0.3, oque="pintar de azul")
            b.reg("azul", *par("g05"), alvo, "azul")
            fecha("g05")
            fecha_paleta()
        passo(5, "escolher o azul", p5)

        def p6():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g06_antes")
            cx = b.acha("Caixa", 30)
            b.arrasta(cx, pt["topo_corpo"])
            d = b.cap("g06_depois")
            b.mudou(a, d, 0.3, oque="soltar a Caixa da cabeça")
            b.reg("caixa_cabeca", *par("g06"), cx, "Caixa", ate=pt["topo_corpo"])
            fecha("g06")
        passo(6, "arrastar outra Caixa para a tampa (a cabeça)", p6)

        def p7():
            a = b.cap("g07_antes")
            b.escreve_campo("Comprimento", CABECA["comprimento"])
            b.escreve_campo("Largura", CABECA["largura"])
            alvo = b.escreve_campo("Altura", CABECA["altura"])
            d = b.cap("g07_depois")
            b.mudou(a, d, 0.3, oque="medidas da cabeça")
            b.reg("medidas_cabeca", *par("g07"), alvo, "Altura")
            fecha("g07")
        passo(7, "cabeça 70 × 36 × 30", p7)

        def p8():
            M.abre_paleta(b)
            a = b.cap("g08_antes", parar=False)
            alvo = M.pinta(b, "cinza-claro")
            d = b.cap("g08_depois", parar=False)
            b.mudou(a, d, 0.3, oque="pintar de cinza")
            b.reg("cinza", *par("g08"), alvo, "cinza claro")
            fecha("g08")
            fecha_paleta()
            h = M.alcas_agora(b, "_cabeca")
            pt["cabeca"] = ((h["esq_frente"][0] + h["dir_frente"][0]) // 2,
                            (h["esq_tras"][1] + h["esq_frente"][1]) // 2)
            pt["face"] = (pt["cabeca"][0], h["esq_frente"][1] - 88)
            pt["topo_cabeca"] = h["topo"]
            pt["face_larg"] = h["dir_frente"][0] - h["esq_frente"][0]
            print(f"     cabeça: clique {pt['cabeca']}, face da frente {pt['face']}", flush=True)
        passo(8, "cabeça cinza-claro", p8)

        def p13():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g13_antes")
            esf = b.acha("Esfera", 30)
            alvo_olho = (pt["face"][0] - int(OLHO_DX * PX_MM), pt["face"][1])
            b.arrasta(esf, alvo_olho)
            d = b.cap("g13_depois")
            b.mudou(a, d, 0.3, oque="soltar a Esfera na face")
            b.reg("olho", *par("g13"), esf, "Esfera", ate=alvo_olho)
            fecha("g13")
            pt["olho"] = alvo_olho
        passo(13, "arrastar a Esfera para a face da frente da cabeça", p13)

        def p14():
            M.abre_paleta(b)
            a = b.cap("g14_antes", parar=False)
            alvo = M.pinta(b, "amarelo")
            d = b.cap("g14_depois", parar=False)
            b.mudou(a, d, 0.2, oque="pintar de amarelo")
            b.reg("amarelo", *par("g14"), alvo, "amarelo")
            fecha("g14")
            fecha_paleta()
        passo(14, "olho amarelo", p14)

        def p15():
            a = b.cap("g15_antes")
            pg.keyboard.press("Control+d"); pg.wait_for_timeout(1500)
            for _ in range(3):
                pg.keyboard.press("Shift+ArrowRight"); pg.wait_for_timeout(300)
            pg.keyboard.press("ArrowRight"); pg.wait_for_timeout(300)
            pg.wait_for_timeout(900)
            d = b.cap("g15_depois")
            b.mudou(a, d, 0.1, oque="duplicar o olho")
            b.reg("duplica", *par("g15"), pt["olho"], "Ctrl + D",
                  tipo="tecla", teclas=["Ctrl", "D"])
            fecha("g15")
        passo(15, "Ctrl + D e empurrar o segundo olho", p15)

        def p15b():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g15b_antes")
            cone = b.acha("Cone", 20)
            b.arrasta(cone, pt["topo_cabeca"])
            d = b.cap("g15b_depois")
            b.mudou(a, d, 0.3, oque="soltar o Cone")
            b.reg("cone", *par("g15b"), cone, "Cone", ate=pt["topo_cabeca"])
            fecha("g15b")
        passo(15, "arrastar o Cone para a tampa da cabeça", p15b)

        def p15c():
            M.abre_paleta(b)
            a = b.cap("g15c_antes", parar=False)
            alvo = M.pinta(b, "vermelho")
            d = b.cap("g15c_depois", parar=False)
            b.mudou(a, d, 0.2, oque="pintar de vermelho")
            b.reg("vermelho", *par("g15c"), alvo, "vermelho")
            fecha("g15c")
            fecha_paleta()
        passo(15, "chapéu vermelho", p15c)

        def p15d():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g15d_antes")
            de, ate = (600, 760), (600 + 12*14, 760 - 12*5)
            pg.mouse.move(*de)
            pg.mouse.down(button="right"); pg.wait_for_timeout(300)
            for i in range(1, 13):
                pg.mouse.move(de[0] + i*14, de[1] - i*5); pg.wait_for_timeout(60)
            pg.mouse.up(button="right"); pg.wait_for_timeout(1600)
            d = b.cap("g15d_depois")
            b.mudou(a, d, 1.0, oque="girar a câmera")
            b.reg("girar", *par("g15d"), de, "plano de trabalho", ate=ate, botao="dir")
            fecha("g15d")
        passo(15, "girar a câmera (botão direito)", p15d)

        def p16():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g16_antes")
            b.clica((63, 180), 2400)
            d = b.cap("g16_depois")
            b.mudou(a, d, 1.0, oque="vista de frente")
            b.reg("vista_frente", *par("g16"), (63, 180), "cubo FRONTAL")
            fecha("g16")
        passo(16, "olhar de frente", p16)

        def p17a():
            b.clica(cap1.CASINHA, 1800)
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g17a_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap("g17a_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg("seleciona", *par("g17a"), (600, 520), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            fecha("g17a")
        passo(17, "Ctrl + A", p17a)

        def p17():
            a = b.cap("g17_antes")
            alvo = b.acha_por_dica("Grupo de união")
            b.clica(alvo, 2800)
            d = b.cap("g17_depois")
            b.mudou(a, d, 0.3, oque="agrupar")
            b.reg("uniao", *par("g17"), alvo, "Grupo de união")
            fecha("g17")
        passo(17, "Grupo de união (a cor some)", p17)

        def p18():
            a = b.cap("g18_antes")
            pg.keyboard.press("Control+z"); pg.wait_for_timeout(1800)
            d = b.cap("g18_depois")
            b.mudou(a, d, 0.3, oque="desfazer o agrupar")
            b.reg("desfaz", *par("g18"), (600, 520), "Ctrl + Z",
                  tipo="tecla", teclas=["Ctrl", "Z"])
            fecha("g18")
        passo(18, "Ctrl + Z", p18)

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
