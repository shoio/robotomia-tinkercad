#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 2 — Porta-lápis: esvaziar um cilindro por dentro.

O truque da Aula 1 (uma forma que vira BURACO) em escala maior: um cilindro
alto e, dentro dele, um cilindro menor que vira Orifício e começa 5 mm acima
do chão — sobra o fundo. E as duas ferramentas novas que toda peça redonda
pede: os NÚMEROS DE TAMANHO das alças (o cilindro não tem campo de medida no
painel) e o ALINHAR (centrar um cilindro dentro do outro).

Uso:  TINK_PERFIL=... ./pwenv/bin/python fonte/cap2.py
      TINK_SABOTA=1 ...  pula a subida do furo (prova do guarda do fundo)
"""
import os, shutil, sys, time
from playwright.sync_api import sync_playwright

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou
import cap1
import mecanica as M

PASTA  = os.path.join(AQUI, "aula2")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
PROJ   = cap1.PROJ
SORTEADO = cap1.SORTEADO
BATIZADO = "Porta-lápis da ANA"

D_CORPO, H_CORPO = 50, 70          # o cilindro de fora: 50 mm de diâmetro, 70 de altura
D_FURO,  H_FURO  = 42, 70          # o furo: 4 mm de parede
FUNDO = 5                          # 5 mm de fundo (o furo sobe isto)
SOLTAR_1 = (600, 540)              # onde cai o corpo
SOLTAR_2 = (800, 700)              # o furo nasce ao lado, no plano (em cima do corpo ele nasceria na altura dele)


def copia_dos_passos_1_a_3():
    """As figuras do site (passos 1–3) são as da Aula 1: o painel do dono tem
    nome real e capas de projetos particulares (PADRAO.md §6), e fotografá-lo
    de novo seria arriscar o vazamento que a Aula 1 já provou que não há."""
    os.makedirs(PASTA, exist_ok=True)
    de = os.path.join(AQUI, "aula1")
    for nome in sorted(os.listdir(de)):
        if nome.startswith("d0") or nome in ("alvos0.json", "painel.txt"):
            shutil.copy2(os.path.join(de, nome), os.path.join(PASTA, nome))
    os.makedirs(os.path.join(PASTA, "gifs"), exist_ok=True)
    for nome in ("criar.gif", "projeto3d_ponto.gif"):
        origem = os.path.join(de, "gifs", nome)
        if os.path.exists(origem):
            shutil.copy2(origem, os.path.join(PASTA, "gifs", nome))


def principal():
    copia_dos_passos_1_a_3()
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

        print(f"abrindo {PROJ}", flush=True)
        pg.goto(PROJ, wait_until="domcontentloaded", timeout=60000)
        cap1.espera_editor(pg)
        cap1.limpa(b)
        with open(os.path.join(PASTA, "projeto.txt"), "w") as f:
            f.write(f"{PROJ}\n{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("plano limpo, vista inicial. começando os passos:\n", flush=True)

        def par(nome):
            """antes/depois do gesto, com os nomes que o reg espera."""
            return f"{nome}_antes.jpg", f"{nome}_depois.jpg"

        def fecha(nome):
            b.jpg(f"{nome}_antes"); b.jpg(f"{nome}_depois")

        # 4 — o primeiro cilindro ------------------------------------------
        def p4():
            a = b.cap("g04_antes")
            cil = b.acha("Cilindro", 30)
            b.arrasta(cil, SOLTAR_1)
            d = b.cap("g04_depois")
            b.mudou(a, d, 0.8, oque="soltar o Cilindro")
            b.reg("cilindro", *par("g04"), cil, "Cilindro", ate=SOLTAR_1)
            fecha("g04")
        passo(4, "arrastar o Cilindro", p4)

        # 6 — a alça do canto: aparecem DOIS números ---------------------------
        alcas = {}

        def p6():
            alcas.update(M.alcas_agora(b, "_alcas6"))
            a = b.cap("g06_antes")
            alvo = alcas["esq_tras"]
            b.clica(alvo, 1000)
            rot = M.rotulos_de_medida(pg)
            if len(rot) != 2:
                raise Falhou(f"esperava 2 números de tamanho e vi {rot}")
            d = b.cap("g06_depois", parar=False)
            b.mudou(a, d, 0.1, oque="clicar na alça do canto")
            b.reg("alca", *par("g06"), alvo, "alça do canto")
            fecha("g06")
        passo(6, "clicar na alça do canto", p6)

        def digita_no_numero(qual, valor, gesto, rotulo, n):
            a = b.cap(f"g{n:02}_antes", parar=False)
            rot = M.rotulos_de_medida(pg)
            if qual == "largura":
                alvo = min(rot, key=lambda t: t[2])        # o de cima
            else:
                alvo = min(rot, key=lambda t: t[1])        # o da esquerda
            M.digita_no_rotulo(b, alvo[1], alvo[2], valor)
            d = b.cap(f"g{n:02}_depois", parar=False)
            b.mudou(a, d, 0.05, oque=f"{qual} = {valor}")
            b.reg(gesto, *par(f"g{n:02}"), (alvo[1], alvo[2]), rotulo)
            fecha(f"g{n:02}")

        # 7, 8 — largura e comprimento do corpo ----------------------------------
        passo(7, f"largura = {D_CORPO}",
              lambda: digita_no_numero("largura", D_CORPO, "largura", "número de cima", 7))
        passo(8, f"comprimento = {D_CORPO}",
              lambda: digita_no_numero("comprimento", D_CORPO, "comprimento", "número da esquerda", 8))

        # 9 — a altura: alça de cima ---------------------------------------------
        def p9():
            h = M.alcas_agora(b, "_alcas9")
            a = b.cap("g09_antes")
            alvo = h["topo"]
            b.clica(alvo, 1000)
            rot = M.rotulos_de_medida(pg)
            if len(rot) != 1:
                raise Falhou(f"esperava 1 número de altura e vi {rot}")
            M.digita_no_rotulo(b, rot[0][1], rot[0][2], H_CORPO)
            d = b.cap("g09_depois")
            b.mudou(a, d, 0.8, oque=f"altura = {H_CORPO}")
            b.reg("altura", *par("g09"), alvo, "alça de cima")
            fecha("g09")
        passo(9, f"altura = {H_CORPO}", p9)

        # 10 — o segundo cilindro, AO LADO ------------------------------------
        def p10():
            b.clica((250, 790), 500)                 # solta a seleção
            a = b.cap("g10_antes")
            cil = b.acha("Cilindro", 30)
            b.arrasta(cil, SOLTAR_2)
            d = b.cap("g10_depois")
            b.mudou(a, d, 0.5, oque="soltar o segundo Cilindro")
            b.reg("cilindro2", *par("g10"), cil, "Cilindro", ate=SOLTAR_2)
            fecha("g10")
        passo(10, "arrastar o segundo Cilindro", p10)

        # 11 — virar Orifício ------------------------------------------------
        def p11():
            a = b.cap("g11_antes")
            alvo = b.acha("Orifício", 8)
            b.clica(alvo, 1800)
            d = b.cap("g11_depois")
            b.mudou(a, d, 0.1, oque="virar Orifício")
            b.reg("orificio", *par("g11"), alvo, "Orifício")
            fecha("g11")
        passo(11, "virar Orifício", p11)

        # 12 — os dois números do furo (42 e 42) ---------------------------------
        def p12():
            h = M.alcas_agora(b, "_alcas12")
            a = b.cap("g12_antes")
            alvo = h["esq_tras"]
            b.clica(alvo, 900)
            rot = M.rotulos_de_medida(pg)
            if len(rot) != 2:
                raise Falhou(f"esperava 2 números de tamanho e vi {rot}")
            comp = min(rot, key=lambda t: t[1])
            M.digita_no_rotulo(b, comp[1], comp[2], D_FURO)
            rot = M.rotulos_de_medida(pg)
            larg = min(rot, key=lambda t: t[2])
            M.digita_no_rotulo(b, larg[1], larg[2], D_FURO)
            d = b.cap("g12_depois")
            b.mudou(a, d, 0.3, oque="encolher o furo")
            b.reg("furo_planta", *par("g12"), alvo, "alça do canto")
            fecha("g12")
        passo(12, f"furo {D_FURO} × {D_FURO}", p12)

        # 13 — a altura do furo --------------------------------------------------
        def p13():
            h = M.alcas_agora(b, "_alcas13")
            a = b.cap("g13_antes")
            alvo = h["topo"]
            b.clica(alvo, 900)
            rot = M.rotulos_de_medida(pg)
            if len(rot) != 1:
                raise Falhou(f"esperava 1 número de altura e vi {rot}")
            M.digita_no_rotulo(b, rot[0][1], rot[0][2], H_FURO)
            d = b.cap("g13_depois")
            b.mudou(a, d, 0.5, oque=f"altura do furo = {H_FURO}")
            b.reg("furo_altura", *par("g13"), alvo, "alça de cima")
            fecha("g13")
        passo(13, f"altura do furo = {H_FURO}", p13)

        # 14 — o furo SOBE 5 mm (Ctrl + ↑) ----------------------------------------
        #     ⛔ O furo nasce no chão, na mesma altura do corpo: agrupado assim
        #        ele ATRAVESSARIA o fundo e o porta-lápis viraria um tubo. Sobe
        #        5 mm e sobra um fundo de 5 mm — o mesmo Ctrl + seta da Aula 1.
        def p14():
            a = b.cap("g14_antes")
            quantos = 0 if os.environ.get("TINK_SABOTA") else FUNDO
            for _ in range(quantos):
                pg.keyboard.press("Control+ArrowUp")
                pg.wait_for_timeout(250)
            pg.wait_for_timeout(900)
            d = b.cap("g14_depois")
            if quantos:
                b.mudou(a, d, 0.1, oque="subir o furo")
            b.reg("sobe", *par("g14"), (pg.viewport_size["width"] // 2 - 60, 520),
                  "Ctrl + seta para cima", tipo="tecla", teclas=["Ctrl", "↑"])
            fecha("g14")
        passo(14, f"subir o furo {FUNDO} mm (Ctrl + ↑)", p14)

        # 15 — selecionar tudo ----------------------------------------------------
        def p15():
            a = b.cap("g15_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap("g15_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg("seleciona", *par("g15"), (600, 520), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            fecha("g15")
        passo(15, "selecionar tudo", p15)

        # 16 — o botão Alinhar -----------------------------------------------------
        def p16():
            a = b.cap("g16_antes")
            alvo = b.acha_por_dica("Alinhar")
            b.clica(alvo, 1500)
            d = b.cap("g16_depois")
            b.mudou(a, d, 0.3, oque="abrir o Alinhar")
            b.reg("alinhar", *par("g16"), alvo, "Alinhar")
            fecha("g16")
        passo(16, "abrir o Alinhar", p16)

        # 17, 18 — centro em X e em Y --------------------------------------------
        def alinha_passo(n, eixo, qual, gesto, rotulo):
            a = b.cap(f"g{n:02}_antes")
            ponto = M.alinha(b, eixo, qual, captura=f"_alinha{n}")
            d = b.cap(f"g{n:02}_depois", parar=False)
            b.mudou(a, d, 0.3, oque=f"alinhar {eixo}")
            b.reg(gesto, *par(f"g{n:02}"), ponto, rotulo)
            fecha(f"g{n:02}")

        passo(17, "centro em X", lambda: alinha_passo(17, "x", "centro", "alinha_x", "bolinha do meio embaixo"))
        passo(18, "centro em Y", lambda: alinha_passo(18, "y", "centro", "alinha_y", "bolinha do meio esquerda"))

        # 19 — Grupo de união ------------------------------------------------------
        def p19():
            # Esc sai do Alinhar MANTENDO as duas formas selecionadas. Sem ele
            # o botão de agrupar não responde (0 px mudados) — e clicar no
            # vazio solta a seleção e obriga a refazer o Ctrl + A.
            pg.keyboard.press("Escape"); pg.wait_for_timeout(900)
            a = b.cap("g19_antes")
            alvo = b.acha_por_dica("Grupo de união")
            b.clica(alvo, 2800)
            d = b.cap("g19_depois")
            b.mudou(a, d, 0.3, oque="agrupar")
            b.reg("uniao", *par("g19"), alvo, "Grupo de união")
            fecha("g19")
        passo(19, "Grupo de união", p19)

        # 20 — olhar de cima: o fundo ficou? --------------------------------------
        def p20():
            b.clica((250, 790), 900)
            a = b.cap("g20_antes")
            alvo = (63, 139)                       # a face SUPERIOR do cubo de vistas
            b.clica(alvo, 2200)
            d = b.cap("g20_depois")
            b.mudou(a, d, 1.0, oque="vista de cima")
            b.reg("vista_cima", *par("g20"), alvo, "cubo SUPERIOR")
            dentro, controle = prova_do_fundo(b, d)
            print(f"     fundo: {dentro} px de peça dentro do furo; plano claro visto ao lado: {controle}",
                  flush=True)
            fecha("g20")
        passo(20, "olhar de cima (o fundo ficou)", p20)

        # 21 — dar nome ------------------------------------------------------------
        def p21():
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


def prova_do_fundo(b, captura):
    """Vista de cima: o furo tem FUNDO?

    Dentro do furo, olhando de cima, se há fundo se vê a peça (laranja); se o
    furo atravessasse, se veria o plano de trabalho (quase branco, de cima). Mede os dois:
    a janela no meio do furo tem de ser laranja, e uma janela só de plano,
    ao lado da peça, tem de ser azul-claro (controle negativo — senão o guarda
    aprovaria uma peça que sumiu)."""
    from PIL import Image
    im = Image.open(captura).convert("RGB")
    # a peça: onde há laranja
    xs, ys = [], []
    for y in range(120, 880, 3):
        for x in range(100, 880, 3):
            r, g, bl = im.getpixel((x, y))
            if r > 200 and 90 < g < 170 and bl < 90:
                xs.append(x); ys.append(y)
    if len(xs) < 200:
        raise Falhou("não achei a peça laranja na vista de cima")
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2

    def laranja(x, y, r=14):
        n = 0
        for yy in range(int(y) - r, int(y) + r + 1, 2):
            for xx in range(int(x) - r, int(x) + r + 1, 2):
                R, G, B = im.getpixel((xx, yy))
                if R > 200 and 90 < G < 170 and B < 90:
                    n += 1
        return n

    def azul(x, y, r=14):
        n = 0
        for yy in range(int(y) - r, int(y) + r + 1, 2):
            for xx in range(int(x) - r, int(x) + r + 1, 2):
                R, G, B = im.getpixel((xx, yy))
                if min(R, G, B) > 215:          # o plano visto de cima é quase branco
                    n += 1
        return n

    dentro = laranja(cx, cy)
    fora = azul(max(xs) + 70, cy)
    if fora < 20:
        raise Falhou(f"controle negativo falhou: o plano ao lado da peça devia ser claro e vi {fora}")
    if dentro < 20:
        raise Falhou(f"o fundo sumiu: no meio do furo há só {dentro} px de peça — "
                     "o furo subiu 5 mm antes de agrupar?")
    return dentro, fora


if __name__ == "__main__":
    principal()
