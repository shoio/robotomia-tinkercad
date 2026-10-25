# -*- coding: utf-8 -*-
"""Aula 4 — Casinha: uma Caixa, um Telhado e um vão de porta.

Tudo o que esta aula afirma sobre a tela foi MEDIDO na bancada (fonte/cap4.py).
Quatro coisas desta aula ninguém acerta de cabeça:

  · o Telhado NÃO tem campo de medida: o tamanho vem das alças (passo 5);
  · solto em cima da casa, o telhado já nasce na altura da tampa (passo 4) —
    mas fica torto: é o Alinhar, com a casa FIXA, que o põe no meio (7 a 10);
  · para alinhar só a casa e a porta é preciso escolhê-las: clique numa e
    Shift + clique na outra (passo 14);
  · o furo da porta fica RENTE à parede da frente quando se alinha em «frente»
    (passo 18): metade dentro, metade fora não cavaria direito.
"""

AULA = {
 "n": 4,
 "slug": "aula4",
 "titulo": "Casinha",
 "subtitulo": "Uma caixa vira casa: ganha um telhado de duas águas, centrado em cima, e um vão de porta na parede da frente.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 4 · telhado e porta",
 "fim": "Acabou a Aula 4. Você fez uma <b>casinha</b>: uma caixa de 60 × 50 × 40 mm, um <b>telhado</b> de duas águas centrado em cima e um <b>vão de porta</b> cavado na parede da frente. Aprendeu a usar o <b>Alinhar</b> com uma peça <b>fixa</b>, a escolher só duas peças com <b>Shift + clique</b> e a alinhar uma peça <b>rente à frente</b> da outra. A peça está salva na sua conta com o nome que você deu — é só abrir o Tinkercad e ela está lá.",
 "avisos": [
   ("Projeto novo", "Esta aula começa num projeto novo, vazio. As peças das aulas anteriores continuam guardadas na sua conta."),
   ("Milímetros", "Todo número é em milímetro. A casinha cabe na palma da mão: <b>60 mm</b> é a largura de um cartão de crédito dobrada ao meio, mais ou menos."),
   ("O que você já sabe", "As formas, as medidas pelos campos e pelas alças, o <span class=ui>Ctrl + A</span>, o <span class=ui>Alinhar</span> e o <span class=ui>Grupo de união</span> são das aulas 1 a 3. Hoje eles aparecem juntos."),
   ("Os clipes", "Os passos com animação mostram o gesto inteiro: o mouse andando, o <b>botão certo acendendo</b> e as <b>teclas acesas</b> quando o gesto é de teclado."),
   ("Travou?", "Todo passo tem um quadro laranja embaixo com o conserto dos erros mais comuns."),
 ],
 "passos": [

  dict(n=1, titulo="Abra o Tinkercad e crie um Projeto 3D", img="aula4/p01_vazio.jpg", clipe="criar.gif",
    corpo="Entre no Tinkercad com a sua conta, como nas aulas anteriores. No canto de cima à direita, clique em <span class=ui>+ Criar</span> e, na primeira linha, em <span class=ui>Projeto 3D</span>.<br><br>Abre o editor com o plano azul quadriculado <b>vazio</b> e um nome sorteado — deixe assim, no último passo você troca.",
    ck="O editor abriu com o plano azul claro quadriculado vazio.",
    sos=[("Não sei entrar","Chame o professor. Não crie conta nova: os seus projetos estão na antiga."),
         ("Abriu outra coisa","Volte com a seta ⟵ do navegador e clique de novo em <span class=ui>+ Criar</span>, escolhendo a primeira linha."),
         ("A tela ficou branca","O Tinkercad é pesado. Espere até meio minuto. Se continuar branca, recarregue com <span class=ui>F5</span>.")]),

  dict(n=2, titulo="Arraste uma Caixa para o plano", img="aula4/g02_depois.jpg", clipe="caixa.gif",
    corpo="Na coluna da direita, a forma <b>vermelha</b> do meio da segunda fileira, à esquerda, é a <span class=ui>Caixa</span>. Segure o botão esquerdo nela, <b>arraste até o meio do plano</b> e solte.<br><br>É a <b>parede</b> da casa.",
    ck="Tem um cubo vermelho no meio do plano, com quadradinhos brancos em volta, e o painel branco escrito <span class=ui>Caixa</span> no alto.",
    sos=[("Peguei a caixa cinza listrada","Essa é o <b>buraco</b>. Aperte <span class=ui>Delete</span> e arraste a vermelha, a da segunda fileira."),
         ("Não apareceu o painel","Clique uma vez na caixa: o painel abre quando ela está selecionada.")]),

  dict(n=3, titulo="Comprimento 50, Largura 60, Altura 40", img="aula4/g03_depois.jpg", clipe="medidas_casa.gif",
    corpo="No painel, clique no campo <span class=ui>Comprimento</span>, apague, escreva <b>50</b> e aperte <span class=ui>Enter</span>. Faça o mesmo em <span class=ui>Largura</span> com <b>60</b> e em <span class=ui>Altura</span> com <b>40</b>.<br><br>O número <b>grande</b> vai em <span class=ui>Largura</span>: é a direção que corre da esquerda para a direita na tela. A casa fica <b>mais larga que funda</b>.",
    ck="Os três campos mostram <b>50</b>, <b>60</b> e <b>40</b>, e a caixa virou um bloco largo, de frente para você.",
    sos=[("O bloco ficou fundo e estreito","O 60 foi parar em <span class=ui>Comprimento</span>. Troque: <b>50</b> em Comprimento e <b>60</b> em Largura."),
         ("Digitei e nada mudou","Falta o <span class=ui>Enter</span> depois de cada número."),
         ("O campo ficou com número estranho","Clique no campo, aperte Ctrl + A (no Mac, Cmd + A) e escreva de novo.")]),

  dict(n=4, titulo="Solte o Telhado em cima da casa", img="aula4/g04_depois.jpg", clipe="telhado.gif",
    corpo="Na coluna da direita, na fileira do cone e da pirâmide, a forma <b>verde</b> com o nome <span class=ui>Telhado</span> é um prisma de duas águas. Segure o botão esquerdo nela e <b>solte bem no meio da tampa</b> da casa.<br><br>O telhado nasce <b>em cima</b> da casa, na altura da tampa — e aparece um <b>quadrado verde</b>: o plano de trabalho foi para o alto da caixa. Ele ainda é pequenininho e está fora do lugar.",
    ck="Um telhado verde pequeno está <b>pousado na tampa</b> da casa, com quadradinhos brancos em volta, e o painel diz <span class=ui>Telhado</span>.",
    sos=[("Não acho o Telhado","Fica na fileira do <b>cone</b> (roxo) e da <b>pirâmide</b> (amarela): é o verde, o terceiro dessa fileira."),
         ("O telhado caiu no chão, ao lado","Você soltou fora da casa. Arraste-o de novo, soltando em cima da <b>tampa</b>."),
         ("Peguei a pirâmide","Serve para outra aula. Aperte <span class=ui>Delete</span> e pegue o verde.")]),

  dict(n=5, titulo="Telhado 66 × 56 × 24, pelas alças", img="aula4/g05_depois.jpg", clipe="medidas_telhado.gif",
    corpo="O telhado <b>não tem campo de medida</b>, como o cilindro da Aula 2: o tamanho vem das <b>alças</b>.<br><br><b>1.</b> Clique na <b>alça do canto</b> de cima à esquerda da base do telhado. Clique no número da <b>esquerda</b> e escreva <b>56</b> (<span class=ui>Enter</span>); clique no número de <b>cima</b> e escreva <b>66</b> (<span class=ui>Enter</span>).<br><b>2.</b> Clique na alça do <b>meio da ponta</b> (a de cima) e escreva <b>24</b> no número da altura.<br><br>O telhado cresce <b>3 mm para cada lado</b> além da casa (66 − 60 = 6, e 6 ÷ 2 = 3): é o <b>beiral</b>. Ele vai ficar torto, para um lado: o Alinhar arruma já.",
    ck="O telhado ficou grande, <b>mais largo</b> que a casa, e cobre a tampa — mas não está centrado: sobra mais de um lado do que do outro.",
    sos=[("Os números sumiram","Clique no telhado e de novo na alça do canto: eles reaparecem."),
         ("Apareceu um número só","Você clicou na alça do <b>meio</b>: ela mede a altura. A do <b>canto</b> mostra dois números."),
         ("O telhado afundou na casa","Aperte Ctrl + Z e confira se o telhado ainda está em cima da tampa antes de mexer nas alças.")]),

  dict(n=6, titulo="Selecione tudo: Ctrl + A", img="aula4/g06_depois.jpg", clipe="seleciona.gif",
    corpo="Clique num <b>lugar vazio</b> do plano e aperte <span class=ui>Ctrl</span> + <span class=ui>A</span> (no Mac, <span class=ui>Cmd</span> + <span class=ui>A</span>).<br><br>A casa e o telhado ficam selecionados juntos: o painel diz <span class=ui>Shapes(2)</span>.",
    ck="A casa e o telhado têm contorno azul, e o painel diz <span class=ui>Shapes(2)</span>.",
    sos=[("Selecionou só um","Clique num lugar vazio do plano e aperte Ctrl + A de novo.")]),

  dict(n=7, titulo="Abra o Alinhar", img="aula4/g07_depois.jpg", clipe="alinhar.gif",
    corpo="Na barra de cima, clique no botão <span class=ui>Alinhar</span> (o ícone com linhas de tamanhos diferentes, ao lado do espelho).<br><br>Aparecem as nove bolinhas pretas em volta das duas peças, como nas aulas 2 e 3.",
    ck="Apareceram as bolinhas pretas em volta da casa e do telhado, e no alto a frase <i>Clique nas alças para alinhar as formas</i>.",
    sos=[("As bolinhas não apareceram","O Alinhar só abre com <b>duas ou mais</b> peças selecionadas. Volte ao passo 6."),
         ("Não acho o botão","Fica na barra de cima, no meio, ao lado do espelho. Passe o mouse e espere o nome aparecer.")]),

  dict(n=8, titulo="FIXE a casa: clique nela", img="aula4/g08_depois.jpg", clipe="fixa.gif",
    corpo="O Alinhar <b>move todas as peças</b> até uma linha comum. Se você alinhar assim, quem se mexe pode ser a <b>casa</b>, e não o telhado.<br><br>Clique <b>no corpo vermelho da casa</b> (uma forma selecionada): ela fica <b>fixa</b>, e só o telhado vai andar.",
    ck="A casa foi clicada e as bolinhas continuam na tela; daqui em diante só o telhado vai se mexer.",
    sos=[("A seleção sumiu","Você clicou fora da casa. Aperte Ctrl + Z, abra o Alinhar de novo e clique <b>em cima do vermelho</b> da casa."),
         ("Não sei se fixou","Siga os próximos passos: se a casa andar, volte ao passo 7 e fixe antes de clicar nas bolinhas.")]),

  dict(n=9, titulo="Centro em X: a bolinha do meio, embaixo", img="aula4/g09_depois.jpg", clipe="alinha_x.gif",
    corpo="Clique na <b>bolinha do meio</b> da fileira de <b>baixo</b>.<br><br>O telhado <b>desliza</b> e se centra na casa, <b>da esquerda para a direita</b>: o beiral fica igual dos dois lados.",
    ck="O telhado ficou centrado na casa da esquerda para a direita; a casa não se mexeu.",
    sos=[("As bolinhas mudaram de lugar","É normal: depois de cada clique elas se reposicionam. Procure de novo a do meio de baixo."),
         ("A casa é que andou","Você não fixou a casa. Aperte Ctrl + Z e volte ao passo 8.")]),

  dict(n=10, titulo="Centro em Y: a bolinha do meio, à esquerda", img="aula4/g10_depois.jpg", clipe="alinha_y.gif",
    corpo="Clique na <b>bolinha do meio</b> da coluna da <b>esquerda</b>.<br><br>Agora o telhado também está centrado de <b>frente para trás</b>: o beiral é igual na frente e atrás. Aperte <span class=ui>Esc</span> para fechar o Alinhar.",
    ck="O telhado está <b>centrado</b> em cima da casa, com beiral igual em volta.",
    sos=[("O telhado ainda está torto","Faça os dois: o do meio embaixo (passo 9) e o do meio à esquerda (este)."),
         ("Sobrou o Alinhar na tela","Aperte <span class=ui>Esc</span>.")]),

  dict(n=11, titulo="Traga outra Caixa: a porta", img="aula4/g11_depois.jpg", clipe="caixa_porta.gif",
    corpo="Clique num lugar vazio do plano, para soltar a seleção. Arraste <b>outra Caixa vermelha</b> da coluna da direita e solte <b>no plano, à frente e ao lado da casa</b> — não em cima dela.<br><br>Essa caixa vai virar o <b>buraco da porta</b>.",
    ck="Tem uma caixinha vermelha no plano, fora da casa, e o painel diz <span class=ui>Caixa</span>.",
    sos=[("A caixa nasceu em cima do telhado","Arraste-a de novo para o <b>plano</b>, longe da casa. Ela precisa estar no chão."),
         ("Peguei a caixa cinza listrada","Essa já é o buraco: pule o próximo passo. Mas ela nasce no tamanho padrão.")]),

  dict(n=12, titulo="Transforme a caixa em Orifício", img="aula4/g12_depois.jpg", clipe="orificio.gif",
    corpo="Com a caixinha selecionada, no painel clique em <span class=ui>Orifício</span> (a bolinha cinza listrada, ao lado de <span class=ui>Sólido</span>).<br><br>A caixa fica <b>cinza e listrada</b>: agora é um <b>buraco</b>.",
    ck="A caixinha ficou cinza e listrada, e no painel o <span class=ui>Orifício</span> está marcado.",
    sos=[("Nada mudou de cor","Confira que a caixinha está selecionada (com as alças) e clique na bolinha do <span class=ui>Orifício</span>."),
         ("A casa é que ficou listrada","Você estava com a casa selecionada. Clique no <span class=ui>Sólido</span> para desfazer e selecione a caixinha.")]),

  dict(n=13, titulo="Porta: Comprimento 12, Largura 16, Altura 28", img="aula4/g13_depois.jpg", clipe="medidas_porta.gif",
    corpo="No painel, escreva <b>12</b> em <span class=ui>Comprimento</span>, <b>16</b> em <span class=ui>Largura</span> e <b>28</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada).<br><br>A porta tem <b>16 mm de largura</b> e <b>28 de altura</b>, e o <b>12</b> é a <b>profundidade</b>: é o quanto o buraco vai entrar na parede.",
    ck="Os campos mostram <b>12</b>, <b>16</b> e <b>28</b>, e o buraco ficou do tamanho de uma portinha em pé.",
    sos=[("A porta ficou deitada","Confira: a <b>altura</b> (28) é o maior número, e a largura (16) é maior que o comprimento (12)."),
         ("O número ficou estranho","Clique no campo, aperte Ctrl + A (no Mac, Cmd + A) e escreva de novo.")]),

  dict(n=14, titulo="Escolha só a casa e a porta: clique e Shift + clique", img="aula4/g14_depois.jpg", clipe="duas.gif",
    corpo="Clique num lugar vazio do plano. Clique <b>na casa</b> (no vermelho da parede). Agora segure <span class=ui>Shift</span> e clique <b>na porta</b> (a caixinha listrada): o Shift <b>junta</b> a segunda peça à seleção, sem soltar a primeira.<br><br>O telhado fica de fora: <b>só a casa e a porta</b> vão ser alinhadas.",
    ck="A casa e a porta têm contorno azul, e o painel diz <span class=ui>Shapes(2)</span>. O telhado não tem contorno.",
    sos=[("O painel diz Shapes(3)","O telhado entrou na seleção. Clique num lugar vazio e refaça: primeiro a casa, depois Shift + clique na porta."),
         ("Só a porta ficou selecionada","Você soltou o Shift antes do clique, ou não clicou na casa primeiro. Refaça."),
         ("Não consigo clicar na porta","Ela é cinza listrada, na frente da casa. Clique bem no meio dela.")]),

  dict(n=15, titulo="Abra o Alinhar de novo", img="aula4/g15_depois.jpg", clipe="alinhar2.gif",
    corpo="Na barra de cima, clique no botão <span class=ui>Alinhar</span>.<br><br>As bolinhas pretas aparecem em volta da casa e da porta — só das duas.",
    ck="Apareceram as bolinhas pretas em volta da casa e da porta.",
    sos=[("As bolinhas não apareceram","Você precisa de duas peças selecionadas. Volte ao passo 14.")]),

  dict(n=16, titulo="FIXE a casa de novo", img="aula4/g16_depois.jpg", clipe="fixa2.gif",
    corpo="Clique em cima do <b>corpo vermelho da casa</b>: ela fica <b>fixa</b> e só a porta vai andar.",
    ck="A casa foi clicada e as bolinhas continuam na tela.",
    sos=[("A seleção sumiu","Você clicou fora da casa. Aperte Ctrl + Z e refaça os passos 14 a 16.")]),

  dict(n=17, titulo="Centro em X: a bolinha do meio, embaixo", img="aula4/g17_depois.jpg", clipe="alinha_x2.gif",
    corpo="Clique na <b>bolinha do meio</b> da fileira de <b>baixo</b>.<br><br>A porta <b>desliza</b> para o <b>meio</b> da parede da frente, da esquerda para a direita.",
    ck="A porta ficou no meio da parede da frente; a casa não se mexeu.",
    sos=[("A casa é que andou","Você não fixou a casa no passo 16. Aperte Ctrl + Z e refaça.")]),

  dict(n=18, titulo="Rente à frente: a bolinha de baixo, à esquerda", img="aula4/g18_depois.jpg", clipe="alinha_frente.gif",
    corpo="Clique na <b>bolinha de baixo</b> da coluna da <b>esquerda</b> (a mais perto de você, que alinha <b>na frente</b>).<br><br>A porta encosta na parede da frente: <b>a frente dela fica rente à frente da casa</b>, e os 12 mm de profundidade entram parede adentro. É assim que o buraco cava a parede.",
    ck="A porta está <b>rente à parede da frente</b>, com o corpo dela dentro da casa. Aperte <span class=ui>Esc</span> para fechar o Alinhar.",
    sos=[("Alinhou no meio e a porta sumiu","Você clicou na bolinha do <b>meio</b> da coluna. A que alinha na <b>frente</b> é a de baixo."),
         ("A porta ficou toda dentro","Pode acontecer se alinhar no meio: só a de baixo deixa a porta rente à frente.")]),

  dict(n=19, titulo="Esc, Ctrl + A e Grupo de união", img="aula4/g19_depois.jpg", clipe="uniao.gif",
    corpo="Aperte <span class=ui>Esc</span>. Clique num lugar vazio e aperte <span class=ui>Ctrl</span> + <span class=ui>A</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>A</span>): agora são <b>três</b> peças selecionadas, <span class=ui>Shapes(3)</span>.<br><br>Na barra de cima, clique no do <b>meio</b> dos três botõezinhos de juntar, o <span class=ui>Grupo de união</span>.<br><br>O buraco da porta <b>cava a parede</b>, e a casa, o telhado e a porta viram <b>uma peça só</b>, toda de uma cor.",
    ck="A casa virou <b>uma peça só</b>, toda vermelha, com um <b>vão de porta</b> na parede da frente, e o painel diz <span class=ui>Union</span>.",
    sos=[("O painel diz Shapes(2)","Faltou uma peça. Clique num lugar vazio do plano e aperte Ctrl + A de novo."),
         ("A porta não cavou","O buraco ficou longe da parede. Aperte Ctrl + Z, desagrupe, e refaça o Alinhar da porta (passos 14 a 18)."),
         ("Sumiu o telhado","O buraco encostou nele. Desagrupe com Ctrl + Shift + G e confira que a porta só toca a parede, não o telhado.")]),

  dict(n=20, titulo="Olhe de frente: a porta e o telhado", img="aula4/g20_depois.jpg", clipe="vista_frente.gif",
    corpo="Clique num <b>lugar vazio</b> do plano. No canto de cima à esquerda, no <b>cubo</b> de vistas, clique na face escrita <span class=ui>FRONTAL</span>.<br><br>A câmera desce e você vê a casa <b>de frente</b>: o telhado <b>de duas águas</b> em cima, com o beiral dos dois lados, e a <b>porta</b> aberta no meio da parede, rente ao chão.",
    ck="De frente se vê o telhado de duas águas, as paredes vermelhas e, no meio, o <b>vão da porta</b> chegando ao chão.",
    sos=[("Não vejo a porta","Confira se não está olhando por trás. Para voltar à vista inicial, use a casinha da barra da esquerda."),
         ("A câmera não mudou","Clique <b>na palavra</b> FRONTAL do cubinho.")]),

  dict(n=21, titulo="Dê um nome ao seu projeto", img="aula4/g21_depois.jpg", clipe="batiza.gif",
    corpo="Clique na <b>casinha</b> da barra da esquerda para voltar à vista inicial. Depois clique no <b>nome do projeto</b>, no canto de cima à esquerda (o sorteado). Apague, escreva <b>Casinha da ANA</b> (ou o seu nome) e aperte <span class=ui>Enter</span>.<br><br>O Tinkercad salva sozinho. A casinha está guardada na sua conta.",
    ck="No canto de cima à esquerda aparece o <b>nome que você escreveu</b>, no lugar do sorteado.",
    sos=[("O nome não mudou","Falta o <span class=ui>Enter</span>. Clique no nome de novo e faça de novo."),
         ("Clicou e o campo não abriu","Clique <b>em cima das letras</b> do nome, e não ao lado.")]),
 ],
}
