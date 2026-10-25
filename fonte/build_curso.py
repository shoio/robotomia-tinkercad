#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta o site do curso na RAIZ do repositorio, a partir de fonte/.

   Rode de qualquer lugar: `python3 fonte/build_curso.py`.
"""
import os, json, shutil
from PIL import Image
import gera_curso as G
import conteudo_a1
import todas_as_aulas

AQUI  = os.path.dirname(os.path.abspath(__file__))     # .../fonte
SAIDA = os.path.dirname(AQUI)                          # a raiz do repositorio
os.chdir(AQUI)   # todos os caminhos de conteudo sao relativos a fonte/

PLANO = [
    (1, "Chaveiro com o seu nome",
     "Uma plaquinha com o seu nome em relevo e um furo que atravessa. A primeira peça 3D.", True),
    (2, "Caneca e porta-lápis",
     "Esvaziar por dentro: o mesmo truque do furo, agora para fazer um recipiente.", False),
]


def aula1(): return _de_conteudo(conteudo_a1)


def construtores():
    """Uma aula entra no build quando o PLANO diz `pronta` E o conteudo existe."""
    por_n = {m.AULA["n"]: m for m in todas_as_aulas.modulos()}
    return [(lambda m=por_n[n]: _de_conteudo(m)) for n, _t, _s, pronta in PLANO
            if pronta and n in por_n]


def _de_conteudo(mod):
    a = dict(mod.AULA)
    passos = []
    for p in a["passos"]:
        q = dict(p); q["foto"] = os.path.basename(p["img"])
        passos.append(q)
    a["passos"] = passos
    a["fotos_de"] = None      # as fotos vem de caminhos variados; copio uma a uma
    a["clipes_de"] = f'{a["slug"]}/gifs'
    return a


def indice(aulas_prontas):
    cartoes = []
    for n, tit, sub, pronta in PLANO:
        if pronta:
            cartoes.append(f'<a class="cartao" href="aula{n}/"><div class="num">Aula {n}</div>'
                           f'<h3>{tit}</h3><p>{sub}</p></a>')
        else:
            cartoes.append(f'<div class="cartao embreve"><div class="num">Aula {n} · em breve</div>'
                           f'<h3>{tit}</h3><p>{sub}</p></div>')
    return (G.CABECA.format(titulo="Tinkercad na Robotomia", css=G.CSS, corpo_attr="",
                            desc="Curso de modelagem 3D no Tinkercad, da Robotomia: passo a passo, "
                                 "com animação em cada gesto.") + f'''
<header class="barra"><div class="barra-in">
  <div class="marca">Robotomia <span>· Tinkercad</span></div>
  <div class="conta">{len(aulas_prontas)} de {len(PLANO)} aulas no ar</div>
</div></header>

<div class="capa">
  <span class="etiqueta">Curso · 8 a 15 anos</span>
  <h1>Modelagem 3D no Tinkercad</h1>
  <p class="linha-fina">Aulas de 50 minutos. Cada uma começa num projeto novo e termina com uma
  peça 3D pronta, salva na conta do aluno. Sem impressora: a peça fica na tela, e dá para girar
  e olhar por baixo. Cada passo tem uma foto da tela de verdade, e os gestos novos têm uma
  animação curta com o botão certo acendendo.</p>
</div>

<div class="grade">
{chr(10).join(cartoes)}
</div>

<p class="fim">Feito para a Robotomia. Todas as figuras são capturas reais do Tinkercad em
português. Se um passo não funcionar na sua tela, o quadro laranja do próprio passo tem o
conserto.</p>
</body></html>''')


def monta():
    # o guarda roda ANTES de gerar: toda regra dele nasceu de um defeito
    # que passou pela leitura e so apareceu seguindo a aula como aluno.
    import confere_aulas, confere_alvos, confere_gesto
    problemas = confere_aulas.confere()
    # E o guarda dos CLIPES, que ate agora existia e nao era chamado por
    # ninguem: a seta tem de apontar para onde a tela mudou.
    # ⛔ `confere_alvos.confere()` devolve (problemas, quantos_conferiu). Somar a
    #    tupla direto na lista jogava o CONTADOR dentro dos problemas e o build
    #    parava dizendo «!! 16». E se o guarda não viu gesto nenhum, isso é falha
    #    — zero conferido não é aprovação.
    probs_alvos, vistos = confere_alvos.confere()
    problemas += probs_alvos
    if not vistos:
        problemas.append("o guarda dos clipes não conferiu gesto nenhum")
    # E o terceiro: a seta e a ordem do passo falam do MESMO item. Sem ele,
    # um clipe trocado de passo passa pelos outros dois sem reclamação —
    # a tela muda no lugar certo, só que não é aquilo que o passo manda fazer.
    probs_casa, casados = confere_gesto.confere()
    problemas += probs_casa
    if not casados:
        problemas.append("o guarda do casamento não casou clipe nenhum")
    if problemas:
        for m in problemas:
            print("  !!", m)
        raise SystemExit("as aulas nao passaram no guarda")
    # Apago so o que ESTE script cria. Um rmtree da pasta inteira ja levou o
    # .git junto uma vez; agora que a saida e a raiz do repositorio, ele
    # levaria tambem a fonte/ que esta gerando o site.
    os.makedirs(SAIDA, exist_ok=True)
    meus = {f"aula{n}" for n, *_ in PLANO} | {"index.html", ".nojekyll"}
    for nome in sorted(meus):
        alvo = os.path.join(SAIDA, nome)
        if os.path.isdir(alvo):
            shutil.rmtree(alvo)
        elif os.path.exists(alvo):
            os.remove(alvo)
    prontas = []
    for construtor in construtores():
        a = construtor()
        pasta = os.path.join(SAIDA, a["slug"])
        os.makedirs(os.path.join(pasta, "fotos"), exist_ok=True)
        os.makedirs(os.path.join(pasta, "clipes"), exist_ok=True)
        # fotos
        for p in a["passos"]:
            orig = p["img"] if "img" in p else os.path.join(a["fotos_de"], p["foto"])
            if not os.path.exists(orig):
                orig = os.path.join(a["fotos_de"], p["foto"])
            # sempre JPEG: PNG de captura pesa ~1 MB e a turma abre a pagina
            # toda ao mesmo tempo na rede da escola
            p["foto"] = os.path.splitext(p["foto"])[0] + ".jpg"
            destino = os.path.join(pasta, "fotos", p["foto"])
            if not os.path.exists(destino):
                im = Image.open(orig).convert("RGB")
                if im.height > 1620:            # corta a barra de comando do rodape
                    im = im.crop((0, 0, im.width, 1620))
                L = 1200
                im = im.resize((L, round(im.height * L / im.width)), Image.LANCZOS)
                im.save(destino, quality=84, optimize=True)
        # clipes
        for p in a["passos"]:
            for _rot, arq in G.clipes_do(p):
                o = os.path.join(a["clipes_de"], arq)
                d = os.path.join(pasta, "clipes", arq)
                if os.path.exists(o) and not os.path.exists(d):
                    shutil.copy(o, d)
        open(os.path.join(pasta, "index.html"), "w").write(G.pagina_aula(a, len(PLANO)))
        prontas.append(a)
        print(f"  aula {a['n']}: {len(a['passos'])} passos, "
              f"{len(os.listdir(os.path.join(pasta,'clipes')))} clipes")
    open(os.path.join(SAIDA, "index.html"), "w").write(indice(prontas))
    open(os.path.join(SAIDA, ".nojekyll"), "w").write("")
    # Um PDF por aula, impresso da propria pagina — assim ele nunca envelhece
    # em relacao ao site (o PDF antigo da Aula 1 ainda mandava clicar num botao
    # que o texto ja tinha deixado de citar).
    import faz_pdfs
    faz_pdfs.main()
    return prontas


if __name__ == "__main__":
    monta()
