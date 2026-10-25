#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 3 — Caneca com alça: o porta-lápis ganha uma alça (um anel em pé).

A aula PARTE do porta-lápis da Aula 2: o aluno o copia (Ctrl + C), abre um
projeto novo e cola (Ctrl + V) — copiar e colar entre projetos é a ferramenta
nova do começo. Depois vêm o Tórulo, as duas setas de GIRAR, o Alinhar com uma
peça FIXA e as setas do teclado para empurrar.

Dois projetos do Tinkercad (e só dois, para não encher a conta do dono):
  A = TINK_PROJ    guarda o porta-lápis (refeito, calado, no começo de cada execução)
  B = TINK_PROJ_B  o projeto «novo» da aula, limpo no começo

Uso:  ./pwenv/bin/python fonte/cap3.py
"""
import os, shutil, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou
import cap1, cap2
import mecanica as M

PASTA  = os.path.join(AQUI, "aula3")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
PROJ_A = cap1.PROJ
PROJ_B = os.environ.get("TINK_PROJ_B", "https://www.tinkercad.com/things/9PAC22X5A1T/edit")
NOME_A = "Porta-lápis da ANA"
SORTEADO_B = "Brilliant Trug-Migelo"
BATIZADO = "Caneca da ANA"

RAIO, TUBO = 14, 4            # o anel: 14 mm de raio até o meio do tubo, tubo de 4 mm
# 4 × Shift+← = 40 mm. O anel tem 18 mm de raio por fora (14 + 4) e a caneca 25: com o
# centro 40 mm à esquerda, a ponta direita do anel fica em −22 — DENTRO da parede
# (−25 a −21) por 3 mm, e sem entrar no vazio da caneca (que começa em −21).
# (Com 41 sobravam só 2 mm de encosto; com 38 o anel invadia o vazio.)
EMPURRA_DEZ, EMPURRA_UM = 4, 0


def monta_porta_lapis(b):
    """O porta-lápis da Aula 2, feito calado (sem foto) no projeto A."""
    pg = b.pg
    cil = b.acha("Cilindro", 30)
    b.arrasta(cil, cap2.SOLTAR_1)
    M.muda_planta(b, cap2.D_CORPO, cap2.D_CORPO); M.muda_altura(b, cap2.H_CORPO)
    pg.mouse.click(250, 790); pg.wait_for_timeout(400)
    b.arrasta(cil, cap2.SOLTAR_2)
    b.clica(b.acha("Orifício", 8), 1500)
    M.muda_planta(b, cap2.D_FURO, cap2.D_FURO); M.muda_altura(b, cap2.H_FURO)
    for _ in range(cap2.FUNDO):
        pg.keyboard.press("Control+ArrowUp"); pg.wait_for_timeout(250)
    b.tecla("Meta+A", 900)
    b.clica(b.acha_por_dica("Alinhar"), 1500)
    M.alinha(b, "x", "centro"); M.alinha(b, "y", "centro")
    pg.keyboard.press("Escape"); pg.wait_for_timeout(800)
    b.clica(b.acha_por_dica("Grupo de união"), 2500)
    pg.mouse.click(250, 790); pg.wait_for_timeout(600)
    pg.mouse.click(*cap1.CASINHA); pg.wait_for_timeout(1800)


def bbox_laranja(captura):
    """Caixa (x0, y0, x1, y1) da peça laranja (a caneca) na captura."""
    im = Image.open(captura).convert("RGB")
    xs, ys = [], []
    for y in range(110, 880, 3):
        for x in range(60, 880, 3):
            r, g, bl = im.getpixel((x, y))
            if r > 190 and 80 < g < 175 and bl < 100:
                xs.append(x); ys.append(y)
    if len(xs) < 200:
        raise Falhou("não achei a caneca laranja na captura")
    return (min(xs), min(ys), max(xs), max(ys))


def principal():
    os.makedirs(PASTA, exist_ok=True)
    # as figuras do site (passo 4) são as da Aula 1/2 — mesma razão da Aula 2
    for nome in ("d02_antes.jpg", "d02_depois.jpg", "d03_marcado.jpg", "d03_menu.jpg",
                 "alvos0.json", "painel.txt"):
        for de in ("aula2", "aula1"):
            o = os.path.join(AQUI, de, nome)
            if os.path.exists(o):
                shutil.copy2(o, os.path.join(PASTA, nome)); break
    os.makedirs(os.path.join(PASTA, "gifs"), exist_ok=True)
    for nome in ("criar.gif",):
        o = os.path.join(AQUI, "aula2", "gifs", nome)
        if os.path.exists(o):
            shutil.copy2(o, os.path.join(PASTA, "gifs", nome))

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

        # ---- a preparação, calada: o porta-lápis no projeto A ------------------
        print("preparando o projeto A (o porta-lápis da Aula 2)…", flush=True)
        pg.goto(PROJ_A, wait_until="domcontentloaded", timeout=60000)
        cap1.espera_editor(pg)
        cap1.limpa(b)
        monta_porta_lapis(b)
        b.renomeia(NOME_A)
        with open(os.path.join(PASTA, "projeto.txt"), "w") as f:
            f.write(f"{PROJ_A}\n{PROJ_B}\n{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("projeto A pronto. começando os passos:\n", flush=True)

        # 1 — o porta-lápis aberto ---------------------------------------------
        def p1():
            b.cap("p01_porta_lapis"); b.jpg("p01_porta_lapis")
        passo(1, "o porta-lápis da Aula 2, aberto", p1)

        # 2 — Ctrl + A -----------------------------------------------------------
        def p2():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g02_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap("g02_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg("seleciona", *par("g02"), (600, 520), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            fecha("g02")
            # Ctrl + C não muda NADA na tela (medido: 0,00 % — o botão Colar já
            # nasce aceso), então não vira clipe: é a segunda metade do passo.
            b.tecla("Meta+C", 1200)
        passo(2, "Ctrl + A e Ctrl + C", p2)

        # 4 — o projeto novo (B) -----------------------------------------------
        #     No site as figuras são as da Aula 1 (o painel do dono não vai para a web).
        def p4():
            pg.goto(PROJ_B, wait_until="domcontentloaded", timeout=60000)
            cap1.espera_editor(pg)
            pg.mouse.click(600, 790); pg.wait_for_timeout(400)
            b.tecla("Meta+A", 900); b.tecla("Delete", 1500)
            pg.mouse.click(*cap1.CASINHA); pg.wait_for_timeout(1800)
            b.renomeia(SORTEADO_B)
            b.cap("p04_novo_vazio"); b.jpg("p04_novo_vazio")
        passo(4, "o projeto novo, vazio", p4)

        # 5 — Ctrl + V -----------------------------------------------------------
        corpo = {}

        def p5():
            pg.mouse.click(600, 790); pg.wait_for_timeout(400)
            a = b.cap("g05_antes")
            b.tecla("Meta+V", 3000)
            d = b.cap("g05_depois")
            b.mudou(a, d, 0.5, oque="colar o porta-lápis")
            corpo["caixa"] = bbox_laranja(d)
            print(f"     o porta-lápis colado ocupa {corpo['caixa']}", flush=True)
            b.reg("cola", *par("g05"), (600, 520), "Ctrl + V",
                  tipo="tecla", teclas=["Ctrl", "V"])
            fecha("g05")
        passo(5, "Ctrl + V", p5)

        # 6 — o Tórulo, ao lado direito -----------------------------------------
        def p6():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            x0, y0, x1, y1 = corpo["caixa"]
            # À ESQUERDA da caneca: o porta-lápis colado cai na metade direita do
            # plano, e um anel solto ali tem alças debaixo do painel de propriedades
            # (medido: a de trás à direita some, e a leitura exige as cinco)
            onde = (max(x0 - 190, 360), min((y0 + y1) // 2 + 90, 700))
            a = b.cap("g06_antes")
            tor = b.acha("Tórulo", 20)
            b.arrasta(tor, onde)
            d = b.cap("g06_depois")
            b.mudou(a, d, 0.3, oque="soltar o Tórulo")
            b.reg("torulo", *par("g06"), tor, "Tórulo", ate=onde)
            fecha("g06")
        passo(6, "arrastar o Tórulo", p6)

        # 7 — Raio e Tubo (campos do painel) ------------------------------------
        def p7():
            a = b.cap("g07_antes")
            b.escreve_campo("Raio", RAIO)
            alvo = b.escreve_campo("Tubo", TUBO)
            d = b.cap("g07_depois")
            b.mudou(a, d, 0.2, oque="Raio e Tubo")
            b.reg("raio_tubo", *par("g07"), alvo, "Tubo")
            fecha("g07")
        passo(7, f"Raio = {RAIO}, Tubo = {TUBO}", p7)

        # 8 — girar o anel EM PÉ (seta de cima) -------------------------------------
        def p8():
            h = M.alcas_agora(b, "_h8")
            seta = M.acha_setas_de_girar(os.path.join(PASTA, "_h8.png"), h, quer=("cima",))["cima"]
            a = b.cap("g08_antes")
            visto, meio = M.gira(b, seta, 90)
            d = b.cap("g08_depois")
            b.mudou(a, d, 0.2, oque="girar o anel em pé")
            print(f"     transferidor: {visto}", flush=True)
            b.reg("gira_cima", *par("g08"), seta, "seta curva de cima",
                  ate=(seta[0] + 60, seta[1] + 45), botao="esq")
            fecha("g08")
        passo(8, "girar em pé (seta de cima)", p8)

        # 9 — virar o anel DE FRENTE (seta de baixo) ----------------------------------
        def p9():
            h = M.alcas_agora(b, "_h9")
            seta = M.acha_setas_de_girar(os.path.join(PASTA, "_h9.png"), h, quer=("baixo",))["baixo"]
            a = b.cap("g09_antes")
            visto, meio = M.gira_em_arco(b, seta, 90)
            d = b.cap("g09_depois")
            b.mudou(a, d, 0.2, oque="virar o anel de frente")
            print(f"     transferidor: {visto}", flush=True)
            b.reg("gira_baixo", *par("g09"), seta, "seta curva de baixo",
                  ate=(seta[0] + 110, seta[1] - 70), botao="esq")
            fecha("g09")
        passo(9, "virar de frente (seta de baixo)", p9)

        # 10 — Ctrl + A ---------------------------------------------------------
        def p10():
            a = b.cap("g10_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap("g10_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg("seleciona2", *par("g10"), (600, 520), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            fecha("g10")
        passo(10, "Ctrl + A", p10)

        # 11 — o botão Alinhar ----------------------------------------------------
        def p11():
            a = b.cap("g11_antes")
            alvo = b.acha_por_dica("Alinhar")
            b.clica(alvo, 1500)
            d = b.cap("g11_depois")
            b.mudou(a, d, 0.3, oque="abrir o Alinhar")
            b.reg("alinhar", *par("g11"), alvo, "Alinhar")
            fecha("g11")
        passo(11, "abrir o Alinhar", p11)

        # 12 — FIXAR a caneca: clicar nela ---------------------------------------
        #     ⛔ O Alinhar move TODAS as formas até uma linha comum: sem fixar a
        #        caneca, ela é que anda até o anel (e o anel some dentro dela).
        #        Clicar numa forma selecionada a fixa no lugar.
        ponto_caneca = {}

        def p12():
            x0, y0, x1, y1 = corpo["caixa"]
            ponto_caneca["p"] = ((x0 + x1) // 2, y0 + (y1 - y0) * 2 // 3)
            a = b.cap("g12_antes")
            b.clica(ponto_caneca["p"], 1000)
            d = b.cap("g12_depois")
            b.mudou(a, d, 0.01, oque="fixar a caneca")
            b.reg("fixa", *par("g12"), ponto_caneca["p"], "copo")
            fecha("g12")
        passo(12, "fixar a caneca", p12)

        # 13, 14, 15 — Y, Z e X no meio ------------------------------------------
        def alinha_passo(n, eixo, qual, gesto, rotulo):
            a = b.cap(f"g{n:02}_antes")
            ponto = M.alinha(b, eixo, qual, captura=f"_alinha{n}")
            d = b.cap(f"g{n:02}_depois", parar=False)
            b.mudou(a, d, 0.05, oque=f"alinhar {eixo}")
            b.reg(gesto, *par(f"g{n:02}"), ponto, rotulo)
            fecha(f"g{n:02}")

        passo(13, "centro em Y", lambda: alinha_passo(13, "y", "centro", "alinha_y", "bolinha do meio esquerda"))
        passo(14, "centro em Z", lambda: alinha_passo(14, "z", "centro", "alinha_z", "bolinha do meio direita"))
        passo(15, "centro em X", lambda: alinha_passo(15, "x", "centro", "alinha_x", "bolinha do meio embaixo"))

        # 16 — Esc + Shift+clique na caneca: só o ANEL fica selecionado ---------------
        def p16():
            pg.keyboard.press("Escape"); pg.wait_for_timeout(900)
            a = b.cap("g16_antes")
            pg.keyboard.down("Shift")
            b.clica(ponto_caneca["p"], 1000)
            pg.keyboard.up("Shift"); pg.wait_for_timeout(500)
            d = b.cap("g16_depois")
            b.mudou(a, d, 0.05, oque="tirar a caneca da seleção")
            b.reg("so_o_anel", *par("g16"), ponto_caneca["p"], "copo",
                  tipo="tecla", teclas=["Shift", "clique"])
            fecha("g16")
        passo(16, "Shift + clique na caneca", p16)

        # 17 — empurrar o anel para a esquerda ------------------------------------------
        def p17():
            a = b.cap("g17_antes")
            for _ in range(EMPURRA_DEZ):
                pg.keyboard.press("Shift+ArrowLeft"); pg.wait_for_timeout(300)
            for _ in range(EMPURRA_UM):
                pg.keyboard.press("ArrowLeft"); pg.wait_for_timeout(300)
            pg.wait_for_timeout(900)
            d = b.cap("g17_depois")
            b.mudou(a, d, 0.1, oque="empurrar o anel")
            b.reg("empurra", *par("g17"), ponto_caneca["p"], "Shift + seta para a esquerda",
                  tipo="tecla", teclas=["Shift", "←"])
            fecha("g17")
        passo(17, "empurrar o anel (Shift + ←)", p17)

        # 18 — Ctrl + A de novo -------------------------------------------------------
        def p18():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g18_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap("g18_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg("seleciona3", *par("g18"), (600, 520), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            fecha("g18")
        passo(18, "Ctrl + A", p18)

        # 19 — Grupo de união ----------------------------------------------------------
        antes_largura = {}

        def p19():
            antes_largura["w"] = bbox_laranja(b.cap("_antes_grupo"))
            a = b.cap("g19_antes")
            alvo = b.acha_por_dica("Grupo de união")
            b.clica(alvo, 2800)
            d = b.cap("g19_depois")
            b.mudou(a, d, 0.2, oque="agrupar")
            b.reg("uniao", *par("g19"), alvo, "Grupo de união")
            fecha("g19")
        passo(19, "Grupo de união", p19)

        # 20 — conferir de frente: a alça está colada na caneca? -----------------------
        def p20():
            b.clica((250, 790), 700)
            a = b.cap("g20_antes")
            alvo = (63, 180)                      # a face FRONTAL do cubo de vistas
            b.clica(alvo, 2200)
            d = b.cap("g20_depois")
            b.mudou(a, d, 1.0, oque="vista de frente")
            b.reg("vista_frente", *par("g20"), alvo, "cubo FRONTAL")
            prova_da_alca(b, d)
            fecha("g20")
        passo(20, "olhar de frente (a alça)", p20)

        # 21 — dar nome ----------------------------------------------------------------
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


def prova_da_alca(b, captura):
    """Vista de frente: tem uma ALÇA colada na caneca?

    Na vista de frente a caneca é um retângulo e a alça um anel que sai da
    lateral direita. Mede a largura da peça laranja na altura do MEIO e a
    largura no TOPO: com alça, o meio é bem mais largo que o topo; sem alça
    (o anel dentro da caneca, ou solto), os dois são iguais. Controle: os dois
    têm de existir (a peça não sumiu)."""
    im = Image.open(captura).convert("RGB")
    caixa = bbox_laranja(captura)
    x0, y0, x1, y1 = caixa

    def largura_na_linha(y):
        xs = [x for x in range(60, 880)
              if (lambda p: p[0] > 150 and 70 < p[1] < 190 and p[2] < 110)(im.getpixel((x, y)))]
        return (max(xs) - min(xs) + 1) if xs else 0

    topo = largura_na_linha(y0 + 12)
    meio = max(largura_na_linha(y) for y in range(y0 + (y1 - y0) // 3, y0 + (y1 - y0) * 2 // 3, 4))
    print(f"     vista de frente: largura no topo {topo} px, no meio {meio} px", flush=True)
    if topo < 20:
        raise Falhou("não achei a caneca na vista de frente")
    if meio < topo + 25:
        raise Falhou(f"não há alça saindo da caneca: topo {topo} px, meio {meio} px")
    return topo, meio


if __name__ == "__main__":
    principal()
