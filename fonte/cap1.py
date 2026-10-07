#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 1 — captura as telas da plaquinha com o nome.

Roda o editor do Tinkercad em headless (não ocupa a tela de ninguém), segue os
passos na ordem e fotografa antes e depois de cada um. Produz:

    fonte/aula1/*.jpg      as capturas em tamanho cheio
    fonte/aula1/alvos.json o ponto, o tipo e o rótulo de cada gesto

A numeração dos arquivos É a numeração dos passos da aula. Os passos 1 e 2
(abrir o Tinkercad e criar o projeto) vivem no cap0.py, que fotografa o painel.

Uso:  TINK_PERFIL=... ./pwenv/bin/python fonte/cap1.py
      TINK_SABOTA=1 ...  pula a descida do furo, para provar o guarda do 17
"""
import os, sys, time
from playwright.sync_api import sync_playwright

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou

PASTA  = os.path.join(AQUI, "aula1")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
PROJ   = os.environ.get("TINK_PROJ", "https://www.tinkercad.com/things/hnHuvfChKyx/edit")
NOME   = "ANA"          # o nome de exemplo que vai na plaquinha
SORTEADO = "Shiny Jaban-Turing"      # o nome que o Tinkercad tinha sorteado
BATIZADO = "Chaveiro da ANA"         # o nome que o passo 21 dá ao projeto
CASINHA = (34, 240)     # o botão de vista inicial, na barra da esquerda


def espera_editor(pg):
    for _ in range(45):
        if pg.evaluate("document.querySelectorAll('canvas').length") > 0:
            break
        pg.wait_for_timeout(1000)
    else:
        raise Falhou("o editor não abriu: nenhum canvas em 45 s")
    pg.wait_for_timeout(9000)


def limpa(b):
    """Plano vazio e câmera na vista inicial.

    ⛔ A casinha é apertada AQUI, calada, e não como passo da aula. O projeto
    reabre com a câmera onde o último uso a deixou, e TODAS as medidas de tela
    deste roteiro (onde está a plaquinha, onde cai o furo) só valem na vista
    inicial. O passo que ENSINA a girar a câmera fica no fim, quando já há
    peça para girar — plano vazio girando não ensina nada.
    """
    b.pg.mouse.click(600, 790)
    b.pg.wait_for_timeout(400)
    b.tecla("Meta+A", 900)
    b.tecla("Delete", 1600)
    b.pg.mouse.click(*CASINHA)
    b.pg.wait_for_timeout(1800)
    # ⛔ Devolve ao projeto o nome SORTEADO antes de começar. Sem isto, a partir
    #    da segunda execução o editor já abre batizado, o passo que ensina a
    #    renomear não muda nada na tela e o clipe vira animação de nada — e o
    #    nome que a criança vê nas 20 primeiras figuras tem de ser o sorteado,
    #    que é o que ela realmente encontra.
    b.renomeia(SORTEADO)


def principal():
    os.makedirs(PASTA, exist_ok=True)
    with sync_playwright() as p:
        ctx = p.chromium.launch_persistent_context(
            PERFIL, headless=True, viewport={"width": 1440, "height": 900})
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
        espera_editor(pg)
        limpa(b)
        # ⛔ A marca de nascimento desta execução. Todas as execuções usam o
        #    MESMO projeto e gravam com os MESMOS nomes de arquivo, então uma
        #    figura que sobrou de uma execução anterior não chama atenção de
        #    ninguém. O guarda compara a data de cada quadro com este arquivo.
        with open(os.path.join(PASTA, "projeto.txt"), "w") as f:
            f.write(f"{PROJ}\n{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("plano limpo, vista inicial. começando os passos:\n", flush=True)

        # 3 — a tela do editor ---------------------------------------------
        def p3():
            b.cap("p03_tela"); b.jpg("p03_tela")
        passo(3, "a tela do editor", p3)

        # 4 — arrastar a Caixa ---------------------------------------------
        def p4():
            a = b.cap("g04_antes")
            cx = b.acha("Caixa", 30)
            b.arrasta(cx, (600, 520))
            d = b.cap("g04_depois")
            b.mudou(a, d, 0.8, oque="soltar a Caixa no plano")
            b.reg("caixa", "g04_antes.jpg", "g04_depois.jpg", cx, "Caixa",
                  ate=(600, 520))
            b.jpg("g04_antes"); b.jpg("g04_depois")
        passo(4, "arrastar a Caixa", p4)

        # 5 — o painel que abriu -------------------------------------------
        def p5():
            b.cap("p05_painel"); b.jpg("p05_painel")
        passo(5, "o painel de propriedades", p5)

        # 6, 7, 8 — as três medidas -----------------------------------------
        #     ⛔ MEDIDO, não suposto: na vista inicial do Tinkercad quem corre
        #        na horizontal da tela é a LARGURA, e a forma Texto escreve
        #        nessa mesma direção. Pôr o 90 em Comprimento deixa a plaquinha
        #        apontando para longe e o nome atravessado nela. Por isso o
        #        número grande vai em Largura. (Vira caixa SOS na aula.)
        MEDIDAS = (("Comprimento", 30), ("Largura", 90), ("Altura", 4))
        for n, (rot, val) in zip((6, 7, 8), MEDIDAS):
            def pN(rot=rot, val=val, n=n):
                a = b.cap(f"g{n:02}_antes")
                alvo = b.escreve_campo(rot, val)
                d = b.cap(f"g{n:02}_depois")
                b.mudou(a, d, 0.25, oque=f"{rot} = {val}")
                b.reg(rot.lower(), f"g{n:02}_antes.jpg", f"g{n:02}_depois.jpg",
                      alvo, rot)
                b.jpg(f"g{n:02}_antes"); b.jpg(f"g{n:02}_depois")
            passo(n, f"{rot} = {val} mm", pN)

        # a plaquinha, medida na tela ANTES de soltar coisa em cima dela
        placa = {}

        def mede_placa(de):
            x0, y0, x1, y1 = b.bbox_vermelho(os.path.join(PASTA, de))
            placa.update(x0=x0, y0=y0, x1=x1, y1=y1,
                         larg=x1-x0, alt=y1-y0, cx=(x0+x1)/2, cy=(y0+y1)/2,
                         furo=(x0 + (x1-x0)*0.09, y0 + (y1-y0)*0.42))
            print(f"     plaquinha na tela: {int(x0)},{int(y0)} → {int(x1)},{int(y1)}"
                  f"  ({int(x1-x0)}×{int(y1-y0)} px)", flush=True)

        # 9 — a forma Texto -------------------------------------------------
        def p9():
            mede_placa("g08_depois.jpg")
            a = b.cap("g09_antes")
            tx = b.acha("Texto", 30)
            # ⛔ O ponto de soltura é MEDIDO na plaquinha, não combinado de
            #    cabeça: ela muda de tamanho e de lugar a cada medida digitada.
            #    A versão por coordenada fixa largou o nome fora da peça.
            b.arrasta(tx, (placa["cx"], placa["cy"]))
            d = b.cap("g09_depois")
            b.mudou(a, d, 0.6, oque="soltar a forma Texto")
            b.reg("texto", "g09_antes.jpg", "g09_depois.jpg", tx, "Texto",
                  ate=(placa["cx"], placa["cy"]))
            b.jpg("g09_antes"); b.jpg("g09_depois")
        passo(9, "arrastar a forma Texto", p9)

        # 10 — escrever o nome ----------------------------------------------
        def p10():
            a = b.cap("g10_antes")
            # ⛔ O rótulo do campo é "Text", em INGLÊS, num painel todo em
            #    português. Procurar por "Texto" acha o título do painel (o
            #    nome da forma) e não o campo. A criança cai na mesma pegadinha.
            loc, alvo = b.acha_campo("Text")
            loc.fill(NOME)
            loc.press("Tab"); pg.wait_for_timeout(2500)
            if not loc.input_value().startswith(NOME):
                raise Falhou(f"o campo Text ficou {loc.input_value()!r}")
            d = b.cap("g10_depois")
            b.mudou(a, d, 0.3, oque="escrever o nome")
            b.reg("nome", "g10_antes.jpg", "g10_depois.jpg", alvo, "Text")
            b.jpg("g10_antes"); b.jpg("g10_depois")
        passo(10, f"escrever {NOME}", p10)

        # 11 — a forma que vai virar buraco ---------------------------------
        #     ⛔ Não use o Cilindro: o painel dele só tem Lados, Chanfro e
        #        Segmentos — não tem Comprimento, Largura nem Altura. Quem
        #        traz os três campos é a Caixa. E isso vira conteúdo: o
        #        orifício não precisa ser redondo, qualquer forma serve.
        def p11():
            a = b.cap("g11_antes")
            cx = b.acha("Caixa", 30)
            b.arrasta(cx, placa["furo"])   # na ponta esquerda, pela medida
            d = b.cap("g11_depois")
            b.mudou(a, d, 0.5, oque="soltar a segunda Caixa")
            b.reg("caixa2", "g11_antes.jpg", "g11_depois.jpg", cx, "Caixa",
                  ate=placa["furo"])
            b.jpg("g11_antes"); b.jpg("g11_depois")
        passo(11, "arrastar a segunda Caixa", p11)

        # 12 — encolher a segunda caixa -------------------------------------
        def p12():
            a = b.cap("g12_antes")
            b.escreve_campo("Comprimento", 8)
            alvo = b.escreve_campo("Largura", 8)
            d = b.cap("g12_depois")
            b.mudou(a, d, 0.25, oque="encolher a caixinha")
            b.reg("encolhe", "g12_antes.jpg", "g12_depois.jpg", alvo, "Largura")
            b.jpg("g12_antes"); b.jpg("g12_depois")
        passo(12, "encolher a caixinha para 8 mm", p12)

        # 13 — virar Orifício -----------------------------------------------
        def p13():
            a = b.cap("g13_antes")
            # o rótulo tem ~18 px de altura: filtro de 20 o descartava
            alvo = b.acha("Orifício", 8)
            b.clica(alvo, 2000)
            d = b.cap("g13_depois")
            b.mudou(a, d, 0.15, oque="virar Orifício")
            b.reg("orificio", "g13_antes.jpg", "g13_depois.jpg", alvo, "Orifício")
            b.jpg("g13_antes"); b.jpg("g13_depois")
        passo(13, "clicar em Orifício", p13)

        # 14 — fazer o furo DESCER ------------------------------------------
        #     ⛔ Passo que ninguém adivinha: ao soltar a caixinha em cima da
        #        plaquinha, o Tinkercad criou um plano de trabalho na face de
        #        cima (o quadrado verde) e a caixinha nasceu em z = 4 mm — ou
        #        seja, POUSADA sobre a peça, sem entrar nela. Agrupar assim não
        #        fura nada. Ctrl + ↓ desce 1 mm por toque; 6 toques atravessam
        #        a plaquinha de 4 mm com folga. Medido, não suposto.
        def p14():
            a = b.cap("g14_antes")
            # TINK_SABOTA=1 pula a descida — é a sabotagem que prova que o
            # guarda do passo 17 enxerga de verdade. Fica atrás de bandeira
            # para ser repetível, não um remendo de uma vez só.
            quantos = 0 if os.environ.get("TINK_SABOTA") else 6
            for _ in range(quantos):
                pg.keyboard.press("Control+ArrowDown")
                pg.wait_for_timeout(200)
            pg.wait_for_timeout(900)
            d = b.cap("g14_depois")
            if quantos:
                b.mudou(a, d, 0.1, oque="descer o furo")
            b.reg("desce", "g14_antes.jpg", "g14_depois.jpg",
                  placa["furo"], "Ctrl + seta para baixo",
                  tipo="tecla", teclas=["Ctrl", "↓"])
            b.jpg("g14_antes"); b.jpg("g14_depois")
        passo(14, "descer o furo 6 mm (Ctrl + ↓)", p14)

        # 15 — selecionar tudo ----------------------------------------------
        def p15():
            a = b.cap("g15_antes")
            b.tecla("Meta+A", 1500)
            d = b.cap("g15_depois")
            b.mudou(a, d, 0.1, oque="selecionar tudo")
            b.reg("seleciona", "g15_antes.jpg", "g15_depois.jpg",
                  (placa["cx"], placa["cy"]), "Ctrl + A",
                  tipo="tecla", teclas=["Ctrl", "A"])
            b.jpg("g15_antes"); b.jpg("g15_depois")
        passo(15, "selecionar tudo", p15)

        # 16 — Grupo de união (NÃO «Grupo do conjunto») ---------------------
        def p16():
            a = b.cap("g16_antes")
            alvo = b.acha_por_dica("Grupo de união")
            b.clica(alvo, 2800)
            d = b.cap("g16_depois")
            b.mudou(a, d, 0.5, oque="agrupar em união")
            b.reg("uniao", "g16_antes.jpg", "g16_depois.jpg", alvo, "Grupo de união")
            b.jpg("g16_antes"); b.jpg("g16_depois")
        passo(16, "Grupo de união", p16)

        # 17 — a peça pronta, e a prova de que o furo vazou -----------------
        def p17():
            b.clica((250, 790), 1400)      # clica no vazio: tira a moldura
            cam = b.cap("p17_pronta")
            dentro, fora = b.furo_vazado(cam, placa["furo"])
            print(f"     furo aberto: {dentro} px de chão à vista, "
                  f"controles {fora}", flush=True)
            b.jpg("p17_pronta")
        passo(17, "a peça pronta (com furo aberto)", p17)

        # 18 — girar a câmera, AGORA que há peça para girar ------------------
        def p18():
            a = b.cap("g18_antes")
            de, ate = (600, 700), (600 + 12*14, 700 - 12*5)
            pg.mouse.move(*de)
            pg.mouse.down(button="right"); pg.wait_for_timeout(300)
            for i in range(1, 13):
                pg.mouse.move(de[0] + i*14, de[1] - i*5); pg.wait_for_timeout(60)
            pg.mouse.up(button="right"); pg.wait_for_timeout(1600)
            d = b.cap("g18_depois")
            b.mudou(a, d, 1.0, oque="girar a câmera")
            # ⛔ botão DIREITO: desenhado como arrasto comum, a criança segura
            #    o esquerdo e arrasta a PEÇA em vez de girar a câmera.
            b.reg("girar", "g18_antes.jpg", "g18_depois.jpg", de,
                  "plano de trabalho", ate=ate, botao="dir")
            b.jpg("g18_antes"); b.jpg("g18_depois")
        passo(18, "girar a câmera (botão direito)", p18)

        # 19 — voltar à vista inicial ---------------------------------------
        def p19():
            a = b.cap("g19_antes")
            b.clica(CASINHA, 1800)
            d = b.cap("g19_depois")
            b.mudou(a, d, 0.8, oque="voltar à vista inicial")
            b.reg("vista_inicial", "g19_antes.jpg", "g19_depois.jpg",
                  CASINHA, "casinha")
            b.jpg("g19_antes"); b.jpg("g19_depois")
        passo(19, "voltar à vista inicial", p19)

        # 20 — dar nome ao projeto ------------------------------------------
        def p20():
            a = b.cap("g20_antes")
            alvo = b.renomeia(BATIZADO)
            d = b.cap("g20_depois")
            b.mudou(a, d, 0.02, box=(0, 0, 500, 50), oque="trocar o nome")
            b.reg("batiza", "g20_antes.jpg", "g20_depois.jpg", alvo,
                  "nome do projeto")
            b.jpg("g20_antes"); b.jpg("g20_depois")
        passo(20, f"dar nome ao projeto ({BATIZADO})", p20)

        b.grava_alvos()
        print(f"\nalvos.json com {len(b.alvos)} gestos", flush=True)
        print(f"capturas: {len([f for f in os.listdir(PASTA) if f.endswith('.jpg')])} jpg",
              flush=True)
        ctx.close()


if __name__ == "__main__":
    principal()
