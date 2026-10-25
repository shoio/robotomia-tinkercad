"""Aula 11 — Peça que encaixa: um furo de 12 mm e um pino de 10 mm (folga de 1 mm de cada lado).

O que é novo: FOLGA. O pino com o MESMO diâmetro do furo não entraria numa peça
impressa de verdade; com 12 contra 10 sobra 1 mm em volta, e é isso que se vê de cima
como um anel escuro entre o pino e a placa. Reaproveita: cilindro pelas alças,
Orifício, Alinhar com forma fixa, Shift + clique e União.
"""
import os, shutil, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou
import cap1
import mecanica as M

PASTA  = os.path.join(AQUI, "aula11")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
PROJ   = cap1.PROJ
BATIZADO = "Encaixe da ANA"
PLACA = dict(comprimento=40, largura=40, altura=8)
FURO = 12
PINO = dict(d=10, altura=20)
SOLTAR_PLACA = (600, 560)
SOLTAR_CIL = (330, 650)


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


def prova_da_folga(captura):
    """Vista de cima: vai da borda do pino (laranja) para fora e exige um anel que
    NÃO é laranja nem vermelho (o chão visto pela folga) antes de a placa começar.
    Controle: o centro é laranja e mais longe há vermelho."""
    import numpy as np
    im = np.asarray(Image.open(captura).convert("RGB"), dtype=int)
    lar = (im[:, :, 0] > 200) & (im[:, :, 1] > 90) & (im[:, :, 1] < 170) & (im[:, :, 2] < 90)
    ver = (im[:, :, 0] > 150) & (im[:, :, 1] < 90) & (im[:, :, 2] < 90)
    lar[:, 880:] = False; lar[:100] = False; ver[:, 880:] = False; ver[:100] = False
    ys, xs = np.nonzero(lar)
    if len(xs) < 800:
        raise Falhou("não achei o pino laranja na vista de cima")
    cx, cy = int(xs.mean()), int(ys.mean())
    linha_l, linha_v = lar[cy], ver[cy]
    dir_ = [x for x in range(cx, 880) if linha_l[x]]
    if not dir_:
        raise Falhou("o pino sumiu da linha do meio")
    borda_pino = max(dir_)
    placa = [x for x in range(borda_pino, 880) if linha_v[x]]
    if not placa:
        raise Falhou("não achei a placa vermelha ao lado do pino")
    folga_px = min(placa) - borda_pino - 1
    esc = (max(dir_) - min(x for x in range(0, cx) if linha_l[x])) / PINO["d"]
    print(f"     folga vista de cima: {folga_px} px = {folga_px / esc:.2f} mm (esperado 1 mm); {esc:.1f} px/mm", flush=True)
    if not (0.5 <= folga_px / esc <= 1.8):
        raise Falhou(f"a folga devia ser ~1 mm e mede {folga_px / esc:.2f} mm")


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

        def seleciona_e_alinha(n, gesto, ponto_fixo, rotulo):
            """(Ctrl + A | seleção já feita) -> Alinhar -> fixa a peça de `ponto_fixo`."""
            a = b.cap(f"g{n:02}_antes")
            alvo = b.acha_por_dica("Alinhar")
            b.clica(alvo, 1500)
            b.clica(ponto_fixo, 1000)
            d = b.cap(f"g{n:02}_depois", parar=False)
            b.mudou(a, d, 0.3, oque="abrir o Alinhar")
            b.reg(gesto, *par(f"g{n:02}"), alvo, "Alinhar")
            fecha(f"g{n:02}")

        print(f"abrindo {PROJ}", flush=True)
        pg.goto(PROJ, wait_until="domcontentloaded", timeout=60000)
        cap1.espera_editor(pg)
        cap1.limpa(b)
        # a régua da aula anterior fica salva no projeto: um clique a tira, Esc sai do modo
        pg.mouse.click(1302, 132); pg.wait_for_timeout(1200)
        pg.keyboard.press("Escape"); pg.wait_for_timeout(900)
        pg.mouse.click(250, 790); pg.wait_for_timeout(600)
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
            b.arrasta(cx, SOLTAR_PLACA)
            d = b.cap("g02_depois")
            b.mudou(a, d, 0.8, oque="soltar a Caixa")
            b.reg("caixa", *par("g02"), cx, "Caixa", ate=SOLTAR_PLACA)
            fecha("g02")
        passo(2, "arrastar a Caixa (a placa)", p2)

        def p3():
            a = b.cap("g03_antes")
            b.escreve_campo("Comprimento", PLACA["comprimento"])
            b.escreve_campo("Largura", PLACA["largura"])
            alvo = b.escreve_campo("Altura", PLACA["altura"])
            d = b.cap("g03_depois")
            b.mudou(a, d, 0.3, oque="medidas da placa")
            b.reg("medidas_placa", *par("g03"), alvo, "Altura")
            fecha("g03")
            h = M.alcas_agora(b, "_placa")
            pt["placa"] = ((h["esq_frente"][0] + h["dir_frente"][0]) // 2, h["esq_frente"][1] - 22)
            print(f"     placa: clique {pt['placa']}", flush=True)
        passo(3, "placa 40 × 40 × 8", p3)

        def p4():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g04_antes")
            cil = b.acha("Cilindro", 30)
            b.arrasta(cil, SOLTAR_CIL)
            d = b.cap("g04_depois")
            b.mudou(a, d, 0.3, oque="soltar o Cilindro")
            b.reg("cilindro", *par("g04"), cil, "Cilindro", ate=SOLTAR_CIL)
            fecha("g04")
        passo(4, "arrastar o Cilindro (o furo)", p4)

        def p5():
            a = b.cap("g05_antes")
            alvo = M.muda_planta(b, FURO, FURO, nome="_alcasF")
            M.muda_altura(b, 12, nome="_alcasF2")
            d = b.cap("g05_depois")
            b.mudou(a, d, 0.1, oque="medidas do furo")
            b.reg("medidas_furo", *par("g05"), alvo, "alça do canto")
            fecha("g05")
        passo(5, "furo 12 × 12 × 12, pelas alças", p5)

        def p6():
            a = b.cap("g06_antes")
            alvo = b.acha("Orifício", 8)
            b.clica(alvo, 1800)
            d = b.cap("g06_depois")
            b.mudou(a, d, 0.05, oque="virar Orifício")
            b.reg("orificio", *par("g06"), alvo, "Orifício")
            fecha("g06")
        passo(6, "virar Orifício", p6)

        def p7():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            b.tecla("Meta+A", 1200)
            seleciona_e_alinha(7, "alinhar", pt["placa"], "placa")
        passo(7, "Ctrl + A, Alinhar e fixar a placa", p7)

        passo(8, "furo: centro em X", lambda: alinha_passo(8, "x", "centro", "alinha_x", "bolinha do meio embaixo"))
        passo(9, "furo: centro em Y", lambda: alinha_passo(9, "y", "centro", "alinha_y", "bolinha do meio esquerda"))

        def p10():
            pg.keyboard.press("Escape"); pg.wait_for_timeout(700)
            a = b.cap("g10_antes")
            alvo = b.acha_por_dica("Grupo de união")
            b.clica(alvo, 2800)
            d = b.cap("g10_depois")
            b.mudou(a, d, 0.1, oque="agrupar")
            b.reg("uniao", *par("g10"), alvo, "Grupo de união")
            fecha("g10")
            pg.mouse.click(250, 790); pg.wait_for_timeout(600)
        passo(10, "Esc e Grupo de união", p10)

        def p11():
            a = b.cap("g11_antes")
            cil = b.acha("Cilindro", 30)
            b.arrasta(cil, SOLTAR_CIL)
            d = b.cap("g11_depois")
            b.mudou(a, d, 0.3, oque="soltar o Cilindro do pino")
            b.reg("cilindro2", *par("g11"), cil, "Cilindro", ate=SOLTAR_CIL)
            fecha("g11")
        passo(11, "arrastar outro Cilindro (o pino)", p11)

        def p12():
            a = b.cap("g12_antes")
            alvo = M.muda_planta(b, PINO["d"], PINO["d"], nome="_alcasP")
            M.muda_altura(b, PINO["altura"], nome="_alcasP2")
            d = b.cap("g12_depois")
            b.mudou(a, d, 0.1, oque="medidas do pino")
            b.reg("medidas_pino", *par("g12"), alvo, "alça do canto")
            fecha("g12")
            h = M.alcas_agora(b, "_pino")
            pt["pino"] = ((h["esq_frente"][0] + h["dir_frente"][0]) // 2, (h["esq_tras"][1] + h["esq_frente"][1]) // 2 + 8)
        passo(12, "pino 10 × 10 × 20, pelas alças", p12)

        def p14():
            a = b.cap("g14_antes")
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            pg.mouse.click(*pt["placa"]); pg.wait_for_timeout(800)
            pg.keyboard.down("Shift")
            pg.mouse.click(*pt["pino"]); pg.keyboard.up("Shift"); pg.wait_for_timeout(900)
            d = b.cap("g14_depois")
            b.mudou(a, d, 0.03, oque="placa e pino selecionados")
            b.reg("duas", *par("g14"), pt["pino"], "pino",
                  tipo="tecla", teclas=["Shift", "clique"])
            fecha("g14")
        passo(14, "clicar na placa e Shift + clique no pino", p14)

        passo(15, "Alinhar e fixar a placa", lambda: seleciona_e_alinha(15, "alinhar2", pt["placa"], "placa"))
        passo(16, "pino: centro em X", lambda: alinha_passo(16, "x", "centro", "alinha_x2", "bolinha do meio embaixo"))
        passo(17, "pino: centro em Y", lambda: alinha_passo(17, "y", "centro", "alinha_y2", "bolinha do meio esquerda"))

        def p18():
            pg.keyboard.press("Escape"); pg.wait_for_timeout(700)
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g18_antes")
            alvo = (63, 139)
            b.clica(alvo, 2400)
            d = b.cap("g18_depois")
            b.mudou(a, d, 1.0, oque="vista de cima")
            prova_da_folga(os.path.join(PASTA, "g18_depois.png"))
            b.reg("vista_cima", *par("g18"), alvo, "cubo SUPERIOR")
            fecha("g18")
        passo(18, "olhar de cima: a folga", p18)

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
