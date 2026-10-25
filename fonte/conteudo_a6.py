# -*- coding: utf-8 -*-
"""Aula 6 — Foguete: corpo, ponta (Cone) e aletas em cruz por duplicar e girar.

Medido na bancada (fonte/cap6.py). Pegadinhas:
  · o Cone solto na tampa do corpo já nasce CENTRADO (alinhar não muda nada);
  · a aleta é uma tira que ATRAVESSA o corpo: duas aletas numa Caixa só; a
    cópia, girada 90°, faz as outras duas (cruz de quatro);
  · a tira já nasce no chão (base z = 0): só precisa de X e Y;
  · aleta fina demais (3 mm) esconde as alças umas atrás das outras: 6 mm.
"""

AULA = {
 "n": 6,
 "slug": "aula6",
 "titulo": "Foguete",
 "subtitulo": "Um cilindro, uma ponta e quatro aletas: uma só tira, duplicada e girada, vira a cruz de baixo.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 6 · duplicar e girar",
 "fim": "Acabou a Aula 6. Você fez um <b>foguete</b>: corpo, ponta de <b>cone</b> e <b>quatro aletas</b>. O truque foi modelar uma tira só, que atravessa o corpo e já dá <b>duas</b> aletas, e depois <b>duplicar</b> (Ctrl + D) e <b>girar 90°</b> a cópia: a cruz está pronta. Quando as peças se repetem em volta de um eixo, faça uma e gire as cópias. O foguete está salvo na sua conta com o nome que você deu.",
 "avisos": [
   ("Projeto novo", "Esta aula começa num projeto novo, vazio. As peças das aulas anteriores continuam guardadas na sua conta."),
   ("Milímetros", "O foguete tem <b>70 mm</b> de altura: do tamanho de um pincel curto."),
   ("O que você já sabe", "Medidas pelas alças (Aula 2), Alinhar com uma peça fixa e Shift + clique (aulas 3 e 4), Ctrl + D e girar (Aula 5). Hoje eles se juntam."),
   ("Os clipes", "Os passos com animação mostram o gesto inteiro: o mouse andando, o <b>botão certo acendendo</b> e as <b>teclas acesas</b> quando o gesto é de teclado."),
   ("Travou?", "Todo passo tem um quadro laranja embaixo com o conserto dos erros mais comuns."),
 ],
 "passos": [

  dict(n=1, titulo="Abra o Tinkercad e crie um Projeto 3D", img="aula6/p01_vazio.jpg", clipe="criar.gif",
    corpo="Entre no Tinkercad com a sua conta. No canto de cima à direita, clique em <span class=ui>+ Criar</span> e, na primeira linha, em <span class=ui>Projeto 3D</span>.<br><br>Abre o editor com o plano azul quadriculado <b>vazio</b> e um nome sorteado — deixe assim, no último passo você troca.",
    ck="O editor abriu com o plano azul claro quadriculado vazio.",
    sos=[("Não sei entrar","Chame o professor. Não crie conta nova: os seus projetos estão na antiga."),
         ("Abriu outra coisa","Volte com a seta ⟵ do navegador e clique de novo em <span class=ui>+ Criar</span>, escolhendo a primeira linha."),
         ("A tela ficou branca","O Tinkercad é pesado. Espere até meio minuto. Se continuar branca, recarregue com <span class=ui>F5</span>.")]),

  dict(n=2, titulo="Arraste um Cilindro para o plano", img="aula6/g02_depois.jpg", clipe="cilindro.gif",
    corpo="Na coluna da direita, a forma <b>laranja</b> do meio da segunda fileira é o <span class=ui>Cilindro</span>. Arraste-a até o meio do plano e solte.<br><br>É o <b>corpo</b> do foguete.",
    ck="Tem um cilindro laranja no meio do plano e o painel diz <span class=ui>Cilindro</span>.",
    sos=[("Peguei o cilindro cinza listrado","Esse é o <b>buraco</b>. Aperte <span class=ui>Delete</span> e arraste o laranja.")]),

  dict(n=3, titulo="Corpo 20 × 20 × 50, pelas alças", img="aula6/g03_depois.jpg", clipe="medidas_corpo.gif",
    corpo="O cilindro não tem campo de medida (Aula 2): use as <b>alças</b>. Clique na <b>alça do canto</b> de cima à esquerda; no número da <b>esquerda</b> escreva <b>20</b> e <span class=ui>Enter</span>, no de <b>cima</b> escreva <b>20</b> e <span class=ui>Enter</span>. Depois clique na alça do <b>meio da tampa</b> e escreva <b>50</b> no número da altura.<br><br>O corpo fica fino e alto.",
    ck="O cilindro virou um tubo fino e alto, e os números mostram 20, 20 e 50.",
    sos=[("O número ficou estranho","Clique no número, aperte Ctrl + A (no Mac, Cmd + A) e escreva de novo."),
         ("Os números sumiram","Clique no cilindro e na alça do canto de novo.")]),

  dict(n=4, titulo="Solte o Cone na tampa do corpo", img="aula6/g04_depois.jpg", clipe="cone.gif",
    corpo="Na coluna da direita, na fileira da pirâmide, o <b>cone roxo</b> com o nome <span class=ui>Cone</span>. Segure o botão esquerdo nele e <b>solte bem no meio da tampa</b> do corpo.<br><br>O cone nasce <b>em cima</b> do corpo, e aparece o <b>quadrado verde</b>: o plano de trabalho foi para o alto da peça. O cone nasce <b>centrado</b> na tampa — por isso não é preciso alinhar.",
    ck="Um cone roxo pequeno está pousado na tampa do corpo, e o painel diz <span class=ui>Cone</span>.",
    sos=[("Não acho o Cone","Fica na fileira da pirâmide amarela: é o roxo."),
         ("O cone caiu no chão","Você soltou fora do corpo. Arraste-o de novo para a <b>tampa</b>.")]),

  dict(n=5, titulo="Ponta 20 × 20 × 20, pelas alças", img="aula6/g05_depois.jpg", clipe="medidas_ponta.gif",
    corpo="Clique na <b>alça do canto</b> da base do cone; escreva <b>20</b> nos dois números da base. Depois clique na alça do <b>meio da ponta</b> e escreva <b>20</b> na altura.<br><br>A base do cone tem a <b>mesma largura</b> do corpo e a ponta fica com 20 mm de altura: o foguete está de cabeça feita.",
    ck="O cone ficou do mesmo diâmetro do corpo, formando a ponta do foguete.",
    sos=[("O cone ficou largo demais","Volte à alça do canto e escreva 20 nos dois números."),
         ("Sumiu a ponta","Você mexeu na altura do corpo. Aperte Ctrl + Z e refaça só o cone.")]),

  dict(n=6, titulo="Arraste uma Caixa: a aleta", img="aula6/g10_depois.jpg", clipe="caixa.gif",
    corpo="Clique num <b>lugar vazio</b> do plano. Arraste uma <b>Caixa vermelha</b> da coluna da direita e solte <b>no plano, à direita do foguete</b>, longe dele.<br><br>Essa caixa vai virar uma <b>tira</b> que atravessa o corpo: uma peça só que dá <b>duas</b> aletas.",
    ck="Tem uma caixa vermelha no plano, ao lado do foguete, e o painel diz <span class=ui>Caixa</span>.",
    sos=[("A caixa caiu em cima do foguete","Arraste-a de novo para o plano, longe dele."),
         ("Peguei a caixa cinza listrada","Essa é o buraco. Aperte Delete e pegue a vermelha.")]),

  dict(n=7, titulo="Aleta: Comprimento 6, Largura 40, Altura 16", img="aula6/g11_depois.jpg", clipe="medidas_aleta.gif",
    corpo="No painel, escreva <b>6</b> em <span class=ui>Comprimento</span>, <b>40</b> em <span class=ui>Largura</span> e <b>16</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada).<br><br>É uma tirinha: <b>comprida</b> de lado a lado (40 mm), <b>fina</b> de frente para trás (6 mm) e <b>baixa</b> (16 mm).",
    ck="A caixa virou uma tira comprida e baixa, e os campos mostram 6, 40 e 16.",
    sos=[("A tira ficou virada","O <b>40</b> tem de estar em <span class=ui>Largura</span>, e não em Comprimento."),
         ("Digitei e nada mudou","Falta o <span class=ui>Enter</span> depois de cada número.")]),

  dict(n=8, titulo="Escolha o corpo e a aleta: clique e Shift + clique", img="aula6/g12_depois.jpg", clipe="duas.gif",
    corpo="Clique num lugar vazio do plano. Clique <b>no corpo</b> do foguete (o laranja). Agora segure <span class=ui>Shift</span> e clique <b>na aleta</b> (a tira vermelha).<br><br>O Shift <b>junta</b> a segunda peça à seleção. O cone fica de fora: só o corpo e a aleta.",
    ck="O corpo e a aleta têm contorno azul, e o painel diz <span class=ui>Shapes(2)</span>. O cone não tem contorno.",
    sos=[("O painel diz Shapes(3)","O cone entrou. Clique num lugar vazio e refaça: primeiro o corpo, depois Shift + clique na aleta."),
         ("Só a aleta ficou selecionada","Você soltou o Shift antes do clique, ou não clicou no corpo primeiro. Refaça.")]),

  dict(n=9, titulo="Abra o Alinhar", img="aula6/g12b_depois.jpg", clipe="alinhar2.gif",
    corpo="Na barra de cima, clique no botão <span class=ui>Alinhar</span> (o ícone de linhas de tamanhos diferentes, ao lado do espelho). Aparecem as bolinhas pretas em volta do corpo e da aleta.",
    ck="Apareceram as bolinhas pretas em volta do corpo e da aleta.",
    sos=[("As bolinhas não apareceram","O Alinhar só abre com <b>duas ou mais</b> peças selecionadas. Volte ao passo 8.")]),

  dict(n=10, titulo="FIXE o corpo: clique nele", img="aula6/g13_depois.jpg", clipe="fixa2.gif",
    corpo="Clique em cima do <b>corpo laranja</b> do foguete: ele fica <b>fixo</b> e só a aleta vai andar.",
    ck="O corpo foi clicado e as bolinhas continuam na tela.",
    sos=[("A seleção sumiu","Você clicou fora do corpo. Aperte Ctrl + Z e refaça os passos 8 a 10.")]),

  dict(n=11, titulo="Centro em X: a bolinha do meio, embaixo", img="aula6/g14_depois.jpg", clipe="alinha_x2.gif",
    corpo="Clique na <b>bolinha do meio</b> da fileira de <b>baixo</b>. A tira <b>desliza</b> e se centra no corpo, da esquerda para a direita.",
    ck="A tira está centrada no corpo, da esquerda para a direita.",
    sos=[("O corpo andou","Você não fixou o corpo. Aperte Ctrl + Z e volte ao passo 10.")]),

  dict(n=12, titulo="Centro em Y: a bolinha do meio, à esquerda", img="aula6/g15_depois.jpg", clipe="alinha_y2.gif",
    corpo="Clique na <b>bolinha do meio</b> da coluna da <b>esquerda</b>. A tira atravessa o corpo <b>pelo meio</b>, de frente para trás, e aparece dos dois lados: já são <b>duas aletas</b>.<br><br>Não precisa alinhar a altura: a tira já nasceu <b>no chão</b>, na mesma base do corpo. Aperte <span class=ui>Esc</span> para fechar o Alinhar.",
    ck="A tira passa pelo meio do corpo e sai dos dois lados, rente ao chão.",
    sos=[("A tira está na frente do corpo","Faltou este passo: clique na bolinha do meio da coluna da esquerda."),
         ("Sobrou o Alinhar na tela","Aperte <span class=ui>Esc</span>.")]),

  dict(n=13, titulo="Clique na aleta e aperte Ctrl + D", img="aula6/g17_depois.jpg", clipe="duplica.gif",
    corpo="Clique numa <b>ponta da tira</b> (a parte vermelha que sai do corpo): só a tira fica selecionada. Aperte <span class=ui>Ctrl</span> + <span class=ui>D</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>D</span>).<br><br><b>Nada muda na tela</b>: nasceu uma cópia da tira, em cima da original, e é ela que fica selecionada.",
    ck="O painel diz <span class=ui>Caixa</span> e as alças estão em volta da tira.",
    sos=[("Selecionou o corpo","Você clicou no laranja. Clique na ponta <b>vermelha</b> da tira."),
         ("Não sei se copiou","Aperte Ctrl + Z: se a tira sumir, é porque tinha copiado. Aperte Ctrl + Y e siga.")]),

  dict(n=14, titulo="Gire a cópia 90°: a seta curva de baixo", img="aula6/g18_depois.jpg", clipe="gira.gif",
    corpo="Embaixo da tira há uma <b>seta curva</b> pequena. Segure o botão esquerdo nela e arraste <b>em volta do foguete, num arco</b>, subindo para a direita, até o transferidor mostrar <b>90°</b> (ou −90°). Solte.<br><br>A cópia <b>gira</b> como uma porta e atravessa o corpo pelo outro lado: com a tira de antes, já formam uma <b>cruz</b> — quatro aletas.",
    ck="As duas tiras formam uma <b>cruz</b> em volta do corpo, e o transferidor mostrou 90° (ou −90°).",
    sos=[("O transferidor trava em 40 ou 50","Você está arrastando em linha reta. Faça um arco, como se desenhasse o pedaço de um círculo em volta do foguete."),
         ("Passou de 90","Continue arrastando até voltar ao número certo, ou aperte Ctrl + Z e recomece.")]),

  dict(n=15, titulo="Selecione tudo: Ctrl + A", img="aula6/g19a_depois.jpg", clipe="seleciona.gif",
    corpo="Clique num <b>lugar vazio</b> do plano, segure <span class=ui>Ctrl</span> e aperte <span class=ui>A</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>A</span>). O corpo, o cone e as duas tiras ficam selecionados: <span class=ui>Shapes(4)</span>.",
    ck="O foguete inteiro tem contorno azul, e o painel diz <span class=ui>Shapes(4)</span>.",
    sos=[("O painel diz Shapes(3)","Faltou uma peça. Clique num lugar vazio e aperte Ctrl + A de novo.")]),

  dict(n=16, titulo="Agrupe: Grupo de união", img="aula6/g19_depois.jpg", clipe="uniao.gif",
    corpo="Na barra de cima há três botõezinhos de juntar peças, à direita do meio. Clique no <b>do meio</b>, o <span class=ui>Grupo de união</span>.<br><br>O foguete vira <b>uma peça só</b>, toda da mesma cor: o painel diz <span class=ui>Union</span>.",
    ck="O foguete é uma peça só, de uma cor só, e o painel diz <span class=ui>Union</span>.",
    sos=[("O painel não mudou","Clique no botão do meio dos três, o <span class=ui>Grupo de união</span>."),
         ("Sumiu o cone","O cone não encostava no corpo. Desagrupe com Ctrl + Shift + G e confira o passo 4.")]),

  dict(n=17, titulo="Olhe de cima: a cruz", img="aula6/g20_depois.jpg", clipe="vista_cima.gif",
    corpo="Clique num <b>lugar vazio</b> do plano. No <b>cubo</b> de vistas, no canto de cima à esquerda, clique na face escrita <span class=ui>SUPERIOR</span>.<br><br>De cima se vê uma <b>cruz</b>: o corpo redondo no meio e as quatro aletas saindo para os lados.",
    ck="De cima, um círculo no meio e quatro aletas em cruz, iguais entre si.",
    sos=[("A câmera não mudou","Clique <b>na palavra</b> SUPERIOR do cubinho."),
         ("Só vejo duas aletas","A cópia não foi girada. Volte ao passo 14.")]),

  dict(n=18, titulo="Olhe de frente: o foguete de pé", img="aula6/g20f_depois.jpg", clipe="vista_frente.gif",
    corpo="No mesmo <b>cubo</b> de vistas, clique na face escrita <span class=ui>FRONTAL</span>.<br><br>De frente se vê o foguete de pé: a ponta, o corpo e as aletas na base, rentes ao chão.",
    ck="De frente: a ponta de cone em cima, o corpo no meio e as aletas embaixo, no chão.",
    sos=[("A câmera não mudou","Clique <b>na palavra</b> FRONTAL do cubinho.")]),

  dict(n=19, titulo="Dê um nome ao seu projeto", img="aula6/g21_depois.jpg", clipe="batiza.gif",
    corpo="Clique na <b>casinha</b> da barra da esquerda para voltar à vista inicial. Depois clique no <b>nome do projeto</b>, no canto de cima à esquerda, apague, escreva <b>Foguete da ANA</b> (ou o seu nome) e aperte <span class=ui>Enter</span>.<br><br>O Tinkercad salva sozinho. O foguete está guardado na sua conta.",
    ck="No canto de cima à esquerda aparece o <b>nome que você escreveu</b>.",
    sos=[("O nome não mudou","Falta o <span class=ui>Enter</span>."),
         ("O campo não abriu","Clique <b>em cima das letras</b> do nome.")]),
 ],
}
