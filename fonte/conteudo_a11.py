# -*- coding: utf-8 -*-
"""Aula 11 — Peça que encaixa: furo de 12 mm e pino de 10 mm.

Medido na bancada (fonte/cap11.py). Pegadinhas:
  · FOLGA: o pino do MESMO diâmetro do furo não entra numa peça impressa; 12 contra
    10 deixa 1 mm de cada lado — de cima, é um anel fininho entre o pino e a placa
    (medido: ~0,5 a 1 mm na tela, 4 px/mm);
  · o furo (Orifício) fica FORA da placa até ser alinhado, e o Alinhar centra os dois;
  · a placa tem de ser FIXA (clique nela) senão ela anda até o furo.
"""
import ast
INTRO = ast.literal_eval(open(__file__.replace("conteudo_a11.py", "_intro11.txt")).read())

AULA = {
 "n": 11,
 "slug": "aula11",
 "titulo": "Peça que encaixa",
 "subtitulo": "Uma placa com um furo de 12 mm e um pino de 10 mm: a conta da folga que faz duas peças se encaixarem de verdade.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 11 · folga e encaixe",
 "fim": "Acabou a Aula 11. Você fez uma <b>placa com furo</b> e um <b>pino</b> que entra nele — e descobriu a conta da <b>folga</b>: furo de 12 mm, pino de 10 mm, <b>1 mm de espaço</b> de cada lado. Numa impressora de verdade, peça com o mesmo tamanho do furo <b>não entra</b>: a folga deixa. De cima, a folga é o <b>anel fininho</b> entre o pino e a placa. As peças estão salvas na sua conta com o nome que você deu. <i>Desafio:</i> faça um pino de 11,8 mm: a folga fica minúscula — e o encaixe, apertado.",
 "avisos": [
   ("Projeto novo", "Esta aula começa num projeto novo, vazio. As peças das aulas anteriores continuam guardadas na sua conta."),
   ("Folga", "<b>Folga</b> é o espaço que sobra entre duas peças que se encaixam. Sem ela, a peça impressa <b>trava</b>: a impressora nunca acerta o milímetro exato."),
   ("O que você já sabe", "Cilindro pelas alças (Aula 2), Orifício e União (Aulas 1 e 2), Alinhar com uma peça fixa e Shift + clique (aulas 3 e 4)."),
   ("Os clipes", "Os passos com animação mostram o gesto inteiro: o mouse andando, o <b>botão certo acendendo</b> e as <b>teclas acesas</b> quando o gesto é de teclado."),
   ("Travou?", "Todo passo tem um quadro laranja embaixo com o conserto dos erros mais comuns."),
 ],
 "passos": INTRO + [

  dict(n=4, titulo="Arraste uma Caixa para o plano: a placa", img="aula11/g02_depois.jpg", clipe="caixa.gif",
    corpo="Na coluna da direita, a forma <b>vermelha</b> do meio da segunda fileira, à esquerda, é a <span class=ui>Caixa</span>. Segure o botão esquerdo nela, <b>arraste até o meio do plano</b> e solte.",
    ck="Tem um cubo vermelho no meio do plano e o painel diz <span class=ui>Caixa</span>.",
    sos=[("Peguei a caixa cinza listrada","Essa é o <b>buraco</b>. Aperte <span class=ui>Delete</span> e arraste a vermelha.")]),

  dict(n=5, titulo="Placa: Comprimento 40, Largura 40, Altura 8", img="aula11/g03_depois.jpg", clipe="medidas_placa.gif",
    corpo="No painel, escreva <b>40</b> em <span class=ui>Comprimento</span>, <b>40</b> em <span class=ui>Largura</span> e <b>8</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada). Uma <b>placa quadrada</b> fininha.",
    ck="O cubo virou uma placa quadrada e baixa.",
    sos=[("Digitei e nada mudou","Falta o <span class=ui>Enter</span> depois de cada número.")]),

  dict(n=6, titulo="Arraste um Cilindro para a esquerda: o furo", img="aula11/g04_depois.jpg", clipe="cilindro.gif",
    corpo="Na coluna da direita, a forma <b>laranja</b> do meio da segunda fileira é o <span class=ui>Cilindro</span>. Arraste-o e solte <b>no plano, à esquerda da placa</b>, fora dela.",
    ck="Tem um cilindro laranja no plano, à esquerda da placa, e o painel diz <span class=ui>Cilindro</span>.",
    sos=[("Peguei o cilindro cinza listrado","Esse já é o buraco. Pule o passo 8, mas siga as medidas."),
         ("Soltei em cima da placa","Arraste-o de novo para o plano vazio, ao lado.")]),

  dict(n=7, titulo="Furo: 12 × 12 × 12, pelas alças", img="aula11/g05_depois.jpg", clipe="medidas_furo.gif",
    corpo="O cilindro não tem campo de medida: use as <b>alças</b>. Clique na <b>alça do canto</b> de cima à esquerda; no número da <b>esquerda</b> escreva <b>12</b> e <span class=ui>Enter</span>; no de <b>cima</b> escreva <b>12</b> e <span class=ui>Enter</span>. Depois clique na alça do <b>meio da tampa</b> e escreva <b>12</b> na altura.<br><br>O diâmetro do furo é <b>12 mm</b>; a altura 12 é mais que os 8 da placa, para o buraco <b>atravessar</b>.",
    ck="O cilindro virou um disco de 12 mm, mais alto que a placa.",
    sos=[("O número ficou estranho","Clique no número, aperte Ctrl + A (no Mac, Cmd + A) e escreva de novo."),
         ("Os números sumiram","Clique no cilindro e na alça do canto de novo.")]),

  dict(n=8, titulo="Transforme em Orifício", img="aula11/g06_depois.jpg", clipe="orificio.gif",
    corpo="Com o cilindro selecionado, no painel clique em <span class=ui>Orifício</span> (a bolinha cinza listrada, ao lado de <span class=ui>Sólido</span>). O cilindro fica <b>cinza e listrado</b>: agora é um buraco.",
    ck="O cilindro ficou cinza e listrado, e no painel o <span class=ui>Orifício</span> está marcado.",
    sos=[("Nada mudou de cor","Confirme que o cilindro está selecionado (com as alças) e clique na bolinha do <span class=ui>Orifício</span>.")]),

  dict(n=9, titulo="Ctrl + A, Alinhar e fixe a placa", img="aula11/g07_depois.jpg", clipe="alinhar.gif",
    corpo="Clique num lugar vazio, aperte <span class=ui>Ctrl</span> + <span class=ui>A</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>A</span>) e, na barra de cima, clique no botão <span class=ui>Alinhar</span> (ícone com linhas de tamanhos diferentes, ao lado do espelho). Aparecem as bolinhas pretas.<br><br>Depois <b>clique na placa vermelha</b>: ela fica <b>fixa</b>, e só o furo vai andar.",
    ck="Apareceram as bolinhas pretas, e a placa foi clicada (ela fica fixa).",
    sos=[("As bolinhas não apareceram","O Alinhar só abre com <b>duas ou mais</b> peças selecionadas. Aperte Ctrl + A de novo."),
         ("A seleção sumiu","Você clicou fora das peças. Aperte Ctrl + Z, abra o Alinhar de novo e clique <b>em cima do vermelho</b>.")]),

  dict(n=10, titulo="Centro em X: a bolinha do meio, embaixo", img="aula11/g08_depois.jpg", clipe="alinha_x.gif",
    corpo="Clique na <b>bolinha do meio</b> da fileira de <b>baixo</b>. O furo <b>desliza</b> para o meio da placa, da esquerda para a direita.",
    ck="O furo ficou no meio da placa, da esquerda para a direita.",
    sos=[("A placa andou","Você não fixou a placa. Aperte Ctrl + Z e volte ao passo 9.")]),

  dict(n=11, titulo="Centro em Y: a bolinha do meio, à esquerda", img="aula11/g09_depois.jpg", clipe="alinha_y.gif",
    corpo="Clique na <b>bolinha do meio</b> da coluna da <b>esquerda</b>. O furo agora também está no meio da placa, de frente para trás: aparece <b>dentro</b> dela.",
    ck="O furo aparece no centro da placa.",
    sos=[("O furo não entrou na placa","Faltou um dos dois alinhamentos. Faça o do meio de baixo (passo 10) e o do meio da esquerda (este).")]),

  dict(n=12, titulo="Esc e Grupo de união: o furo cava a placa", img="aula11/g10_depois.jpg", clipe="uniao.gif",
    corpo="Aperte <span class=ui>Esc</span>. Na barra de cima há três botõezinhos de juntar peças: clique no do <b>meio</b>, o <span class=ui>Grupo de união</span>.<br><br>O buraco <b>cava</b> a placa e as duas peças viram <b>uma só</b>: o painel diz <span class=ui>Union</span>. Agora a placa tem um <b>furo de 12 mm</b> no meio.",
    ck="A placa tem um furo redondo no meio, e o painel diz <span class=ui>Union</span>.",
    sos=[("O furo não apareceu","O furo não estava dentro da placa. Aperte Ctrl + Z, refaça os passos 10 e 11 e agrupe."),
         ("Esqueci o Esc","Se as bolinhas pretas ainda estão na tela, aperte <span class=ui>Esc</span> antes de agrupar.")]),

  dict(n=13, titulo="Outro Cilindro, ao lado: o pino", img="aula11/g11_depois.jpg", clipe="cilindro2.gif",
    corpo="Clique num lugar vazio do plano. Arraste <b>outro Cilindro laranja</b> e solte <b>no plano, à esquerda da placa</b>, fora dela.",
    ck="Tem um cilindro laranja no plano, à esquerda da placa furada.",
    sos=[("Soltei em cima da placa","Arraste-o de novo para o plano vazio, ao lado.")]),

  dict(n=14, titulo="Pino: 10 × 10 × 20, pelas alças", img="aula11/g12_depois.jpg", clipe="medidas_pino.gif",
    corpo="Pelas alças: <b>10</b> nos dois números da base (alça do canto) e <b>20</b> na altura (alça do meio da tampa).<br><br>O pino tem <b>10 mm</b> de diâmetro: <b>2 mm a menos</b> que o furo (12). Esses 2 mm viram <b>1 mm de folga</b> de cada lado (2 ÷ 2 = 1).",
    ck="O cilindro virou um pino fino e alto: um pouco mais fino que o furo.",
    sos=[("O número ficou estranho","Clique no número, aperte Ctrl + A (no Mac, Cmd + A) e escreva de novo."),
         ("Os números sumiram","Clique no cilindro e na alça do canto de novo.")]),

  dict(n=15, titulo="Escolha a placa e o pino: clique e Shift + clique", img="aula11/g14_depois.jpg", clipe="duas.gif",
    corpo="Clique num lugar vazio. Clique <b>na placa</b> (no vermelho) e, segurando <span class=ui>Shift</span>, clique <b>no pino</b>.<br><br>O painel diz <span class=ui>Shapes(2)</span>: a placa e o pino.",
    ck="A placa e o pino têm contorno azul, e o painel diz <span class=ui>Shapes(2)</span>.",
    sos=[("O painel diz outra coisa","Clique num lugar vazio e refaça: primeiro a placa, depois Shift + clique no pino.")]),

  dict(n=16, titulo="Abra o Alinhar e fixe a placa", img="aula11/g15_depois.jpg", clipe="alinhar2.gif",
    corpo="Na barra de cima, clique no botão <span class=ui>Alinhar</span>. Depois clique <b>na placa</b>: ela fica fixa, e só o pino vai andar.",
    ck="Apareceram as bolinhas pretas, e a placa foi clicada.",
    sos=[("As bolinhas não apareceram","Você precisa de duas peças selecionadas. Volte ao passo 15.")]),

  dict(n=17, titulo="Pino: centro em X, a bolinha do meio embaixo", img="aula11/g16_depois.jpg", clipe="alinha_x2.gif",
    corpo="Clique na <b>bolinha do meio</b> da fileira de <b>baixo</b>. O pino vai para o meio da placa, da esquerda para a direita.",
    ck="O pino ficou na mesma coluna do furo.",
    sos=[("A placa andou","Você não fixou a placa. Aperte Ctrl + Z e refaça o passo 16.")]),

  dict(n=18, titulo="Pino: centro em Y — ele encaixa", img="aula11/g17_depois.jpg", clipe="alinha_y2.gif",
    corpo="Clique na <b>bolinha do meio</b> da coluna da <b>esquerda</b>. O pino <b>desce dentro do furo</b>: ele <b>encaixou</b>. Aperte <span class=ui>Esc</span> para fechar o Alinhar.",
    ck="O pino está dentro do furo da placa, no meio, e o Alinhar já pode fechar.",
    sos=[("O pino não entrou","Faltou um dos alinhamentos: o do meio de baixo (passo 17) e o do meio da esquerda (este).")]),

  dict(n=19, titulo="Olhe de cima: a folga", img="aula11/g18_depois.jpg", clipe="vista_cima.gif",
    corpo="Clique num lugar vazio do plano. No <b>cubo</b> de vistas, no canto de cima à esquerda, clique na face escrita <span class=ui>SUPERIOR</span>.<br><br>De cima se vê a placa vermelha com um círculo laranja no meio — o pino — e, em volta dele, um <b>anel fininho</b> onde se enxerga o chão: é a <b>folga</b> de 1 mm. Se o pino tivesse o mesmo tamanho do furo, <b>não haveria anel</b>.",
    ck="De cima: o pino laranja no meio da placa vermelha, com um <b>anel fininho</b> em volta dele (é bem fino: aproxime com o <b>+</b> para enxergar melhor).",
    sos=[("Não vejo anel","Aproxime a câmera com o <b>+</b> da barra da esquerda. Se mesmo assim o pino encosta na placa, ele tem o mesmo diâmetro do furo: volte ao passo 14 e confira o 10."),
         ("A câmera não mudou","Clique <b>na palavra</b> SUPERIOR do cubinho.")]),

  dict(n=20, titulo="Dê um nome ao seu projeto", img="aula11/g19_depois.jpg", clipe="batiza.gif",
    corpo="Clique na <b>casinha</b> da barra da esquerda para voltar à vista inicial. Depois clique no <b>nome do projeto</b>, no canto de cima à esquerda, apague, escreva <b>Encaixe da ANA</b> (ou o seu nome) e aperte <span class=ui>Enter</span>.<br><br>O Tinkercad salva sozinho. As peças estão guardadas na sua conta.",
    ck="No canto de cima à esquerda aparece o <b>nome que você escreveu</b>.",
    sos=[("O nome não mudou","Falta o <span class=ui>Enter</span>."),
         ("O campo não abriu","Clique <b>em cima das letras</b> do nome.")]),
 ],
}
for i, p in enumerate(AULA["passos"], 1):
    p["n"] = i
