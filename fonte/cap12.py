"""Aula 12 — Projeto livre e mostra: um totem de quatro peças e o caminho até MOSTRAR.

O exemplo é um totem (base, coluna, chapéu), cada peça com a sua cor. O que a aula
ensina é o CAMINHO de um projeto próprio: planejar, montar com o que as aulas deram,
conferir, e MOSTRAR: Enviar para (imagem do projeto) e Exportar (arquivos .STL / .OBJ).
Nenhum arquivo é baixado e nada é publicado: só se abrem os diálogos.
"""
import os, shutil, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou
import cap1
import mecanica as M

PASTA  = os.path.join(AQUI, "aula12")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
PROJ   = cap1.PROJ
BATIZADO = "Totem da ANA"
BASE = dict(comprimento=40, largura=40, altura=10)
COLUNA = dict(d=20, altura=40)
CONE = dict(d=20, altura=24)
SOLTAR_BASE = (600, 600)
ENVIAR = (1387, 72)
EXPORTAR = (1299, 72)


def copia_dos_passos_do_site():
    os.makedirs(PASTA, exist_ok=True)
    for nome in ("d01_site.jpg", "d02_antes.jpg", "d02_depois.jpg", "d03_marcado.jpg", "d03_menu.jpg",
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

        def pinta(n, gesto, cor):
            a = b.cap(f"g{n:02}_antes", parar=False)
            alvo = M.abre_paleta(b)
            M.pinta(b, cor)
            pg.mouse.click(976, 200); pg.wait_for_timeout(900)      # fecha a janela
            d = b.cap(f"g{n:02}_depois")
            b.mudou(a, d, 0.1, oque=f"pintar de {cor}")
            b.reg(gesto, *par(f"g{n:02}"), alvo, "bolinha de cor", abre_janela=True)
            fecha(f"g{n:02}")

        def mostra(n, gesto, ponto, rotulo, oque):
            pg.keyboard.press("Escape"); pg.wait_for_timeout(500)
            a = b.cap(f"g{n:02}_antes", parar=False)
            pg.mouse.click(*ponto); pg.wait_for_timeout(1800)
            d = b.cap(f"g{n:02}_depois", parar=False)
            b.mudou(a, d, 2.0, oque=oque)
            b.reg(gesto, *par(f"g{n:02}"), ponto, rotulo, abre_janela=True)
            fecha(f"g{n:02}")

        print(f"abrindo {PROJ}", flush=True)
        pg.goto(PROJ, wait_until="domcontentloaded", timeout=60000)
        cap1.espera_editor(pg)
        cap1.limpa(b)
        pg.mouse.click(1302, 132); pg.wait_for_timeout(1200)
        pg.keyboard.press("Escape"); pg.wait_for_timeout(900)
        pg.mouse.click(250, 790); pg.wait_for_timeout(600)
        with open(os.path.join(PASTA, "projeto.txt"), "w") as f:
            f.write(f"{PROJ}\n{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("plano limpo, vista inicial. começando os passos:\n", flush=True)

        pt = {}

        def p1():
            b.cap("p01_vazio"); b.jpg("p01_vazio")
        passo(1, "o projeto novo, vazio (planejar)", p1)

        def p2():
            a = b.cap("g02_antes")
            cx = b.acha("Caixa", 30)
            b.arrasta(cx, SOLTAR_BASE)
            d = b.cap("g02_depois")
            b.mudou(a, d, 0.8, oque="soltar a Caixa")
            b.reg("caixa", *par("g02"), cx, "Caixa", ate=SOLTAR_BASE)
            fecha("g02")
        passo(2, "arrastar a Caixa (a base)", p2)

        def topo_de(nome):
            h = M.alcas_agora(b, nome)
            return ((h["esq_tras"][0] + h["dir_tras"][0]) // 2, h["topo"][1] + 6)

        def p3():
            a = b.cap("g03_antes")
            b.escreve_campo("Comprimento", BASE["comprimento"])
            b.escreve_campo("Largura", BASE["largura"])
            alvo = b.escreve_campo("Altura", BASE["altura"])
            d = b.cap("g03_depois")
            b.mudou(a, d, 0.2, oque="medidas da base")
            b.reg("medidas_base", *par("g03"), alvo, "Altura")
            fecha("g03")
        passo(3, "base 40 × 40 × 10", p3)

        passo(4, "pintar a base de verde", lambda: pinta(4, "azul", "verde"))

        def p5():
            pt["topo"] = topo_de("_base")
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g05_antes")
            cil = b.acha("Cilindro", 30)
            b.arrasta(cil, pt["topo"])
            d = b.cap("g05_depois")
            b.mudou(a, d, 0.3, oque="soltar o Cilindro na tampa")
            b.reg("cilindro", *par("g05"), cil, "Cilindro", ate=pt["topo"])
            fecha("g05")
        passo(5, "arrastar o Cilindro para a tampa da base", p5)

        def p6():
            a = b.cap("g06_antes")
            alvo = M.muda_planta(b, COLUNA["d"], COLUNA["d"], nome="_alcasC")
            M.muda_altura(b, COLUNA["altura"], nome="_alcasC2")
            d = b.cap("g06_depois")
            b.mudou(a, d, 0.1, oque="medidas da coluna")
            b.reg("medidas_coluna", *par("g06"), alvo, "alça do canto")
            fecha("g06")
        passo(6, "coluna 20 × 20 × 40, pelas alças", p6)

        passo(7, "pintar a coluna de amarelo", lambda: pinta(7, "amarelo", "amarelo"))

        def p8():
            pt["topo2"] = topo_de("_col")
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g08_antes")
            cone = b.acha("Cone", 20)
            b.arrasta(cone, pt["topo2"])
            d = b.cap("g08_depois")
            b.mudou(a, d, 0.3, oque="soltar o Cone")
            b.reg("cone", *par("g08"), cone, "Cone", ate=pt["topo2"])
            fecha("g08")
        passo(8, "arrastar o Cone para a tampa da coluna", p8)

        def p9():
            a = b.cap("g09_antes")
            alvo = M.muda_planta(b, CONE["d"], CONE["d"], nome="_alcasK")
            M.muda_altura(b, CONE["altura"], nome="_alcasK2")
            d = b.cap("g09_depois")
            b.mudou(a, d, 0.1, oque="medidas do chapéu")
            b.reg("medidas_cone", *par("g09"), alvo, "alça do canto")
            fecha("g09")
        passo(9, "chapéu 20 × 20 × 24, pelas alças", p9)

        passo(10, "pintar o chapéu de vermelho", lambda: pinta(10, "vermelho", "vermelho"))

        def p11():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g11_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap("g11_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg("seleciona", *par("g11"), (600, 520), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            fecha("g11")
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
        passo(11, "Ctrl + A: são três peças (não agrupe: cor some)", p11)

        def p12():
            a = b.cap("g12_antes")
            de, ate = (600, 780), (600 + 12 * 14, 780 - 12 * 5)
            pg.mouse.move(*de)
            pg.mouse.down(button="right"); pg.wait_for_timeout(300)
            for i in range(1, 13):
                pg.mouse.move(de[0] + i * 14, de[1] - i * 5); pg.wait_for_timeout(60)
            pg.mouse.up(button="right"); pg.wait_for_timeout(1600)
            d = b.cap("g12_depois")
            b.mudou(a, d, 1.0, oque="girar a câmera")
            b.reg("girar", *par("g12"), de, "plano de trabalho", ate=ate, botao="dir")
            fecha("g12")
        passo(12, "girar a câmera (botão direito)", p12)

        def p13():
            a = b.cap("g13_antes")
            alvo = (63, 180)
            b.clica(alvo, 2400)
            d = b.cap("g13_depois")
            b.mudou(a, d, 1.0, oque="vista de frente")
            b.reg("vista_frente", *par("g13"), alvo, "cubo FRONTAL")
            fecha("g13")
        passo(13, "olhar de frente", p13)

        def p14():
            b.clica(cap1.CASINHA, 1800)
            a = b.cap("g14_antes")
            alvo = b.renomeia(BATIZADO)
            d = b.cap("g14_depois")
            b.mudou(a, d, 0.02, box=(0, 0, 500, 50), oque="trocar o nome")
            b.reg("batiza", *par("g14"), alvo, "nome do projeto")
            fecha("g14")
        passo(14, f"dar nome ao projeto ({BATIZADO})", p14)

        passo(15, "Enviar para: a imagem do projeto",
              lambda: mostra(15, "enviar", ENVIAR, "Enviar para", "abrir o Enviar para"))
        passo(16, "Exportar: .STL e .OBJ",
              lambda: mostra(16, "exportar", EXPORTAR, "Exportar", "abrir o Exportar"))

        pg.keyboard.press("Escape"); pg.wait_for_timeout(500)
        b.grava_alvos()
        print(f"\nalvos.json com {len(b.alvos)} gestos", flush=True)
        ctx.close()


if __name__ == "__main__":
    principal()
