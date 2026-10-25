# -*- coding: utf-8 -*-
"""A bancada do Tinkercad: dirige o editor por Playwright, em laço fechado.

Diferença para os cursos irmãos: lá o botão se acha por OCR na tela; aqui ele
se acha no DOM, pelo nome acessível ou pela dica (tooltip). O alvo do clipe é
a caixa do próprio elemento — não há leitura a errar.

⛔ Toda rotina confere o próprio efeito antes de devolver. Se não mudou nada na
   tela, ela levanta — é melhor parar do que fotografar o passo errado.
"""
import os, json, time
from PIL import Image, ImageChops

AQUI   = os.path.dirname(os.path.abspath(__file__))
PERFIL = os.environ.get("TINK_PERFIL", "/private/tmp/tinkprofile")
MUNDO  = (60, 110, 1160, 880)      # o retângulo do plano de trabalho
# ⛔ Para MEDIR a peça, o retângulo é outro: o painel de propriedades tem uma
#    bolinha VERMELHA ("Sólido") dentro de MUNDO. Medindo em MUNDO, a peça
#    "media" 514x374 px quando tinha 247x84 — a bolinha entrava na conta.
PECA   = (70, 250,  890, 878)      # só o plano, à esquerda do painel


class Falhou(Exception):
    pass


# ───────────────────────────────── imagem ──────────────────────────────────

def diferenca(a, b, box=MUNDO):
    """Quantos por cento dos pixels mudaram entre duas capturas."""
    A = Image.open(a).convert("RGB").crop(box)
    B = Image.open(b).convert("RGB").crop(box)
    d = ImageChops.difference(A, B).convert("L")
    n = sum(1 for v in d.getdata() if v > 18)
    return 100.0 * n / (d.width * d.height)


# ───────────────────────────────── a bancada ───────────────────────────────

class Bancada:
    def __init__(self, pg, pasta):
        self.pg = pg
        self.pasta = pasta
        os.makedirs(pasta, exist_ok=True)
        self.alvos = {}
        self._n = 0

    # ---- capturas -------------------------------------------------------

    DESCANSO = (220, 830)      # canto vazio do plano, longe de tudo

    def cap(self, nome, parar=True):
        """Salva a tela inteira. Devolve o caminho.

        ⛔ Tira o ponteiro da frente antes de fotografar. Parado em cima de uma
        peça ou de um botão, ele acende realce e dica que não são do passo —
        e o clipe desenha o próprio ponteiro por cima depois.
        """
        if parar:
            self.pg.mouse.move(*self.DESCANSO)
            self.pg.wait_for_timeout(500)
        cam = os.path.join(self.pasta, f"{nome}.png")
        self.pg.screenshot(path=cam)
        return cam

    def jpg(self, nome, q=92):
        """Converte a captura para JPEG q92, como o padrão manda."""
        png = os.path.join(self.pasta, f"{nome}.png")
        jpg = os.path.join(self.pasta, f"{nome}.jpg")
        Image.open(png).convert("RGB").save(jpg, "JPEG", quality=q)
        os.remove(png)
        return jpg

    def reg(self, gesto, antes, depois, alvo, rotulo, ate=None,
            tipo=None, teclas=None, botao="esq", abre_janela=False):
        """Registra um gesto para virar clipe.

        `rotulo` é o nome que o PASSO vai citar. O guarda confere que o alvo
        gravado é mesmo o elemento com esse nome — é o invariante que substitui
        o OCR dos cursos irmãos.

        ⛔ `ate` é obrigatório no ARRASTO. Sem ele o guarda herdado («perto da
        seta tem de ter mudado alguma coisa») reprova todo arrasto de palheta,
        onde a seta começa num item que não muda e o que muda é o plano do
        outro lado da tela — e a saída seria uma bandeira de exceção, que é
        pior. O fim do gesto é o endereço certo para a conferência.
        """
        d = {"antes": antes, "depois": depois,
             "alvo": [round(alvo[0]), round(alvo[1])],
             "rotulo": rotulo,
             "tipo": tipo or ("arrasto" if ate is not None else "clique")}
        if ate is not None:
            d["ate"] = [round(ate[0]), round(ate[1])]
        if teclas:
            d["teclas"] = list(teclas)
        if botao != "esq":
            d["botao"] = botao
        if abre_janela:
            # o gesto ABRE uma janela grande (a paleta de cores) que cai sobre as
            # janelas de controle negativo: o guarda não pode exigir silêncio ali
            d["abre_janela"] = True
        if d["tipo"] == "tecla" and not teclas:
            raise Falhou(f"{gesto}: gesto de tecla sem dizer QUAIS teclas")
        self.alvos[gesto] = d

    def grava_alvos(self):
        cam = os.path.join(self.pasta, "alvos.json")
        with open(cam, "w", encoding="utf-8") as f:
            json.dump(self.alvos, f, ensure_ascii=False, indent=1)
        return cam

    # ---- achar coisas na tela -------------------------------------------

    def acha(self, nome, minw=10):
        """Elemento pelo nome acessível (aria-label, title ou texto exato).

        Duas passadas, nesta ordem:
          1ª  elemento-FOLHA (ou com aria/title). É a regra que já estava de pé
              e que a palheta de formas obedece.
          2ª  se a 1ª não achar nada, o MENOR elemento cujo texto inteiro é o
              nome. ⛔ Foi preciso porque os itens do menu «Criar» são <a> com
              um ícone dentro: não são folha, não têm aria-label, e a 1ª passada
              passava reto por «Projeto 3D». Menor = o mais interno, que é o
              que a criança enxerga como o item.
        """
        r = self.pg.evaluate("""([nome, minw]) => {
            let folha = null, qualquer = null;
            document.querySelectorAll('*').forEach(e => {
              const a = (e.getAttribute && (e.getAttribute('aria-label') || e.getAttribute('title'))) || '';
              const todo = (e.textContent || '').trim();
              const r = e.getBoundingClientRect();
              if (r.width < minw || r.height < minw) return;
              // só o que está DENTRO da tela: «Projeto 3D» casou uma vez com um
              // elemento a 1441 px de altura, fora da janela, e o alvo saiu do
              // recorte — seta apontando para fora da própria figura.
              if (r.bottom <= 0 || r.top >= window.innerHeight) return;
              if (r.right <= 0 || r.left >= window.innerWidth) return;
              const p = {x:r.x+r.width/2, y:r.y+r.height/2, a:r.width*r.height,
                         x0:r.x, y0:r.y, x1:r.right, y1:r.bottom};
              if ((a || (e.children.length === 0 ? todo : '')) === nome) {
                if (!folha || r.y > folha.y) folha = p;       // o mais de baixo
              } else if (todo === nome) {
                if (!qualquer || p.a < qualquer.a) qualquer = p;  // o mais interno
              }
            });
            return folha || qualquer;
        }""", [nome, minw])
        if not r:
            raise Falhou(f"não achei {nome!r} na tela")
        self.ultima_caixa = (r["x0"], r["y0"], r["x1"], r["y1"])
        return (r["x"], r["y"])

    def acha_por_dica(self, comeco):
        """Botão da barra pela DICA que aparece ao passar o mouse.

        Os botões de agrupar não têm nome acessível nenhum: o único lugar
        onde o nome existe é a dica. Varre a faixa da barra e lê.
        """
        for x in range(700, 1180, 48):
            self.pg.mouse.move(x, 72)
            self.pg.wait_for_timeout(900)
            txt = self.pg.evaluate("""() => {
                let s = '';
                document.querySelectorAll('[role=tooltip],[class*=ooltip],[class*=Tooltip]').forEach(e => {
                  const r = e.getBoundingClientRect();
                  if (r.width > 5) s += ' ' + (e.textContent || '').trim();
                });
                return s;
            }""")
            if comeco.lower() in txt.lower():
                self.pg.mouse.move(600, 500)      # tira a dica da frente
                self.pg.wait_for_timeout(400)
                return (x, 72)
        raise Falhou(f"nenhum botão da barra tem dica começando por {comeco!r}")

    def acha_campo(self, rotulo):
        """O campo de medida que fica logo abaixo do rótulo (Comprimento…).

        ⛔ Nunca por coordenada fixa: o painel desliza entre execuções — os
        mesmos cinco campos já apareceram em y=444 e em y=456. O endereço é
        sempre «o input logo abaixo do rótulo», lido na hora.

        Devolve (locator, ponto) — o locator porque `fill()` é o único jeito
        que entra; a digitação sintética não registra neste campo.
        """
        lab = self.pg.evaluate("""(rot) => {
            let m = null;
            document.querySelectorAll('*').forEach(e => {
              if (e.children.length) return;
              if ((e.textContent || '').trim() !== rot) return;
              const r = e.getBoundingClientRect();
              if (r.width < 5) return;
              m = {x:r.x, y:r.y};
            });
            return m;
        }""", rotulo)
        if not lab:
            raise Falhou(f"não achei o rótulo {rotulo!r} na tela")
        inputs = self.pg.locator("input")
        melhor = None
        for i in range(inputs.count()):
            bb = inputs.nth(i).bounding_box()
            if not bb or bb["width"] < 8:
                continue
            dy = bb["y"] - lab["y"]
            if dy < -8 or dy > 48 or bb["x"] < lab["x"] - 24:
                continue
            if melhor is None or abs(dy) < melhor[0]:
                melhor = (abs(dy), inputs.nth(i),
                          (bb["x"] + bb["width"]/2, bb["y"] + bb["height"]/2))
        if melhor is None:
            raise Falhou(f"achei o rótulo {rotulo!r} mas nenhum campo abaixo dele")
        return melhor[1], melhor[2]

    # ---- gestos ---------------------------------------------------------

    def clica(self, ponto, espera=1200):
        self.pg.mouse.move(ponto[0], ponto[1])
        self.pg.wait_for_timeout(260)
        self.pg.mouse.click(ponto[0], ponto[1])
        self.pg.wait_for_timeout(espera)

    def arrasta(self, origem, destino, passos=16, pressao=480):
        """Arrasto com pressão longa antes de mover.

        Sem a pausa depois do mouse.down a palheta não registra o gesto —
        o mesmo defeito que o curso de Flowlab mediu na mesa de blocos.
        """
        self.pg.mouse.move(origem[0], origem[1]); self.pg.wait_for_timeout(320)
        self.pg.mouse.down();                     self.pg.wait_for_timeout(pressao)
        for i in range(1, passos + 1):
            t = i / passos
            self.pg.mouse.move(origem[0] + (destino[0]-origem[0])*t,
                               origem[1] + (destino[1]-origem[1])*t)
            self.pg.wait_for_timeout(45)
        self.pg.wait_for_timeout(360)
        self.pg.mouse.up()
        self.pg.wait_for_timeout(2200)

    def escreve_campo(self, rotulo, valor):
        """Põe um número num campo de medida e confere que entrou.

        ⛔ Não deixe esta conferência passar calada. A primeira versão só
        reclamava quando CONSEGUIA ler o campo; quando a leitura falhava ela
        devolvia sem dizer nada, e o passo seguinte fotografava uma caixa que
        nunca mudou de tamanho. Se não dá para ler, é falha.
        """
        loc, ponto = self.acha_campo(rotulo)
        loc.fill(str(valor))
        loc.press("Enter")
        self.pg.wait_for_timeout(1200)
        try:
            lido = loc.input_value()
        except Exception as e:
            raise Falhou(f"{rotulo}: não consegui reler o campo ({type(e).__name__})")
        if not str(lido).startswith(str(valor)):
            raise Falhou(f"{rotulo}: pedi {valor!r}, o campo ficou {lido!r}")
        return ponto

    def renomeia(self, novo, ponto=(178, 24)):
        """Troca o nome do projeto. Devolve o ponto que foi clicado.

        ⛔ O nome NÃO é um input até alguém clicar nele: no DOM parado ali só
        há uma <div>. Procurar input no alto da tela devolve lista vazia e a
        leitura fácil é «não dá para renomear». Clique primeiro, leia depois.
        """
        self.pg.mouse.click(*ponto)
        self.pg.wait_for_timeout(1400)
        campo = None
        for i in range(self.pg.locator("input").count()):
            bb = self.pg.locator("input").nth(i).bounding_box()
            if bb and bb["y"] < 60 and bb["width"] > 80:
                campo = self.pg.locator("input").nth(i); break
        if campo is None:
            raise Falhou("cliquei no nome do projeto e nenhum campo apareceu")
        campo.fill(novo)
        campo.press("Enter")
        self.pg.wait_for_timeout(2000)
        return ponto

    def tecla(self, atalho, espera=1500):
        self.pg.keyboard.press(atalho)
        self.pg.wait_for_timeout(espera)

    # ---- medir a peça na tela -------------------------------------------

    def bbox_vermelho(self, captura, tol=78, box=PECA):
        """Onde está a peça vermelha, em pixels da tela.

        ⛔ Não solte peça em coordenada combinada de cabeça. A plaquinha muda
        de tamanho e de lugar quando você digita as medidas, e o ponto que
        servia antes cai fora depois. Meça a peça na captura e solte a partir
        dela — foi o que arrumou o nome empilhado e o furo fora do lugar.
        """
        im = Image.open(captura).convert("RGB").crop(box)
        px = im.load()
        xs, ys = [], []
        for y in range(0, im.height, 2):
            for x in range(0, im.width, 2):
                r, g, b = px[x, y]
                if r > 120 and r > g + 45 and r > b + 45:
                    xs.append(x); ys.append(y)
        if len(xs) < 60:
            raise Falhou(f"não achei peça vermelha em {os.path.basename(captura)}")
        return (box[0] + min(xs), box[1] + min(ys),
                box[0] + max(xs), box[1] + max(ys))

    def furo_vazado(self, captura, ponto, r=16, controles=(46, 110), minimo=60):
        """O furo está ABERTO? Procura a luz do chão através dele.

        ⛔ O furo nasce EM CIMA da plaquinha: ao soltar uma forma sobre a face
        de outra, o Tinkercad cria um plano de trabalho ali e a nova peça
        começa em z = 4 mm. Agrupar assim não tira nada — fica só um risco no
        topo, que de longe passa por furo. A conferência é a mesma que a aula
        pede à criança: dá para ver o chão através dele?

        ⛔ Não basta espiar UM pixel no meio: nesta câmera o meio do quadrado
        cai na parede de dentro do furo, que é vermelha. Conta os pixels claros
        da janela inteira — e mede duas janelas iguais em plaquinha lisa como
        controle negativo, para o guarda não passar por a peça ter sumido.
        """
        im = Image.open(captura).convert("RGB")

        def claros(cx, cy):
            n = 0
            for y in range(int(cy)-r, int(cy)+r+1):
                for x in range(int(cx)-r, int(cx)+r+1):
                    R, G, B = im.getpixel((x, y))
                    if R - (G + B) / 2 < 20 and R > 150:
                        n += 1
            return n

        dentro = claros(*ponto)
        fora = [claros(ponto[0] + dx, ponto[1]) for dx in controles]
        if max(fora) > 5:
            raise Falhou(f"controle negativo sujo: devia ser plaquinha cheia ao lado "
                         f"do furo e vi {fora} pixels claros — a peça saiu do lugar?")
        if dentro < minimo:
            raise Falhou(f"o furo não vazou: {dentro} pixels de chão à vista "
                         f"(mínimo {minimo}); a caixinha desceu o bastante?")
        return dentro, fora

    def centro_vermelho(self, captura, **kw):
        x0, y0, x1, y1 = self.bbox_vermelho(captura, **kw)
        return ((x0 + x1) / 2, (y0 + y1) / 2)

    # ---- conferência ----------------------------------------------------

    def mudou(self, antes, depois, minimo=0.4, box=MUNDO, oque=""):
        pc = diferenca(antes, depois, box)
        if pc < minimo:
            raise Falhou(f"a tela não mudou o bastante{' em ' + oque if oque else ''}: "
                         f"{pc:.2f}% (mínimo {minimo}%)")
        return pc
