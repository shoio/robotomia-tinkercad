#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""O GUARDA DO CASAMENTO: a seta do clipe e a ordem do passo falam do MESMO item.

   O `confere_alvos.py` garante que a seta cai onde a tela mudou. Isso impede
   seta no vazio — mas não impede seta no lugar ERRADO: mudou alguma coisa ali,
   só que não era aquilo que o passo mandava apertar.

   Nos cursos irmãos essa segunda conferência era um relatório para LEITURA
   humana, montado com OCR em volta do ponto. Aqui não precisa: o alvo de cada
   gesto veio do DOM, e a bancada gravou junto o NOME que a máquina leu no
   elemento (`rotulo`). Então dá para transformar a leitura humana em
   invariante:

       o rótulo do elemento em que a máquina clicou tem de aparecer no TEXTO
       do passo que usa aquele clipe.

   Se um dia eu trocar a ordem dos passos, ou reaproveitar um clipe no passo
   errado, isto fica vermelho — e nenhuma leitura minha precisa ser confiável.

       python3 fonte/confere_gesto.py
"""
import json, os, re, sys, unicodedata

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# palavrinhas que não distinguem nada: exigir «a», «de», «do» seria exigir ruído
VAZIAS = {"a", "o", "as", "os", "de", "do", "da", "e", "em", "para", "com", "no", "na"}


def limpa(t):
    t = re.sub(r"<[^>]+>", " ", t)                      # tira as marcas de HTML
    t = unicodedata.normalize("NFD", t)
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]+", " ", t.lower())


def fichas(rotulo):
    return [p for p in limpa(rotulo).split() if p and p not in VAZIAS]


def confere(aulas=None):
    import gera_curso as _G
    if aulas is None:
        import conteudo_a1
        aulas = [conteudo_a1.AULA]
    problemas, casados = [], 0
    for A in aulas:
        slug = A["slug"]
        alvos = {}
        for arq in ("alvos.json", "alvos0.json"):
            if os.path.exists(f"{slug}/{arq}"):
                alvos.update(json.load(open(f"{slug}/{arq}")))
        if not alvos:
            problemas.append(f"{slug}: sem alvos.json — nada para casar")
            continue
        usados = set()
        for p in A["passos"]:
            texto = limpa(p.get("titulo", "") + " " + p.get("corpo", "") + " "
                          + p.get("depois", "") or "")
            for _rot, arquivo in _G.clipes_do(p):
                chave = arquivo[:-4] if arquivo.endswith(".gif") else arquivo
                usados.add(chave)
                d = alvos.get(chave)
                if d is None:
                    problemas.append(f"{slug} passo {p['n']}: o clipe {arquivo} "
                                     "não tem alvo gravado")
                    continue
                faltam = [f for f in fichas(d["rotulo"]) if f not in texto]
                if faltam:
                    problemas.append(
                        f"{slug} passo {p['n']} ({p['titulo'][:34]}): a seta do "
                        f"clipe {arquivo} aponta para «{d['rotulo']}», e o texto "
                        f"do passo não diz {', '.join(repr(f) for f in faltam)}")
                else:
                    casados += 1
        # clipe gravado e nunca pedido por passo nenhum é trabalho perdido —
        # e, pior, é o sinal de que um passo ficou sem a animação dele
        sobra = sorted(k for k in alvos
                       if k not in usados and alvos[k].get("tipo") != "marca")
        for k in sobra:
            problemas.append(f"{slug}: o clipe {k}.gif existe e nenhum passo o pede")
    return problemas, casados


if __name__ == "__main__":
    e, n = confere()
    for m in e:
        print("  !!", m)
    if not n:
        print("  !! nenhum casamento conferido — guarda com zero medido é cego")
        raise SystemExit(1)
    print(f"  {n} clipe(s) casado(s) com o texto do passo, {len(e)} problema(s)")
    raise SystemExit(1 if e else 0)
