#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 4 — Casinha: uma Caixa, um Telhado e um furo de porta.

O que é novo: a forma TELHADO (sem campo de medida: o tamanho vai pelas alças),
SOLTAR uma forma em cima de outra (o telhado nasce na tampa da casa),
o ALINHAR usado duas vezes — o telhado centrado em cima da casa, e a porta
rente à parede da frente — e o SHIFT + clique para escolher só duas formas.

Uso:  ./pwenv/bin/python fonte/cap4.py
"""
import os, shutil, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou
import cap1
import mecanica as M

PASTA  = os.path.join(AQUI, "aula4")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
PROJ   = cap1.PROJ
BATIZADO = "Casinha da ANA"

CASA = dict(comprimento=50, largura=60, altura=40)       # 60 de largura (esq→dir), 50 de fundo
TELHADO = dict(largura=66, comprimento=56, altura=24)    # 3 mm de beiral em cada lado
PORTA = dict(comprimento=12, largura=16, altura=28)      # 12 de fundo: entra 12 mm na parede
SOLTAR_CASA = (600, 560)
SOLTAR_PORTA = (820, 720)


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

        print(f"abrindo {PROJ}", flush=True)
        pg.goto(PROJ, wait_until="domcontentloaded", timeout=60000)
        cap1.espera_editor(pg)
        cap1.limpa(b)
        with open(os.path.join(PASTA, "projeto.txt"), "w") as f:
            f.write(f"{PROJ}\n{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("plano limpo, vista inicial. começando os passos:\n", flush=True)

        casa = {}

        # 1 — o projeto novo, vazio (as figuras do site são as da Aula 1) ---------
        def p1():
            b.cap("p01_vazio"); b.jpg("p01_vazio")
        passo(1, "o projeto novo, vazio", p1)

        # 2 — a Caixa ------------------------------------------------------------
        def p2():
            a = b.cap("g02_antes")
            cx = b.acha("Caixa", 30)
            b.arrasta(cx, SOLTAR_CASA)
            d = b.cap("g02_depois")
            b.mudou(a, d, 0.8, oque="soltar a Caixa")
            b.reg("caixa", *par("g02"), cx, "Caixa", ate=SOLTAR_CASA)
            fecha("g02")
        passo(2, "arrastar a Caixa", p2)

        # 3 — 60 × 50 × 40: os três campos do painel ---------------------------------
        def p3():
            a = b.cap("g03_antes")
            b.escreve_campo("Comprimento", CASA["comprimento"])
            b.escreve_campo("Largura", CASA["largura"])
            alvo = b.escreve_campo("Altura", CASA["altura"])
            d = b.cap("g03_depois")
            b.mudou(a, d, 0.3, oque="medidas da casa")
            b.reg("medidas_casa", *par("g03"), alvo, "Altura")
            fecha("g03")
            h = M.alcas_agora(b, "_casa")
            casa["h"] = h
            casa["topo_centro"] = ((h["esq_tras"][0] + h["dir_tras"][0]) // 2, h["topo"][1])
            casa["ponto"] = ((h["esq_frente"][0] + h["dir_frente"][0]) // 2,
                             (h["esq_tras"][1] + h["esq_frente"][1]) // 2)
            print(f"     a casa: ponto de clique {casa['ponto']}, tampa em {casa['topo_centro']}", flush=True)
        passo(3, "60 × 50 × 40", p3)

        # 4 — o Telhado, solto em cima da casa -----------------------------------
        def p4():
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g04_antes")
            tel = b.acha("Telhado", 20)
            b.arrasta(tel, casa["topo_centro"])
            d = b.cap("g04_depois")
            b.mudou(a, d, 0.3, oque="soltar o Telhado")
            b.reg("telhado", *par("g04"), tel, "Telhado", ate=casa["topo_centro"])
            fecha("g04")
        passo(4, "arrastar o Telhado para a tampa", p4)

        # 5 — as medidas do telhado, pelas alças ------------------------------------
        def p5():
            h = M.alcas_agora(b, "_alcasT")
            a = b.cap("g05_antes")
            alvo = M.muda_planta(b, TELHADO["largura"], TELHADO["comprimento"], nome="_alcasT2")
            M.muda_altura(b, TELHADO["altura"], nome="_alcasT3")
            d = b.cap("g05_depois")
            b.mudou(a, d, 0.3, oque="medidas do telhado")
            b.reg("medidas_telhado", *par("g05"), alvo, "alça do canto")
            fecha("g05")
        passo(5, f"telhado {TELHADO['largura']} × {TELHADO['comprimento']} × {TELHADO['altura']}", p5)

        # 6 — Ctrl + A -----------------------------------------------------------
        def p6():
            a = b.cap("g06_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap("g06_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg("seleciona", *par("g06"), (600, 520), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            fecha("g06")
        passo(6, "Ctrl + A", p6)

        # 7 — Alinhar --------------------------------------------------------------
        def p7():
            a = b.cap("g07_antes")
            alvo = b.acha_por_dica("Alinhar")
            b.clica(alvo, 1500)
            d = b.cap("g07_depois")
            b.mudou(a, d, 0.3, oque="abrir o Alinhar")
            b.reg("alinhar", *par("g07"), alvo, "Alinhar")
            fecha("g07")
        passo(7, "abrir o Alinhar", p7)

        # 8 — fixar a casa ---------------------------------------------------------
        def p8():
            a = b.cap("g08_antes")
            b.clica(casa["ponto"], 1000)
            d = b.cap("g08_depois")
            b.mudou(a, d, 0.01, oque="fixar a casa")
            b.reg("fixa", *par("g08"), casa["ponto"], "casa")
            fecha("g08")
        passo(8, "fixar a casa", p8)

        def alinha_passo(n, eixo, qual, gesto, rotulo):
            a = b.cap(f"g{n:02}_antes")
            ponto = M.alinha(b, eixo, qual, captura=f"_alinha{n}")
            d = b.cap(f"g{n:02}_depois", parar=False)
            b.mudou(a, d, 0.05, oque=f"alinhar {eixo}")
            b.reg(gesto, *par(f"g{n:02}"), ponto, rotulo)
            fecha(f"g{n:02}")

        passo(9, "telhado: centro em X", lambda: alinha_passo(9, "x", "centro", "alinha_x", "bolinha do meio embaixo"))
        passo(10, "telhado: centro em Y", lambda: alinha_passo(10, "y", "centro", "alinha_y", "bolinha do meio esquerda"))

        # 11 — a Caixa da porta ----------------------------------------------------
        def p11():
            pg.keyboard.press("Escape"); pg.wait_for_timeout(700)
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            a = b.cap("g11_antes")
            cx = b.acha("Caixa", 30)
            b.arrasta(cx, SOLTAR_PORTA)
            d = b.cap("g11_depois")
            b.mudou(a, d, 0.3, oque="soltar a Caixa da porta")
            b.reg("caixa_porta", *par("g11"), cx, "Caixa", ate=SOLTAR_PORTA)
            fecha("g11")
        passo(11, "arrastar a Caixa da porta", p11)

        # 12 — Orifício ------------------------------------------------------------
        def p12():
            a = b.cap("g12_antes")
            alvo = b.acha("Orifício", 8)
            b.clica(alvo, 1800)
            d = b.cap("g12_depois")
            b.mudou(a, d, 0.1, oque="virar Orifício")
            b.reg("orificio", *par("g12"), alvo, "Orifício")
            fecha("g12")
        passo(12, "virar Orifício", p12)

        # 13 — as medidas da porta ----------------------------------------------------
        porta = {}

        def p13():
            a = b.cap("g13_antes")
            b.escreve_campo("Comprimento", PORTA["comprimento"])
            b.escreve_campo("Largura", PORTA["largura"])
            alvo = b.escreve_campo("Altura", PORTA["altura"])
            d = b.cap("g13_depois")
            b.mudou(a, d, 0.2, oque="medidas da porta")
            b.reg("medidas_porta", *par("g13"), alvo, "Altura")
            fecha("g13")
            hp = M.alcas_agora(b, "_porta")
            porta["ponto"] = ((hp["esq_frente"][0] + hp["dir_frente"][0]) // 2,
                              (hp["esq_tras"][1] + hp["esq_frente"][1]) // 2)
        passo(13, "porta 16 × 12 × 28", p13)

        # 14 — a casa e a porta, SÓ as duas -----------------------------------------
        def p14():
            a = b.cap("g14_antes")
            pg.mouse.click(*casa["ponto"]); pg.wait_for_timeout(800)
            pg.keyboard.down("Shift")
            pg.mouse.click(*porta["ponto"]); pg.keyboard.up("Shift"); pg.wait_for_timeout(900)
            d = b.cap("g14_depois")
            b.mudou(a, d, 0.05, oque="casa e porta selecionadas")
            b.reg("duas", *par("g14"), porta["ponto"], "porta",
                  tipo="tecla", teclas=["Shift", "clique"])
            fecha("g14")
        passo(14, "clicar na casa e Shift + clique na porta", p14)

        # 15 — Alinhar de novo ---------------------------------------------------
        def p15():
            a = b.cap("g15_antes")
            alvo = b.acha_por_dica("Alinhar")
            b.clica(alvo, 1500)
            d = b.cap("g15_depois")
            b.mudou(a, d, 0.3, oque="abrir o Alinhar")
            b.reg("alinhar2", *par("g15"), alvo, "Alinhar")
            fecha("g15")
        passo(15, "abrir o Alinhar", p15)

        # 16 — fixar a casa de novo -----------------------------------------------
        def p16():
            a = b.cap("g16_antes")
            b.clica(casa["ponto"], 1000)
            d = b.cap("g16_depois")
            b.mudou(a, d, 0.01, oque="fixar a casa")
            b.reg("fixa2", *par("g16"), casa["ponto"], "casa")
            fecha("g16")
        passo(16, "fixar a casa", p16)

        passo(17, "porta: centro em X", lambda: alinha_passo(17, "x", "centro", "alinha_x2", "bolinha do meio embaixo"))
        passo(18, "porta: rente à frente", lambda: alinha_passo(18, "y", "frente", "alinha_frente", "bolinha de baixo esquerda"))

        # 19 — Esc, Ctrl + A e Grupo de união ------------------------------------------
        def p19():
            pg.keyboard.press("Escape"); pg.wait_for_timeout(700)
            pg.mouse.click(250, 790); pg.wait_for_timeout(500)
            b.tecla("Meta+A", 900)
            a = b.cap("g19_antes")
            alvo = b.acha_por_dica("Grupo de união")
            b.clica(alvo, 2800)
            d = b.cap("g19_depois")
            b.mudou(a, d, 0.2, oque="agrupar")
            b.reg("uniao", *par("g19"), alvo, "Grupo de união")
            fecha("g19")
            b.clica((250, 790), 900)
            prova_da_porta(b, b.cap("_prova"), casa["h"])
        passo(19, "Grupo de união", p19)

        # 20 — a vista de frente ------------------------------------------------------
        def p20():
            a = b.cap("g20_antes")
            alvo = (63, 180)                      # a face FRONTAL do cubo de vistas
            b.clica(alvo, 2200)
            d = b.cap("g20_depois")
            b.mudou(a, d, 1.0, oque="vista de frente")
            b.reg("vista_frente", *par("g20"), alvo, "cubo FRONTAL")
            fecha("g20")
        passo(20, "olhar de frente", p20)

        # 21 — o nome -------------------------------------------------------------------
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


def prova_da_porta(b, captura, h):
    """A porta é um VÃO? Na vista inicial, dentro do furo se enxerga o chão (cinza-azulado) e,
    ao lado, a parede é vermelha.

    Controle negativo: a janela da parede, ao lado da porta, tem de ser VERMELHA
    (senão a peça sumiu ou a câmera é outra e a medida não vale nada)."""
    im = Image.open(captura).convert("RGB")
    cx = (h["esq_frente"][0] + h["dir_frente"][0]) // 2
    yf = (h["esq_frente"][1] + h["dir_frente"][1]) // 2

    def vermelho(x, y, r=12):
        n = 0
        for yy in range(y - r, y + r + 1, 2):
            for xx in range(x - r, x + r + 1, 2):
                R, G, B = im.getpixel((xx, yy))
                if R > 140 and G < 80 and B < 90:
                    n += 1
        return n

    dentro = vermelho(cx, yf - 14)
    parede = vermelho(cx - 95, yf - 14)
    print(f"     porta: {dentro} px vermelhos no vão; parede ao lado: {parede}", flush=True)
    if parede < 30:
        raise Falhou(f"controle negativo falhou: a parede ao lado da porta devia ser vermelha ({parede})")
    if dentro > 8:
        raise Falhou(f"a porta não abriu: ainda há {dentro} px de parede onde devia estar o vão")
    return dentro, parede


if __name__ == "__main__":
    principal()
