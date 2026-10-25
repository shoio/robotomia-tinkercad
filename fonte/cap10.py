"""Aula 10 — Régua e escala: dez cubos de 10 mm viram uma barra de 10 cm, medida com a Régua.

O que é novo: a ferramenta RÉGUA (a que fica na coluna da direita, ao lado do plano
de trabalho): ela cria uma origem no plano, e ao selecionar uma peça mostra as
distâncias dela até a origem e as medidas. E o Ctrl + D que SE REPETE (Aula 8)
fazendo uma fileira de nove cópias com um empurrão só. Escala: o dobro de cada lado.
"""
import os, shutil, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou
import cap1
import mecanica as M

PASTA  = os.path.join(AQUI, "aula10")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
PROJ   = cap1.PROJ
BATIZADO = "Régua da ANA"
REGUA = (1302, 132)
LADO = 10
DOBRO = 20


def copia_dos_passos_do_site():
    os.makedirs(PASTA, exist_ok=True)
    for nome in ("d02_antes.jpg", "d02_depois.jpg", "d03_marcado.jpg", "d03_menu.jpg",
                 "d01_site.jpg", "alvos0.json", "painel.txt"):
        for de in ("aula2", "aula1"):
            o = os.path.join(AQUI, de, nome)
            if os.path.exists(o):
                shutil.copy2(o, os.path.join(PASTA, nome)); break
    os.makedirs(os.path.join(PASTA, "gifs"), exist_ok=True)
    o = os.path.join(AQUI, "aula2", "gifs", "criar.gif")
    if os.path.exists(o):
        shutil.copy2(o, os.path.join(PASTA, "gifs", "criar.gif"))


def largura_vermelha(b, nome):
    """Largura em px da silhueta vermelha (a barra) na captura `nome`."""
    import numpy as np
    im = np.asarray(Image.open(os.path.join(PASTA, nome)).convert("RGB"), dtype=int)
    m = (im[:, :, 0] > 150) & (im[:, :, 1] < 90) & (im[:, :, 2] < 90)
    m[:, 880:] = False; m[:100] = False
    ys, xs = np.nonzero(m)
    if len(xs) < 300:
        raise Falhou("não achei a peça vermelha")
    return int(xs.max() - xs.min() + 1)


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

        def teclas(vezes, tecla):
            for _ in range(vezes):
                pg.keyboard.press(tecla); pg.wait_for_timeout(300)

        print(f"abrindo {PROJ}", flush=True)
        pg.goto(PROJ, wait_until="domcontentloaded", timeout=60000)
        cap1.espera_editor(pg)
        cap1.limpa(b)
        with open(os.path.join(PASTA, "projeto.txt"), "w") as f:
            f.write(f"{PROJ}\n{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("plano limpo, vista inicial. começando os passos:\n", flush=True)

        pt = {}

        # ⛔ A RÉGUA FICA SALVA no projeto: depois de uma execução ela continua lá, e
        #    o `limpa` (Ctrl+A, Delete) não a apaga. Um clique no ícone a remove (ou
        #    entra no modo de colocar); Esc sai do modo. Sem isto as dez primeiras
        #    figuras saíam com a régua do ensaio anterior desenhada no plano.
        pg.mouse.click(*REGUA); pg.wait_for_timeout(1200)
        pg.keyboard.press("Escape"); pg.wait_for_timeout(900)
        pg.mouse.click(250, 790); pg.wait_for_timeout(600)

        def p1():
            b.cap("p01_vazio"); b.jpg("p01_vazio")
        passo(1, "o projeto novo, vazio", p1)

        SOLTAR = (330, 640)

        def p2():
            a = b.cap("g02_antes")
            cx = b.acha("Caixa", 30)
            b.arrasta(cx, SOLTAR)
            d = b.cap("g02_depois")
            b.mudou(a, d, 0.5, oque="soltar a Caixa")
            b.reg("caixa", *par("g02"), cx, "Caixa", ate=SOLTAR)
            fecha("g02")
        passo(2, "arrastar a Caixa", p2)

        def p3():
            a = b.cap("g03_antes")
            b.escreve_campo("Comprimento", LADO)
            b.escreve_campo("Largura", LADO)
            alvo = b.escreve_campo("Altura", LADO)
            d = b.cap("g03_depois")
            b.mudou(a, d, 0.1, oque="cubo de 10")
            b.reg("medidas", *par("g03"), alvo, "Altura")
            fecha("g03")
        passo(3, "cubo 10 × 10 × 10", p3)

        def p4():
            a = b.cap("g04_antes")
            pg.keyboard.press("Control+d"); pg.wait_for_timeout(1500)
            teclas(1, "Shift+ArrowRight")
            pg.wait_for_timeout(900)
            d = b.cap("g04_depois")
            b.mudou(a, d, 0.03, oque="copiar e empurrar 10 mm")
            b.reg("copia", *par("g04"), SOLTAR, "Ctrl + D",
                  tipo="tecla", teclas=["Ctrl", "D"])
            fecha("g04")
        passo(4, "Ctrl + D e Shift + → (10 mm)", p4)

        def p5():
            a = b.cap("g05_antes")
            for _ in range(8):
                pg.keyboard.press("Control+d"); pg.wait_for_timeout(1300)
            pg.wait_for_timeout(900)
            d = b.cap("g05_depois")
            b.mudou(a, d, 0.3, oque="repetir oito vezes")
            larg = largura_vermelha(b, "g05_depois.png")
            print(f"     fileira de 10 cubos: {larg} px de largura", flush=True)
            if larg < 380:
                raise Falhou(f"a fileira deveria ter ~10 cubos e tem só {larg} px")
            b.reg("repete", *par("g05"), SOLTAR, "Ctrl + D",
                  tipo="tecla", teclas=["Ctrl", "D"])
            fecha("g05")
        passo(5, "Ctrl + D oito vezes", p5)

        def p6():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g06_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap("g06_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg("seleciona", *par("g06"), (600, 520), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            fecha("g06")
        passo(6, "Ctrl + A", p6)

        def p7():
            a = b.cap("g07_antes")
            alvo = b.acha_por_dica("Grupo de união")
            b.clica(alvo, 2800)
            d = b.cap("g07_depois")
            b.mudou(a, d, 0.1, oque="agrupar")
            b.reg("uniao", *par("g07"), alvo, "Grupo de união")
            fecha("g07")
        passo(7, "Grupo de união", p7)

        def p8():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g08_antes")
            pg.mouse.click(*REGUA); pg.wait_for_timeout(1200)
            d = b.cap("g08_depois", parar=False)
            b.mudou(a, d, 0.5, box=(1170, 100, 1440, 170), oque="abrir a Régua (o ícone fica marcado)")
            b.reg("regua", *par("g08"), REGUA, "Régua", abre_janela=True)
            fecha("g08")
        passo(8, "escolher a Régua", p8)

        def p9():
            a = b.cap("g09_antes", parar=False)
            alvo = (380, 665)
            pg.mouse.click(*alvo); pg.wait_for_timeout(1300)
            d = b.cap("g09_depois", parar=False)
            b.mudou(a, d, 0.01, oque="pôr a régua no plano")
            b.reg("origem", *par("g09"), alvo, "plano de trabalho", abre_janela=True)
            fecha("g09")
        passo(9, "clicar no plano: a origem da régua", p9)

        def p10():
            a = b.cap("g10_antes", parar=False)
            pg.mouse.click(*SOLTAR); pg.wait_for_timeout(1500)
            rot = [t[0] for t in M.rotulos_de_medida(pg)]
            print(f"     números na tela: {rot}", flush=True)
            if "100.00" not in rot:
                raise Falhou(f"a barra devia medir 100.00 mm e os números são {rot}")
            d = b.cap("g10_depois", parar=False)
            b.mudou(a, d, 0.1, oque="selecionar a barra com a régua")
            b.reg("mede", *par("g10"), SOLTAR, "barra", abre_janela=True)
            fecha("g10")
        passo(10, "clicar na barra: a medida de 100", p10)

        def p10b():
            a = b.cap("g10b_antes", parar=False)
            antes = [t[0] for t in M.rotulos_de_medida(pg)]
            teclas(2, "Shift+ArrowUp")
            pg.wait_for_timeout(900)
            depois = [t[0] for t in M.rotulos_de_medida(pg)]
            print(f"     números antes {antes} e depois {depois}", flush=True)
            if depois == antes:
                raise Falhou("empurrei a barra e os números da régua não mudaram")
            d = b.cap("g10b_depois", parar=False)
            b.mudou(a, d, 0.05, oque="empurrar a barra")
            b.reg("empurra", *par("g10b"), SOLTAR, "Shift + ↑",
                  tipo="tecla", teclas=["Shift", "↑"])
            fecha("g10b")
        passo(10, "Shift + ↑ duas vezes: os números mudam", p10b)

        def p10c():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g10c_antes")
            alvo = (63, 139)
            b.clica(alvo, 2400)
            d = b.cap("g10c_depois")
            b.mudou(a, d, 1.0, oque="vista de cima")
            b.reg("vista_cima", *par("g10c"), alvo, "cubo SUPERIOR")
            fecha("g10c")
            b.clica(cap1.CASINHA, 1800)
        passo(10, "olhar de cima", p10c)

        def p10d():
            a = b.cap("g10d_antes")
            pg.mouse.click(*REGUA); pg.wait_for_timeout(1200)
            pg.keyboard.press("Escape"); pg.wait_for_timeout(900)
            d = b.cap("g10d_depois", parar=False)
            b.mudou(a, d, 0.05, oque="tirar a régua")
            b.reg("tira_regua", *par("g10d"), REGUA, "Régua", abre_janela=True)
            fecha("g10d")
        passo(10, "tirar a régua", p10d)

        def p11():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g11_antes")
            cx = b.acha("Caixa", 30)
            alvo = (700, 520)
            b.arrasta(cx, alvo)
            # ⛔ a Caixa nova nasce com o TAMANHO DA ÚLTIMA que se mexeu (20, de uma
            #    execução anterior; no site, o que a criança mexeu por último):
            #    o passo promete um cubo de 10 — confere e acerta, calado.
            for rot in ("Comprimento", "Largura", "Altura"):
                b.escreve_campo(rot, LADO)
            d = b.cap("g11_depois")
            b.mudou(a, d, 0.3, oque="soltar outra Caixa")
            b.reg("caixa2", *par("g11"), cx, "Caixa", ate=alvo)
            fecha("g11")
        passo(11, "arrastar outra Caixa", p11)

        def p12():
            a = b.cap("g12_antes")
            b.escreve_campo("Comprimento", DOBRO)
            b.escreve_campo("Largura", DOBRO)
            alvo = b.escreve_campo("Altura", DOBRO)
            d = b.cap("g12_depois")
            b.mudou(a, d, 0.1, oque="o dobro")
            b.reg("dobro", *par("g12"), alvo, "Altura")
            fecha("g12")
        passo(12, "cubo 20 × 20 × 20: o dobro", p12)

        def p13():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            b.clica(cap1.CASINHA, 1800)
            a = b.cap("g13_antes")
            alvo = b.renomeia(BATIZADO)
            d = b.cap("g13_depois")
            b.mudou(a, d, 0.02, box=(0, 0, 500, 50), oque="trocar o nome")
            b.reg("batiza", *par("g13"), alvo, "nome do projeto")
            fecha("g13")
        passo(13, f"dar nome ao projeto ({BATIZADO})", p13)

        b.grava_alvos()
        print(f"\nalvos.json com {len(b.alvos)} gestos", flush=True)
        ctx.close()


if __name__ == "__main__":
    principal()
