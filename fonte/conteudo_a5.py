# -*- coding: utf-8 -*-
"""Aula 5 — Carrinho: quatro rodas iguais com Ctrl + D (duplicar).

Medido na bancada (fonte/cap5.py). Pegadinhas:
  · o Ctrl + D NÃO muda nada na tela: a cópia nasce em cima da original — por
    isso ele e o empurrão com Shift + seta são um passo só (passo 14);
  · duplicar um PAR: a cópia nasce e dá para empurrar as duas juntas (passo 16);
  · só a seta curva de CIMA é preciso para pôr a roda em pé: o eixo fica de
    um lado a outro do carro (passo 6).
"""

AULA = {
 "n": 5,
 "slug": "aula5",
 "titulo": "Carrinho",
 "subtitulo": "Um corpo, uma roda e Ctrl + D: a roda vira quatro, e o carrinho está pronto.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 5 · duplicar",
 "fim": "Acabou a Aula 5. Você fez um <b>carrinho</b> com <b>quatro rodas iguais</b> modelando só <b>uma</b>: o truque é o <b>Ctrl + D</b>, que duplica o que está selecionado — uma roda virou duas, e as duas viraram quatro, copiando o <b>par</b> de uma vez. Quando uma peça aparece várias vezes, faça uma e duplique. A peça está salva na sua conta com o nome que você deu.",
 "avisos": [
   ("Projeto novo", "Esta aula começa num projeto novo, vazio. As peças das aulas anteriores continuam guardadas na sua conta."),
   ("Milímetros", "Todo número é em milímetro. O carrinho tem <b>60 mm</b> de comprido: o tamanho de um ovo de galinha."),
   ("Setas do teclado", "<b>Shift + seta</b> anda a peça selecionada <b>10 mm</b>; a seta sozinha anda <b>1 mm</b>. Hoje isso faz as rodas chegarem ao lugar certo."),
   ("Os clipes", "Os passos com animação mostram o gesto inteiro: o mouse andando, o <b>botão certo acendendo</b> e as <b>teclas acesas</b> quando o gesto é de teclado."),
   ("Travou?", "Todo passo tem um quadro laranja embaixo com o conserto dos erros mais comuns."),
 ],
 "passos": [

  dict(n=1, titulo="Abra o Tinkercad e crie um Projeto 3D", img="aula5/p01_vazio.jpg", clipe="criar.gif",
    corpo="Entre no Tinkercad com a sua conta. No canto de cima à direita, clique em <span class=ui>+ Criar</span> e, na primeira linha, em <span class=ui>Projeto 3D</span>.<br><br>Abre o editor com o plano azul quadriculado <b>vazio</b> e um nome sorteado — deixe assim, no último passo você troca.",
    ck="O editor abriu com o plano azul claro quadriculado vazio.",
    sos=[("Não sei entrar","Chame o professor. Não crie conta nova: os seus projetos estão na antiga."),
         ("Abriu outra coisa","Volte com a seta ⟵ do navegador e clique de novo em <span class=ui>+ Criar</span>, escolhendo a primeira linha."),
         ("A tela ficou branca","O Tinkercad é pesado. Espere até meio minuto. Se continuar branca, recarregue com <span class=ui>F5</span>.")]),

  dict(n=2, titulo="Arraste uma Caixa para o plano", img="aula5/g02_depois.jpg", clipe="caixa.gif",
    corpo="Na coluna da direita, a forma <b>vermelha</b> do meio da segunda fileira, à esquerda, é a <span class=ui>Caixa</span>. Segure o botão esquerdo nela, <b>arraste até o meio do plano</b> e solte.<br><br>É o <b>corpo</b> do carrinho.",
    ck="Tem um cubo vermelho no meio do plano e o painel branco escrito <span class=ui>Caixa</span> no alto.",
    sos=[("Peguei a caixa cinza listrada","Essa é o <b>buraco</b>. Aperte <span class=ui>Delete</span> e arraste a vermelha, a da segunda fileira.")]),

  dict(n=3, titulo="Comprimento 60, Largura 30, Altura 16", img="aula5/g03_depois.jpg", clipe="medidas_carro.gif",
    corpo="No painel, escreva <b>60</b> no campo <span class=ui>Comprimento</span>, <b>30</b> em <span class=ui>Largura</span> e <b>16</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada).<br><br>O carro é <b>comprido para a frente</b> (o comprimento é a profundidade, para dentro da tela) e as rodas vão ficar dos lados.",
    ck="A caixa virou um bloco <b>comprido e baixo</b>, mais fundo que largo.",
    sos=[("O carro ficou largo e curto","Os números trocaram de lugar: o <b>60</b> tem de estar em <span class=ui>Comprimento</span> e o <b>30</b> em <span class=ui>Largura</span>."),
         ("Digitei e nada mudou","Falta o <span class=ui>Enter</span> depois de cada número.")]),

  dict(n=4, titulo="Arraste um Cilindro para a esquerda", img="aula5/g04_depois.jpg", clipe="cilindro.gif",
    corpo="Na coluna da direita, a forma <b>laranja</b> do meio da segunda fileira é o <span class=ui>Cilindro</span>. Arraste-o e solte <b>no plano, à esquerda do carro</b> — fora dele.<br><br>É a <b>roda</b>.",
    ck="Tem um cilindro laranja no plano, ao lado esquerdo do carro, e o painel diz <span class=ui>Cilindro</span>.",
    sos=[("Peguei o cilindro cinza listrado","Esse é o <b>buraco</b>. Aperte <span class=ui>Delete</span> e arraste o laranja."),
         ("Soltei em cima do carro","Arraste-o de novo para o plano vazio, ao lado.")]),

  dict(n=5, titulo="Roda 20 × 20 × 6, pelas alças", img="aula5/g05_depois.jpg", clipe="medidas_roda.gif",
    corpo="O cilindro não tem campo de medida (Aula 2): use as <b>alças</b>. Clique na <b>alça do canto</b> de cima à esquerda; no número da <b>esquerda</b> escreva <b>20</b> e <span class=ui>Enter</span>, no de <b>cima</b> escreva <b>20</b> e <span class=ui>Enter</span>. Depois clique na alça do <b>meio da tampa</b> e escreva <b>6</b> no número da altura.<br><br>A roda é um disco de 20 mm de diâmetro e <b>6 mm de grossura</b>.",
    ck="O cilindro virou um disco achatado, e os números mostram 20, 20 e 6.",
    sos=[("O número ficou estranho","Clique no número, aperte Ctrl + A (no Mac, Cmd + A) e escreva de novo."),
         ("Os números sumiram","Clique no cilindro e na alça do canto de novo.")]),

  dict(n=6, titulo="Ponha a roda em pé: a seta curva de cima", img="aula5/g06_depois.jpg", clipe="gira.gif",
    corpo="Clique na própria roda para soltar a alça que ficou ativa. Acima dela há uma <b>seta curva</b> pequena. Segure o botão esquerdo nela e <b>arraste devagar</b> para a direita e para baixo.<br><br>Aparece o <b>transferidor</b> colorido. Arraste <b>até o número mostrar 90°</b> (pode ser −90°) e solte.<br><br>O disco <b>levanta</b>: agora é uma roda em pé, de lado, como a de um carro.",
    ck="A roda está <b>em pé</b>, fininha vista de frente, e o transferidor mostrou 90° (ou −90°).",
    sos=[("O transferidor não mexe","Clique na roda antes e tente de novo, segurando a seta curva <b>de cima</b>."),
         ("Passou de 90","Volte um pouquinho sem soltar, até o número certo.")]),

  dict(n=7, titulo="Selecione tudo: Ctrl + A", img="aula5/g07_depois.jpg", clipe="seleciona.gif",
    corpo="Clique num <b>lugar vazio</b> do plano, segure <span class=ui>Ctrl</span> e aperte <span class=ui>A</span> (no Mac, <span class=ui>Cmd</span> + <span class=ui>A</span>). O carro e a roda ficam selecionados: <span class=ui>Shapes(2)</span>.",
    ck="O carro e a roda têm contorno azul, e o painel diz <span class=ui>Shapes(2)</span>.",
    sos=[("Selecionou só um","Clique num lugar vazio do plano e aperte Ctrl + A de novo.")]),

  dict(n=8, titulo="Abra o Alinhar", img="aula5/g08_depois.jpg", clipe="alinhar.gif",
    corpo="Na barra de cima, clique no botão <span class=ui>Alinhar</span> (o ícone de linhas de tamanhos diferentes, ao lado do espelho). Aparecem as bolinhas pretas.",
    ck="Apareceram as bolinhas pretas em volta do carro e da roda.",
    sos=[("As bolinhas não apareceram","O Alinhar só abre com <b>duas ou mais</b> peças selecionadas. Volte ao passo 7.")]),

  dict(n=9, titulo="FIXE o carro: clique nele", img="aula5/g09_depois.jpg", clipe="fixa.gif",
    corpo="Clique <b>no corpo vermelho do carro</b>: ele fica <b>fixo</b> e só a roda vai andar quando você clicar nas bolinhas.",
    ck="O carro foi clicado e as bolinhas continuam na tela.",
    sos=[("A seleção sumiu","Você clicou fora do carro. Aperte Ctrl + Z, abra o Alinhar de novo e clique <b>em cima do vermelho</b>.")]),

  dict(n=10, titulo="Centro em Y: a bolinha do meio, à esquerda", img="aula5/g10_depois.jpg", clipe="alinha_y.gif",
    corpo="Clique na <b>bolinha do meio</b> da coluna da <b>esquerda</b>. A roda passa para a mesma linha do carro, <b>de frente para trás</b>.",
    ck="A roda andou e ficou na altura do meio do carro, de frente para trás.",
    sos=[("As bolinhas mudaram de lugar","É normal: depois de cada clique elas se reposicionam. Procure de novo.")]),

  dict(n=11, titulo="Centro em Z: a bolinha do meio, à direita", img="aula5/g11_depois.jpg", clipe="alinha_z.gif",
    corpo="Clique na <b>bolinha do meio</b> da coluna da <b>direita</b>. A roda <b>sobe</b> até o meio da altura do carro.",
    ck="A roda subiu e ficou na altura do carro.",
    sos=[("Não vejo a bolinha","São três bolinhas pertinho uma da outra, à direita do carro. Aproxime a câmera com o <b>+</b> da barra da esquerda.")]),

  dict(n=12, titulo="Centro em X: a bolinha do meio, embaixo", img="aula5/g12_depois.jpg", clipe="alinha_x.gif",
    corpo="Clique na <b>bolinha do meio</b> da fileira de <b>baixo</b>. A roda vai para o <b>meio do carro</b> e some lá dentro. No próximo passo você a tira de lá.",
    ck="A roda sumiu para dentro do carro; o contorno azul continua em volta.",
    sos=[("O carro andou","Você não fixou o carro no passo 9. Aperte Ctrl + Z três vezes e refaça.")]),

  dict(n=13, titulo="Esc e Shift + clique: só a roda", img="aula5/g13_depois.jpg", clipe="so_a_roda.gif",
    corpo="Aperte <span class=ui>Esc</span> (o Alinhar fecha e as duas peças continuam selecionadas). Segure <span class=ui>Shift</span> e <b>clique no carro</b>: o Shift tira o carro da seleção.<br><br>O painel passa a dizer <span class=ui>Cilindro</span>: só a roda está selecionada, escondida dentro do carro.",
    ck="O painel diz <span class=ui>Cilindro</span> (e não <span class=ui>Shapes(2)</span>).",
    sos=[("O painel ainda diz Shapes(2)","O clique não pegou no carro. Segure o Shift e clique bem no meio do corpo."),
         ("Desmarcou tudo","Você soltou o Shift antes do clique. Aperte Ctrl + A e refaça.")]),

  dict(n=14, titulo="Empurre a roda: Shift + ←, e Shift + ↓", img="aula5/g14_depois.jpg", clipe="empurra.gif",
    corpo="Com só a roda selecionada, segure <span class=ui>Shift</span> e aperte a <b>seta para a esquerda</b> <span class=ui>←</span> <b>uma vez</b> (10 mm); depois, <b>sem o Shift</b>, aperte <span class=ui>←</span> <b>sete vezes</b> (1 mm cada): são 17 mm. A roda sai do carro pela esquerda e <b>encosta</b> nele.<br><br>Agora segure <span class=ui>Shift</span> e aperte a <b>seta para baixo</b> <span class=ui>↓</span> <b>duas vezes</b>: 20 mm para a frente. A roda fica na <b>frente</b> do carro, do lado esquerdo.",
    ck="A roda está do <b>lado esquerdo</b>, na <b>frente</b> do carro, encostada nele.",
    sos=[("A roda foi demais","Cada Shift + seta é 10 mm e cada seta sozinha é 1 mm. Volte com a seta contrária."),
         ("A seta mexeu a câmera","A roda não estava selecionada. Volte ao passo 13."),
         ("A roda não anda","Clique uma vez num lugar vazio do plano, selecione só a roda e tente de novo.")]),

  dict(n=15, titulo="Ctrl + D e empurre a cópia para a direita", img="aula5/g16_depois.jpg", clipe="duplica.gif",
    corpo="Aperte <span class=ui>Ctrl</span> + <span class=ui>D</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>D</span>). <b>Nada muda na tela</b>: nasceu uma <b>cópia</b> da roda, em cima da original, e é a cópia que fica selecionada.<br><br>Agora empurre a cópia: <span class=ui>Shift</span> + <span class=ui>→</span> <b>três vezes</b> e <span class=ui>→</span> <b>quatro vezes</b> (34 mm). Ela atravessa o carro e para <b>do lado direito</b>, também na frente.",
    ck="Tem uma roda em cada lado do carro, na frente, e a roda da direita está selecionada.",
    sos=[("Não nasceu cópia","O atalho só vale com a roda selecionada. Clique nela e aperte Ctrl + D de novo."),
         ("Nasceram duas cópias","Aperte Ctrl + Z uma vez e confira.")]),

  dict(n=16, titulo="Escolha as duas rodas", img="aula5/g17_depois.jpg", clipe="duas_rodas.gif",
    corpo="Clique num lugar vazio do plano. Clique na roda da <b>esquerda</b> e, segurando <span class=ui>Shift</span>, clique na roda da <b>direita</b>.<br><br>O painel diz <span class=ui>Shapes(2)</span>: as duas rodas da frente estão selecionadas, o carro não.",
    ck="As duas rodas têm contorno azul, e o painel diz <span class=ui>Shapes(2)</span>.",
    sos=[("Selecionou o carro também","Você clicou nele. Refaça só nas rodas."),
         ("Só uma ficou selecionada","Segure o <span class=ui>Shift</span> até clicar na segunda roda.")]),

  dict(n=17, titulo="Ctrl + D no par e Shift + ↑", img="aula5/g18_depois.jpg", clipe="duplica_par.gif",
    corpo="Aperte <span class=ui>Ctrl</span> + <span class=ui>D</span>: o <b>par inteiro</b> foi copiado. Agora segure <span class=ui>Shift</span> e aperte <span class=ui>↑</span> <b>quatro vezes</b>: 40 mm para <b>trás</b>.<br><br>O par novo vai para a parte de trás do carro. São <b>quatro rodas</b>, e você modelou só uma.",
    ck="O carro tem quatro rodas: duas na frente e duas atrás.",
    sos=[("Só apareceu uma roda atrás","Você copiou uma roda só. Aperte Ctrl + Z duas vezes e refaça a partir do passo 16."),
         ("As rodas de trás ficaram desencontradas","Cada Shift + ↑ é 10 mm. Conte quatro toques.")]),

  dict(n=18, titulo="Selecione tudo e agrupe: Grupo de união", img="aula5/g19_depois.jpg", clipe="uniao.gif",
    corpo="Clique num lugar vazio, aperte <span class=ui>Ctrl</span> + <span class=ui>A</span> e, na barra de cima, clique no do <b>meio</b> dos três botõezinhos de juntar, o <span class=ui>Grupo de união</span>.<br><br>O carro e as quatro rodas viram <b>uma peça só</b>, de uma cor: o painel diz <span class=ui>Union</span>.",
    ck="O painel diz <span class=ui>Union</span> e o carrinho é uma peça só, toda vermelha.",
    sos=[("O painel diz Shapes(5)","O agrupar não pegou: clique no botão do meio dos três."),
         ("Sumiu uma roda","A roda estava solta no ar. Desagrupe com Ctrl + Shift + G e confira se ela encosta no carro.")]),

  dict(n=19, titulo="Olhe de cima: as quatro rodas", img="aula5/g20_depois.jpg", clipe="vista_cima.gif",
    corpo="Clique num lugar vazio. No cubo de vistas, no canto de cima à esquerda, clique na face escrita <span class=ui>SUPERIOR</span>.<br><br>De cima se vê o <b>corpo</b> e as <b>quatro rodas</b> aparecendo nos cantos, duas de cada lado.",
    ck="De cima: o corpo comprido e quatro rodinhas saindo pelos lados, nos cantos.",
    sos=[("A câmera não mudou","Clique <b>na palavra</b> SUPERIOR do cubinho."),
         ("Só vejo duas rodas","As de trás ficaram no mesmo lugar das da frente. Volte ao passo 17.")]),

  dict(n=20, titulo="Dê um nome ao seu projeto", img="aula5/g21_depois.jpg", clipe="batiza.gif",
    corpo="Clique na <b>casinha</b> da barra da esquerda para voltar à vista inicial. Depois clique no <b>nome do projeto</b>, no canto de cima à esquerda, apague, escreva <b>Carrinho da ANA</b> (ou o seu nome) e aperte <span class=ui>Enter</span>.<br><br>O Tinkercad salva sozinho. O carrinho está guardado na sua conta.",
    ck="No canto de cima à esquerda aparece o <b>nome que você escreveu</b>.",
    sos=[("O nome não mudou","Falta o <span class=ui>Enter</span>."),
         ("O campo não abriu","Clique <b>em cima das letras</b> do nome.")]),
 ],
}
