#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O GUARDA DOS CLIPES: a seta tem de terminar onde a tela MUDOU.

   Herdado do curso de Flowlab e REESCRITO, porque a regra de lá não é a
   convenção aqui. Lá a regra era «perto da SETA tem de ter mudado alguma
   coisa», com uma bandeira `clicado` para abrir exceção. No Tinkercad metade
   dos gestos é ARRASTO da palheta: a seta começa num item que não muda e o
   que muda fica do outro lado da tela. Com a regra de lá, ou os três arrastos
   reprovavam, ou todos iam para a exceção — e exceção que cobre o caso
   difícil é a bandeira que não guarda nada.

   A regra daqui não precisa de exceção nenhuma:

       o FIM do gesto (`ate` no arrasto, `alvo` no clique) tem de cair onde
       a imagem ANTES e a imagem DEPOIS são diferentes.

   E uma segunda, que só existe porque aqui o alvo vem do DOM:

       o `rotulo` gravado é o nome que a máquina leu no elemento clicado —
       o `confere_gesto.py` confere que o PASSO da aula cita esse mesmo nome.

       python3 fonte/confere_alvos.py
"""
import json, os, sys
import numpy as np
from PIL import Image

os.chdir(os.path.dirname(os.path.abspath(__file__)))

RAIO   = 170        # o quanto em volta do fim do gesto eu aceito como "foi ali"
CANTO  = 60         # perto demais de um canto é sinal de alvo não preenchido

# ⛔ O 400 que veio do curso de Flowlab reprovava dois gestos CERTOS: digitar
#    30 num campo onde estava 20 muda só os riscos de dois algarismos (217 px),
#    e o guarda chamava isso de "seta no vazio". Número herdado não é medida.
#    Medido aqui: em janela inerte do mesmo par de quadros a conta dá 0 px, e o
#    menor sinal verdadeiro dos 14 gestos dá 217. Daí o 60 — bem acima do ruído.
MINIMO = 60
# E para o 60 não virar barra sem sentido no dia em que a captura ficar
# ruidosa, cada par leva CONTROLE NEGATIVO: janelas que têm de dar quase zero.
# As janelas de controle dependem do TAMANHO do quadro, então são declaradas por
# tamanho. Para a tela cheia do editor são da COLUNA DA PALHETA, longe dos itens
# que a aula arrasta: nenhum passo repinta ali. (A barra de cima NÃO serve: com
# raio de 170 a janela alcança o plano de trabalho, e o passo que gira a câmera a
# suja com 1386 px.) Para o recorte do menu «Criar», são o lado esquerdo, onde o
# menu não chega.
# ⛔ Tamanho não declarado é ERRO, não é «sem controle». Com janela caindo fora
#    da imagem o numpy devolve fatia vazia, a soma dá 0, e o controle negativo
#    passa a aprovar tudo sem medir nada.
CONTROLES = {
    (1440, 900): ((1300, 860), (1390, 500)),
    ( 620, 285): ((  60, 220), (  60,  60)),
}
RUIDO_MAX = 50


def mudou_perto(pasta, dados, ponto, raio=RAIO):
    """(quantos pixels mudaram perto do ponto, quantos mudaram na tela toda)"""
    a = os.path.join(pasta, dados["antes"])
    b = os.path.join(pasta, dados["depois"])
    if not (os.path.exists(a) and os.path.exists(b)):
        return None, None
    A = np.asarray(Image.open(a).convert("L"), dtype=int)
    B = np.asarray(Image.open(b).convert("L"), dtype=int)
    if A.shape != B.shape:
        return None, None
    dif = np.abs(A - B) > 30
    x, y = ponto
    y0, y1 = max(0, y - raio), min(A.shape[0], y + raio)
    x0, x1 = max(0, x - raio), min(A.shape[1], x + raio)
    return int(dif[y0:y1, x0:x1].sum()), int(dif.sum())


def confere(pastas=None):
    pastas = pastas or sorted(p for p in os.listdir(".")
                              if p.startswith("aula") and os.path.isdir(p))
    problemas, vistos = [], 0
    for pasta in pastas:
        tudo = {}
        for arq in ("alvos.json", "alvos0.json"):
            if os.path.exists(f"{pasta}/{arq}"):
                tudo.update(json.load(open(f"{pasta}/{arq}")))
        if not tudo:
            continue
        for chave, dados in sorted(tudo.items()):
            if dados.get("tipo") == "marca":     # não é clipe: é círculo em foto
                continue
            vistos += 1
            alvo = dados.get("alvo")
            if not alvo or len(alvo) != 2:
                problemas.append(f"{pasta}/{chave}: sem alvo")
                continue
            if not dados.get("rotulo"):
                problemas.append(f"{pasta}/{chave}: sem rótulo — a seta não "
                                 "sabe dizer em que ela clicou")
                continue
            if alvo[0] < CANTO and alvo[1] < CANTO:
                problemas.append(f"{pasta}/{chave}: a seta aponta para o CANTO "
                                 f"da tela {alvo} — alvo não preenchido")
                continue
            fim = dados.get("ate") or alvo
            perto, total = mudou_perto(pasta, dados, fim)
            if perto is None:
                problemas.append(f"{pasta}/{chave}: faltam os quadros do clipe")
                continue
            tam = Image.open(os.path.join(pasta, dados["antes"])).size
            if tam not in CONTROLES:
                problemas.append(f"{pasta}/{chave}: quadro {tam[0]}×{tam[1]} sem "
                                 "janelas de controle declaradas — sem controle "
                                 "negativo este guarda não vale nada")
                continue
            ruido = max(mudou_perto(pasta, dados, c)[0] for c in CONTROLES[tam])
            if ruido > RUIDO_MAX:
                problemas.append(f"{pasta}/{chave}: controle negativo sujo "
                                 f"({ruido} px onde nada devia mudar) — com esse "
                                 f"ruído o mínimo de {MINIMO} px não prova nada")
                continue
            if total < 200:
                problemas.append(f"{pasta}/{chave}: a tela não mudou entre os "
                                 f"dois quadros ({total} px) — clipe sem gesto")
            elif perto < MINIMO:
                onde = "o fim do arrasto" if dados.get("ate") else "a seta"
                problemas.append(f"{pasta}/{chave}: {onde} cai em {fim}, onde "
                                 f"quase nada mudou ({perto} px num raio de "
                                 f"{RAIO}; a tela toda mudou {total})")
    return problemas, vistos


def prova():
    """SABOTAGEM REPETÍVEL: muda um alvo de lugar e exige que o guarda veja.

    ⛔ Guarda novo se prova duas vezes. Limpo ele dá zero problemas — o que
    também é o que um guarda cego dá. Aqui ele leva, numa cópia, uma seta
    arrastada para um canto morto do plano, e tem de reprovar justamente esse
    gesto. Fica atrás de bandeira para poder repetir, não é teste de uma vez só.

        python3 fonte/confere_alvos.py --prova
    """
    import shutil, tempfile
    base = sorted(p for p in os.listdir(".")
                  if p.startswith("aula") and os.path.isdir(p))[0]
    tmp = tempfile.mkdtemp(prefix="provaalvos_")
    falso = os.path.join(tmp, base)
    shutil.copytree(base, falso)
    dados = json.load(open(f"{falso}/alvos.json"))
    vitima = sorted(dados)[0]
    dados[vitima]["alvo"] = [980, 820]          # canto morto do plano
    dados[vitima].pop("ate", None)
    json.dump(dados, open(f"{falso}/alvos.json", "w"))
    aqui = os.getcwd()
    os.chdir(tmp)
    try:
        e, n = confere([base])
    finally:
        os.chdir(aqui)
        shutil.rmtree(tmp, ignore_errors=True)
    pegou = [m for m in e if vitima in m]
    print(f"  sabotado: {vitima} apontando para o vazio")
    for m in e:
        print("    ->", m)
    if not pegou:
        print("  !! O GUARDA NÃO VIU A SABOTAGEM — ele está cego")
        return 1
    print(f"  ok: o guarda reprovou {vitima}, e só ele ({len(e)} problema(s))")
    return 0


if __name__ == "__main__":
    if "--prova" in sys.argv:
        raise SystemExit(prova())
    e, n = confere([a for a in sys.argv[1:] if not a.startswith("-")] or None)
    for m in e:
        print("  !!", m)
    if not n:
        print("  !! nenhum gesto conferido — guarda com zero medido é guarda cego")
        raise SystemExit(1)
    print(f"  {n} gesto(s) conferido(s), {len(e)} problema(s)")
    raise SystemExit(1 if e else 0)
