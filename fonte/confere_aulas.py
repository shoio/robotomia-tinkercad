#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O GUARDA do conteudo. Roda no comeco de todo build e PARA o build se
   reprovar.

   Cada regra nasceu de um defeito real do curso de Roblox ou desta noite de
   Flowlab — nenhuma e preferencia de estilo.
"""
import os, re, sys, glob, json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# frases que EMPURRAM o trabalho para outro lugar. O aluno le um passo por vez:
# um passo que delega parece completo na leitura continua e deixa a crianca
# parada na frente da tela.
DELEGA = ["como na aula passada", "igual ao de cima", "use a receita",
          "voce ja sabe", "do mesmo jeito de antes", "como antes"]


def confere(aulas=None):
    erros = []
    if aulas is None:
        import conteudo_a1
        aulas = [conteudo_a1.AULA]

    for A in aulas:
        n, slug = A["n"], A["slug"]

        def erra(m):
            erros.append(f"aula {n}: {m}")

        passos = A["passos"]
        if not (19 <= len(passos) <= 21):
            erra(f"tem {len(passos)} passos; o padrao e de 19 a 21 (o que cabe em 50 min)")

        # 1. numeracao sem buraco
        for i, p in enumerate(passos, 1):
            if p["n"] != i:
                erra(f"passo na posicao {i} esta numerado {p['n']}")

        for p in passos:
            onde = f"passo {p['n']}"

            # 2. toda foto existe
            img = p.get("img")
            if not img:
                erra(f"{onde}: sem foto")
            elif not os.path.exists(img):
                erra(f"{onde}: foto sumida {img}")

            # 3. todo clipe citado existe
            # o clipe pode ser um so ou uma LISTA de (rotulo, arquivo)
            import gera_curso as _G
            for _rot, cl in _G.clipes_do(p):
                if not os.path.exists(os.path.join(slug, "gifs", cl)):
                    erra(f"{onde}: clipe sumido {cl}")

            # 4. quadro verde e quadro laranja obrigatorios
            if not p.get("ck", "").strip():
                erra(f"{onde}: sem quadro verde (como saber que deu certo)")
            if not p.get("sos"):
                erra(f"{onde}: sem quadro laranja (o que fazer se travar)")
            for s in p.get("sos", []):
                if len(s) != 2 or not s[0].strip() or not s[1].strip():
                    erra(f"{onde}: socorro incompleto {s!r}")

            # 5. nenhum passo delega
            corpo = (p.get("corpo", "") + " " + p.get("ck", "")).lower()
            for frase in DELEGA:
                if frase in corpo:
                    erra(f"{onde}: delega com '{frase}' — repita o procedimento")

            # 6. passo que manda clicar tem de dizer ONDE.
            # So o CORPO conta: juntar o quadro verde aqui fazia a regra passar
            # por causa de um <span class=ui> que estava no quadro, nao na ordem.
            # ⛔ A LISTA DE PALAVRAS DE LUGAR É DESTE CURSO, não herdada.
            #    A do curso de Flowlab fala de casa, grade e bolinha de fio;
            #    aqui o aluno clica em painel, campo, bolinha, barra e plano.
            #    Copiar a lista do irmão deixaria «clique no do meio» passar por
            #    não ter nenhuma palavra que ela conhecesse — e reprovaria
            #    ordens perfeitamente claras.
            so_corpo = p.get("corpo", "").lower()
            if re.search(r"\bclique\b", so_corpo) and not re.search(
                    r"(em <span class=ui>|no <span class=ui>|na <span class=ui>|dentro|canto|"
                    r"coluna|fileira|linha|bolinha|figura|caixinha|ponta|quadradinho|metade|"
                    r"painel|campo|barra|plano|palheta|bot[ãa]o|espa[çc]o vazio|do meio|"
                    r"em cima d)", so_corpo):
                erra(f"{onde}: manda clicar e nao diz onde")

        # 6b. DUAS FOTOS IGUAIS, byte a byte, sao uma promessa quebrada.
        #
        # Nasceu da `p13_limite` da Aula 2: a pagina diz "escreva o limite da
        # camera" e mostrava a MESMA figura do passo anterior, porque a captura
        # fechava o painel antes de fotografar. A crianca compara a tela dela
        # com a figura e nao encontra o que o texto promete — e nenhuma trava
        # via isso, porque as duas fotos existiam e abriam.
        import hashlib
        vistas = {}
        for p in passos:
            img = p.get("img")
            if not img or not os.path.exists(img):
                continue
            h = hashlib.md5(open(img, "rb").read()).hexdigest()
            if h in vistas and vistas[h][1] != img:
                erra(f"passo {p['n']}: a foto {img} e IGUAL, byte a byte, a do "
                     f"passo {vistas[h][0]} ({vistas[h][1]})")
            vistas.setdefault(h, (p["n"], img))

        # 6c. FOTO PUBLICADA MAIS VELHA QUE A CAPTURA.
        #
        # `para_jpeg` apaga o PNG depois de converter, entao PNG e JPEG com o
        # mesmo nome, lado a lado, ja querem dizer que a conversao nao rodou
        # desde a ultima captura — e se o PNG for mais NOVO, o que a pagina
        # mostra e a captura ANTERIOR. Foi o que aconteceu com a Aula 2: as
        # fotos do ceu azul estavam na pasta em PNG e a pagina publicava os
        # JPEG do jogo branco, de duas horas antes. `git status` nao ajuda:
        # ele diz "modificado", nao "velho".
        for p in passos:
            img = p.get("img")
            if not img or not img.endswith(".jpg"):
                continue
            png = img[:-4] + ".png"
            if os.path.exists(png) and os.path.exists(img):
                if os.path.getmtime(png) > os.path.getmtime(img):
                    erra(f"passo {p['n']}: {img} e MAIS VELHO que a captura "
                         f"{png} — falta rodar para_jpeg.py {slug}")

        # 6d. MIDIA DE OUTRA EXECUCAO DA BANCADA.
        #
        # `aulaN/projeto.txt` e reescrito toda vez que a captura limpa o plano e
        # comeca de novo; tudo o que foi fotografado DAQUELA peca veio depois.
        # Entao um quadro mais velho que o `projeto.txt` e de outra execucao — e
        # o que ele mostra pode ja nao existir. Vale em dobro aqui, porque todas
        # as execucoes usam o MESMO projeto do Tinkercad e os arquivos tem os
        # mesmos nomes: a figura velha nao chama atencao de ninguem.
        #
        # Nasceu de `lava_movable.gif`: o passo pedia o clipe, o arquivo
        # existia, abria, e a seta apontava para onde a tela tinha mudado —
        # mas os quadros eram de tres dias antes, com o nivel ainda BRANCO,
        # no meio de dezesseis clipes de ceu escuro. Nenhum guarda via. Quem
        # viu foi o olho, numa folha de contato com os dezessete lado a lado.
        cam_jogo = os.path.join(slug, "projeto.txt")
        if os.path.exists(cam_jogo):
            nascimento = os.path.getmtime(cam_jogo)
            alvos = os.path.join(slug, "alvos.json")
            quadros = {}
            if os.path.exists(alvos):
                for chave, c in json.load(open(alvos)).items():
                    for campo in ("antes", "depois"):
                        if isinstance(c.get(campo), str):
                            quadros.setdefault(c[campo], set()).add(chave)
            for arq, chaves in sorted(quadros.items()):
                cam = os.path.join(slug, arq)
                if os.path.exists(cam) and os.path.getmtime(cam) < nascimento:
                    erra(f"o quadro {arq} (clipe {'/'.join(sorted(chaves))}) e "
                         f"mais VELHO que a captura desta aula — e de outra execucao")
            for p in passos:
                img = p.get("img")
                if (img and img.startswith(slug + "/") and os.path.exists(img)
                        and os.path.getmtime(img) < nascimento):
                    erra(f"passo {p['n']}: a foto {img} e mais VELHA que o jogo "
                         "desta aula — e de outro jogo")

        # 7. o fecho tem de dizer que o trabalho FICOU, e como achar de novo.
        #
        # ⛔ Regra trocada, nao herdada. No curso de Flowlab o fecho tinha de
        #    falar do LINK do jogo, porque la a entrega e um endereco que a
        #    crianca manda para a familia. Aqui nao ha link: a entrega e uma
        #    peca guardada na conta dela. Mantida a regra do irmao, ela
        #    reprovaria todo fecho honesto deste curso e so passaria se eu
        #    inventasse um link que nao existe.
        fecho = A.get("fim", "").lower()
        if not any(w in fecho for w in ("salv", "guardad", "na sua conta")):
            erra("o fecho da aula nao diz que a peca ficou salva na conta")

    return erros


if __name__ == "__main__":
    e = confere()
    for m in e:
        print("  !!", m)
    print(f"  {len(e)} problema(s)")
    raise SystemExit(1 if e else 0)
