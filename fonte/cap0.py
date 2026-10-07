#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Passos 1 a 3 — do site até o editor aberto.

⛔ PRIVACIDADE, e isto não é detalhe: o painel do Tinkercad do dono mostra o
   NOME REAL dele na barra da esquerda e as capas de 64 projetos particulares
   (inclusive material da Robotomia que ainda não saiu). Este curso vai para um
   site público no GitHub. Então:

     · o passo 1 é fotografado numa sessão SEM CONTA (contexto novo, sem
       perfil) — é a página de entrada que qualquer criança vê;
     · os passos 2 e 3 recortam só a FAIXA DE CIMA do painel, onde mora o
       botão Criar. Nenhuma capa de projeto, nenhum nome, entra no recorte.
     · toda captura passa por `sem_vazamento()` antes de virar arquivo.

   python3 fonte/cap0.py
"""
import os, sys, time
from playwright.sync_api import sync_playwright
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from bancada import Bancada, Falhou

PASTA  = os.path.join(AQUI, "aula1")
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
# ⛔ Começa em x=240, e não em 0, porque a BARRA DA ESQUERDA do painel traz a
#    foto e o NOME REAL do dono logo abaixo do logotipo. Com o recorte em 0 o
#    `sem_vazamento` reprovou na primeira execução, dizendo o nome dele — que
#    é exatamente o serviço que ele tem de prestar.
FAIXA  = (820, 0, 1440, 285)    # o canto de cima à direita: Criar e o menu
DONO   = ("Julio", "Schoenardie", "Robotomia", "Bruticus", "Borwo", "Leelo")


def sem_vazamento(pg, box):
    """Nenhum texto particular pode cair dentro do recorte que vai ser salvo."""
    achados = pg.evaluate("""(box) => {
        const fora = [];
        document.querySelectorAll('*').forEach(e => {
          if (e.children.length) return;
          const t = (e.textContent || '').trim();
          if (!t) return;
          const r = e.getBoundingClientRect();
          if (r.bottom < box[1] || r.top > box[3]) return;
          if (r.right  < box[0] || r.left > box[2]) return;
          fora.push(t);
        });
        return fora;
    }""", list(box))
    sujo = [t for t in achados if any(p.lower() in t.lower() for p in DONO)]
    if sujo:
        raise Falhou("o recorte pegaria coisa particular do dono: "
                     + "; ".join(sorted(set(sujo))[:6]))
    return len(achados)


def recorta(b, nome, box):
    png = os.path.join(PASTA, f"{nome}.png")
    Image.open(png).crop(box).save(png)
    return b.jpg(nome)


def principal():
    os.makedirs(PASTA, exist_ok=True)
    # ⛔ A marca de nascimento DESTA captura vai ANTES das figuras. Escrita no
    #    fim, ela fica mais nova que tudo o que acabou de ser fotografado, e o
    #    guarda que compara idades acusa de velha justamente a figura recém
    #    tirada. Cada captura tem a sua marca: as figuras do painel respondem a
    #    esta, as do editor respondem ao `projeto.txt` do cap1.py.
    with open(os.path.join(PASTA, "painel.txt"), "w") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    with sync_playwright() as p:

        # ---- passo 1: a página de entrada, SEM conta nenhuma --------------
        anon = p.chromium.launch(headless=True)
        # ⛔ locale pt-BR. Sem ele o Tinkercad serve a página em INGLÊS, e a
        #    figura do passo 1 saiu dizendo «Log In» enquanto o texto do passo
        #    mandava procurar «Entrar». Figura contra frase: quem confere lendo
        #    os dois não vê, quem confere olhando a figura vê na hora.
        ctx_anon = anon.new_context(locale="pt-BR",
                                    extra_http_headers={"Accept-Language": "pt-BR,pt;q=0.9"},
                                    viewport={"width": 1440, "height": 900})
        pag = ctx_anon.new_page()
        pag.goto("https://www.tinkercad.com/", wait_until="domcontentloaded",
                 timeout=60000)
        pag.wait_for_timeout(7000)
        # ⛔ O botão NÃO se chama «Entrar» nem «Log In»: chama «Fazer login».
        #    Eu escrevi os dois primeiros de cabeça e este guarda reprovou os
        #    dois. A palavra que o passo manda a criança procurar tem de ser a
        #    que está na tela — e quem sabe qual é é a tela, não eu.
        #    (A página só sai em português com locale pt-BR no navegador; sem
        #    ele o Tinkercad serve tudo em inglês.)
        PALAVRA = "Fazer login"
        if PALAVRA.lower() not in pag.evaluate("document.body.innerText").lower():
            raise Falhou(f"a página de entrada veio sem «{PALAVRA}» — é a "
                         "palavra que o passo 1 manda procurar; se o Tinkercad "
                         "mudou o rótulo, é o TEXTO do passo que tem de mudar")
        ba = Bancada(pag, PASTA)
        ba.cap("d01_site"); ba.jpg("d01_site")
        print("  ✓  1. a página de entrada em português (sessão sem conta)",
              flush=True)
        anon.close()

        # ---- passos 2 e 3: o botão Criar, só a faixa de cima --------------
        ctx = p.chromium.launch_persistent_context(
            PERFIL, headless=True, viewport={"width": 1440, "height": 900})
        pg = ctx.pages[0] if ctx.pages else ctx.new_page()
        b = Bancada(pg, PASTA)
        pg.goto("https://www.tinkercad.com/dashboard",
                wait_until="domcontentloaded", timeout=60000)
        pg.wait_for_timeout(9000)

        n = sem_vazamento(pg, FAIXA)
        print(f"     recorte da faixa conferido: {n} textos, nenhum do dono",
              flush=True)

        b.cap("d02_antes")
        criar = b.acha("Criar", 14)   # o rótulo é um span de ~20 px: filtro alto o perde
        b.clica(criar, 2200)
        b.cap("d02_depois")
        if not sem_vazamento(pg, FAIXA):
            raise Falhou("menu aberto e a faixa ficou sem texto nenhum — "
                         "guarda com zero medido não guarda nada")
        recorta(b, "d02_antes", FAIXA)
        recorta(b, "d02_depois", FAIXA)
        # o alvo é gravado em coordenadas do RECORTE, que é o que vira clipe
        b.reg("criar", "d02_antes.jpg", "d02_depois.jpg",
              (criar[0] - FAIXA[0], criar[1] - FAIXA[1]), "Criar")
        print("  ✓  2. clicar em Criar (menu abre)", flush=True)

        # onde está «Projeto 3D» dentro do menu — para o círculo do passo 3
        p3d = b.acha("Projeto 3D", 14)
        b.cap("d03_menu")
        recorta(b, "d03_menu", FAIXA)
        alvo3d = (round(p3d[0] - FAIXA[0]), round(p3d[1] - FAIXA[1]))
        cx = b.ultima_caixa
        caixa3d = [round(cx[0]-FAIXA[0]), round(cx[1]-FAIXA[1]),
                   round(cx[2]-FAIXA[0]), round(cx[3]-FAIXA[1])]
        print(f"  ✓  3. «Projeto 3D» no menu, caixa {caixa3d} do recorte", flush=True)

        b.alvos["projeto3d_ponto"] = {"alvo": list(alvo3d), "rotulo": "Projeto 3D",
                                      "tipo": "marca", "em": "d03_menu.jpg",
                                      "caixa": caixa3d}
        cam = os.path.join(PASTA, "alvos0.json")
        import json
        json.dump(b.alvos, open(cam, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print(f"\n  alvos0.json: {len(b.alvos)} itens", flush=True)
        ctx.close()


if __name__ == "__main__":
    principal()
