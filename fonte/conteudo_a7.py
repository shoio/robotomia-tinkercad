# -*- coding: utf-8 -*-
"""Aula 7 — Robô de formas: cores, formas soltas na FACE de outra e o que agrupar faz com a cor.

Medido na bancada (fonte/cap7.py). Pegadinhas:
  · a paleta abre ancorada na bolinha de cor e fica ABERTA: cobre as alças; um
    segundo clique na bolinha a fecha (Esc não fecha);
  · uma forma solta na FACE da frente de outra nasce ali (o plano verde fica
    de pé) — assim nascem os olhos, sem número nenhum;
  · pelos CAMPOS do painel a caixa cresce do centro: a cabeça já fica centrada
    no corpo (as alças, não: foi a telhado da Aula 4);
  · agrupar (união) apaga as cores: tudo vira uma cor só — e Ctrl + Z devolve.
"""

AULA = {
 "n": 7,
 "slug": "aula7",
 "titulo": "Robô de formas",
 "subtitulo": "Caixas, esferas e um cone viram um robô — e cada peça ganha a sua cor.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 7 · cores",
 "fim": "Acabou a Aula 7. Você montou um <b>robô</b> de formas e <b>pintou cada peça</b> com a paleta. Aprendeu que uma forma solta <b>na face</b> de outra nasce ali (os olhos) e que o <b>Grupo de união apaga as cores</b>: tudo vira uma cor só. Por isso o robô ficou <b>solto</b>, peça por peça. A peça está salva na sua conta com o nome que você deu.",
 "avisos": [
   ("Projeto novo", "Esta aula começa num projeto novo, vazio. As peças das aulas anteriores continuam guardadas na sua conta."),
   ("Milímetros", "O robô tem <b>80 mm</b> de largura: um pouco menos que uma mão."),
   ("Cores", "A paleta fica numa <b>bolinha de cor</b> no painel da peça. Ela abre uma janela que <b>cobre</b> parte da tela: feche-a clicando de novo na bolinha."),
   ("Os clipes", "Os passos com animação mostram o gesto inteiro: o mouse andando, o <b>botão certo acendendo</b> e as <b>teclas acesas</b> quando o gesto é de teclado."),
   ("Travou?", "Todo passo tem um quadro laranja embaixo com o conserto dos erros mais comuns."),
 ],
 "passos": [

  dict(n=1, titulo="Abra o Tinkercad e crie um Projeto 3D", img="aula7/p01_vazio.jpg", clipe="criar.gif",
    corpo="Entre no Tinkercad com a sua conta. No canto de cima à direita, clique em <span class=ui>+ Criar</span> e, na primeira linha, em <span class=ui>Projeto 3D</span>.<br><br>Abre o editor com o plano azul quadriculado <b>vazio</b> e um nome sorteado — deixe assim, no último passo você troca.",
    ck="O editor abriu com o plano azul claro quadriculado vazio.",
    sos=[("Não sei entrar","Chame o professor. Não crie conta nova: os seus projetos estão na antiga."),
         ("Abriu outra coisa","Volte com a seta ⟵ do navegador e clique de novo em <span class=ui>+ Criar</span>, escolhendo a primeira linha."),
         ("A tela ficou branca","O Tinkercad é pesado. Espere até meio minuto. Se continuar branca, recarregue com <span class=ui>F5</span>.")]),

  dict(n=2, titulo="Arraste uma Caixa para o plano: o corpo", img="aula7/g02_depois.jpg", clipe="caixa.gif",
    corpo="Na coluna da direita, a forma <b>vermelha</b> do meio da segunda fileira, à esquerda, é a <span class=ui>Caixa</span>. Segure o botão esquerdo nela, <b>arraste até o meio do plano</b> e solte.<br><br>É o <b>corpo</b> do robô.",
    ck="Tem um cubo vermelho no meio do plano e o painel branco escrito <span class=ui>Caixa</span> no alto.",
    sos=[("Peguei a caixa cinza listrada","Essa é o <b>buraco</b>. Aperte <span class=ui>Delete</span> e arraste a vermelha.")]),

  dict(n=3, titulo="Corpo: Comprimento 40, Largura 80, Altura 36", img="aula7/g03_depois.jpg", clipe="medidas_corpo.gif",
    corpo="No painel, escreva <b>40</b> em <span class=ui>Comprimento</span>, <b>80</b> em <span class=ui>Largura</span> e <b>36</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada).<br><br>O corpo fica <b>largo</b>: o número grande vai em <span class=ui>Largura</span>.",
    ck="A caixa virou um bloco largo e baixo, de frente para você.",
    sos=[("O bloco ficou fundo e estreito","O 80 foi parar em <span class=ui>Comprimento</span>. Troque os dois números."),
         ("Digitei e nada mudou","Falta o <span class=ui>Enter</span> depois de cada número.")]),

  dict(n=4, titulo="Abra a paleta: clique na bolinha de cor", img="aula7/g04_depois.jpg", clipe="paleta.gif",
    corpo="No painel branco do alto, clique na <b>bolinha vermelha</b> ao lado da palavra <span class=ui>Sólido</span>.<br><br>Abre a janela <span class=ui>Cores sólidas</span>, com <b>três fileiras</b> de bolinhas: a de cima é de cores <b>claras</b>, a do meio é a cor <b>normal</b> e a de baixo é <b>escura</b>. A janela cobre parte do plano.",
    ck="Abriu a janela <span class=ui>Cores sólidas</span> com três fileiras de bolinhas coloridas.",
    sos=[("Não abriu nada","Clique <b>na bolinha colorida</b>, e não na palavra <span class=ui>Sólido</span>. A peça precisa estar selecionada."),
         ("Cliquei em Orifício","Aí a peça virou buraco. Clique em <span class=ui>Sólido</span> para voltar e abra a paleta de novo.")]),

  dict(n=5, titulo="Escolha o azul", img="aula7/g05_depois.jpg", clipe="azul.gif",
    corpo="Na fileira do <b>meio</b>, clique na bolinha <b>azul</b> (a sétima da esquerda para a direita, depois do azul-claro).<br><br>O corpo do robô fica <b>azul</b>. Depois, <b>clique de novo na bolinha de cor</b> do painel para fechar a janela — ela tapa as alças.",
    ck="O corpo está azul, e a bolinha do painel também ficou azul.",
    sos=[("Ficou azul-claro","Você pegou a bolinha da fileira de cima. A normal é a do <b>meio</b>."),
         ("A janela não fecha","Clique na bolinha de cor do painel de novo. O Esc não fecha essa janela.")]),

  dict(n=6, titulo="Outra Caixa na tampa do corpo: a cabeça", img="aula7/g06_depois.jpg", clipe="caixa_cabeca.gif",
    corpo="Clique num <b>lugar vazio</b> do plano para soltar a seleção. Arraste <b>outra Caixa vermelha</b> e solte <b>bem no meio da tampa</b> do corpo.<br><br>A caixa nasce <b>em cima</b> do corpo, e aparece o <b>quadrado verde</b> (o plano de trabalho foi para o alto da peça).",
    ck="Tem uma caixa vermelha pousada em cima do corpo azul, com o quadrado verde em volta.",
    sos=[("A caixa caiu no chão","Você soltou fora do corpo. Arraste de novo para o meio da <b>tampa</b>.")]),

  dict(n=7, titulo="Cabeça: Comprimento 36, Largura 70, Altura 30", img="aula7/g07_depois.jpg", clipe="medidas_cabeca.gif",
    corpo="No painel, escreva <b>36</b> em <span class=ui>Comprimento</span>, <b>70</b> em <span class=ui>Largura</span> e <b>30</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada).<br><br>A cabeça é <b>um pouco menor</b> que o corpo. Pelos campos do painel a caixa cresce <b>a partir do centro</b>: ela continua centrada em cima do corpo.",
    ck="A cabeça ficou um pouco menor que o corpo, centrada em cima dele.",
    sos=[("A cabeça saiu torta","Confira os números: 36, 70 e 30, cada um no seu campo.")]),

  dict(n=8, titulo="Pinte a cabeça de cinza-claro", img="aula7/g08_depois.jpg", clipe="cinza.gif",
    corpo="Com a cabeça selecionada, clique na <b>bolinha de cor</b> do painel. Na fileira do <b>meio</b>, clique na bolinha <b>cinza bem clara</b> (a penúltima, à direita).<br><br>A cabeça fica cinza-claro. Clique de novo na bolinha de cor do painel para fechar a janela.",
    ck="A cabeça está cinza-claro, em cima do corpo azul.",
    sos=[("Ficou cinza-escuro","Você pegou a última bolinha. A cinza bem clara é a <b>penúltima</b> da fileira do meio."),
         ("Pintei o corpo","Você estava com o corpo selecionado. Clique na cabeça e pinte de novo.")]),

  dict(n=9, titulo="Solte a Esfera na FACE da frente da cabeça", img="aula7/g13_depois.jpg", clipe="olho.gif",
    corpo="Clique num lugar vazio do plano. Na coluna da direita, a <b>bola azul</b> do canto direito da segunda fileira é a <span class=ui>Esfera</span>. Segure o botão esquerdo nela e <b>solte em cima da frente da cabeça</b>, um pouco para a esquerda do meio — na parede da frente, e não na tampa.<br><br>O <b>quadrado verde</b> fica de pé, colado na parede: a esfera <b>nasce ali</b>, saindo da parede como um olho.",
    ck="A esfera azul está colada na frente da cabeça, do lado esquerdo, e o quadrado verde está de pé.",
    sos=[("A esfera caiu no chão","Você soltou fora da cabeça. Arraste de novo, soltando em cima da <b>parede da frente</b>."),
         ("A esfera foi para a tampa","Você soltou na parte de cima. Solte mais para baixo, na frente da cabeça."),
         ("O olho ficou no corpo azul","Solte mais para cima: o meio da cabeça, e não a beirada de baixo.")]),

  dict(n=10, titulo="Pinte o olho de amarelo", img="aula7/g14_depois.jpg", clipe="amarelo.gif",
    corpo="Com a esfera selecionada, clique na <b>bolinha de cor</b> do painel e, na fileira do meio, na bolinha <b>amarela</b> (a terceira). Clique de novo na bolinha de cor para fechar a janela.",
    ck="O olho está amarelo.",
    sos=[("Ficou laranja","A amarela é a <b>terceira</b> da fileira do meio, a laranja é a segunda.")]),

  dict(n=11, titulo="Ctrl + D: o segundo olho", img="aula7/g15_depois.jpg", clipe="duplica.gif",
    corpo="Com o olho selecionado, aperte <span class=ui>Ctrl</span> + <span class=ui>D</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>D</span>): nasce uma <b>cópia</b> em cima dele.<br><br>Agora empurre a cópia para a direita: <span class=ui>Shift</span> + <span class=ui>→</span> <b>três vezes</b> e <span class=ui>→</span> <b>uma vez</b> (31 mm). Os dois olhos ficam lado a lado, os dois amarelos: <b>a cópia leva a cor</b>.",
    ck="A cabeça tem <b>dois olhos amarelos</b>, lado a lado.",
    sos=[("O olho foi demais","Cada Shift + seta é 10 mm e cada seta sozinha é 1 mm. Volte com a seta contrária."),
         ("Os olhos ficaram um em cima do outro","O Ctrl + D copiou, mas faltou empurrar. Aperte Shift + → três vezes.")]),

  dict(n=12, titulo="Solte o Cone na tampa da cabeça", img="aula7/g15b_depois.jpg", clipe="cone.gif",
    corpo="Clique num lugar vazio do plano. Na coluna da direita, na fileira da pirâmide, o <b>cone roxo</b>. Solte-o <b>no meio da tampa</b> da cabeça.<br><br>O cone nasce em cima: é o <b>chapéu</b> do robô.",
    ck="Um cone roxo está em cima da cabeça, no meio.",
    sos=[("O cone caiu no chão","Você soltou fora da cabeça. Arraste de novo para a <b>tampa</b>.")]),

  dict(n=13, titulo="Pinte o chapéu de vermelho", img="aula7/g15c_depois.jpg", clipe="vermelho.gif",
    corpo="Com o cone selecionado, clique na <b>bolinha de cor</b> do painel e, na fileira do meio, na bolinha <b>vermelha</b> (a primeira da esquerda). Clique de novo na bolinha de cor para fechar a janela.",
    ck="O chapéu está vermelho.",
    sos=[("Ficou rosa","A vermelha é a <b>primeira</b> bolinha da fileira do meio, a rosa fica mais à direita.")]),

  dict(n=14, titulo="Gire a câmera com o botão direito", img="aula7/g15d_depois.jpg", clipe="girar.gif",
    corpo="Clique num lugar vazio. Segure o botão <b>direito</b> do mouse em cima do <b>plano de trabalho</b> e arraste um pouco para a direita e para cima.<br><br>A câmera <b>gira</b> e dá para ver o robô de outro lado: os olhos saem da parede da cabeça como bolinhas. Os olhos são <b>esferas inteiras</b>, não buracos.",
    ck="A câmera mudou: dá para ver o robô de lado, com os olhos saindo da cabeça.",
    sos=[("A peça saiu do lugar","Você usou o botão <b>esquerdo</b>. Aperte Ctrl + Z e repita com o <b>direito</b>."),
         ("A câmera foi longe","Use a casinha da barra da esquerda para voltar à vista inicial.")]),

  dict(n=15, titulo="Olhe de frente: o robô", img="aula7/g16_depois.jpg", clipe="vista_frente.gif",
    corpo="No canto de cima à esquerda, no <b>cubo</b> de vistas, clique na face escrita <span class=ui>FRONTAL</span>.<br><br>De frente se vê o robô: corpo azul, cabeça cinza, dois olhos amarelos e o chapéu vermelho.",
    ck="De frente se vê o corpo azul, a cabeça cinza, os dois olhos amarelos e o chapéu vermelho.",
    sos=[("A câmera não mudou","Clique <b>na palavra</b> FRONTAL do cubinho.")]),

  dict(n=16, titulo="Selecione tudo: Ctrl + A", img="aula7/g17a_depois.jpg", clipe="seleciona.gif",
    corpo="Clique na <b>casinha</b> da barra da esquerda para voltar à vista inicial. Clique num lugar vazio e aperte <span class=ui>Ctrl</span> + <span class=ui>A</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>A</span>).<br><br>Todas as peças ficam selecionadas, com contorno azul: o painel diz <span class=ui>Shapes(5)</span>.",
    ck="O robô inteiro tem contorno azul, e o painel diz <span class=ui>Shapes(5)</span>.",
    sos=[("O painel diz outro número","Conte: corpo, cabeça, dois olhos e chapéu são cinco peças. Se faltar uma, clique num lugar vazio e refaça.")]),

  dict(n=17, titulo="Agrupe: veja a cor sumir", img="aula7/g17_depois.jpg", clipe="uniao.gif",
    corpo="Na barra de cima, clique no do <b>meio</b> dos três botõezinhos de juntar, o <span class=ui>Grupo de união</span>.<br><br>As cinco peças viram <b>uma só</b>, e agora <b>tudo fica de uma cor só</b>, azul: o <b>Grupo de união apaga as cores</b>. Só vale agrupar quando a peça é de uma cor só — como nas aulas anteriores.",
    ck="O robô virou uma peça só, toda azul, e o painel diz <span class=ui>Union</span>.",
    sos=[("O painel não mudou","Clique no botão do meio dos três, o <span class=ui>Grupo de união</span>.")]),

  dict(n=18, titulo="Desfaça: Ctrl + Z", img="aula7/g18_depois.jpg", clipe="desfaz.gif",
    corpo="Aperte <span class=ui>Ctrl</span> + <span class=ui>Z</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>Z</span>): o agrupar é <b>desfeito</b> e as <b>cores voltam</b>. O robô fica solto, peça por peça.<br><br>Por isso o robô colorido <b>não se agrupa</b>. Cor se escolhe peça a peça, antes de qualquer união.",
    ck="O robô voltou a ter as quatro cores: azul, cinza, amarelo e vermelho.",
    sos=[("Não voltou","Aperte Ctrl + Z mais uma vez, até o painel não dizer mais <span class=ui>Union</span>."),
         ("Voltou demais","Aperte Ctrl + Y (no Mac, Cmd + Shift + Z) para refazer um passo.")]),

  dict(n=19, titulo="Dê um nome ao seu projeto", img="aula7/g19_depois.jpg", clipe="batiza.gif",
    corpo="Clique na <b>casinha</b> da barra da esquerda para voltar à vista inicial. Depois clique no <b>nome do projeto</b>, no canto de cima à esquerda, apague, escreva <b>Robô da ANA</b> (ou o seu nome) e aperte <span class=ui>Enter</span>.<br><br>O Tinkercad salva sozinho. O robô está guardado na sua conta.",
    ck="No canto de cima à esquerda aparece o <b>nome que você escreveu</b>.",
    sos=[("O nome não mudou","Falta o <span class=ui>Enter</span>."),
         ("O campo não abriu","Clique <b>em cima das letras</b> do nome.")]),
 ],
}
