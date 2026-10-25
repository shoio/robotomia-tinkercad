# -*- coding: utf-8 -*-
"""Aula 9 — Porta-celular: uma base, um encosto inclinado e um batente.

Medido na bancada (fonte/cap9.py). Pegadinhas:
  · a seta de INCLINAR é a terceira seta curva, a menorzinha, junto da quina de
    trás-direita da tampa; puxada para CIMA ela inclina o encosto para TRÁS, e o
    transferidor lê -15°, -20°, -27°… (não para em 22,5°: o ângulo é «uns 20°»);
  · na vista inicial a base fica escondida atrás do batente e debaixo do
    encosto: só a faixa da tampa entre os dois é dela (é ali que se clica);
  · Alinhar 'atrás' e 'frente' usam a base como régua: o encosto vai para o
    fundo e o batente para a frente.
"""

AULA = {
 "n": 9,
 "slug": "aula9",
 "titulo": "Porta-celular",
 "subtitulo": "Uma base, um encosto inclinado para trás e um batente na frente: o celular fica de pé, olhando para você.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 9 · inclinar",
 "fim": "Acabou a Aula 9. Você fez um <b>porta-celular</b>: uma base, um <b>encosto inclinado</b> para trás (uns 20°) e um <b>batente</b> na frente para o celular não escorregar. Aprendeu a <b>inclinar</b> uma peça pela setinha do lado e a usar a <b>base como régua</b> no Alinhar: o encosto vai para trás, o batente para a frente. A peça está salva na sua conta com o nome que você deu. <i>Desafio:</i> meça o seu celular e ajuste a largura do batente.",
 "avisos": [
   ("Projeto novo", "Esta aula começa num projeto novo, vazio. As peças das aulas anteriores continuam guardadas na sua conta."),
   ("Milímetros", "A base tem <b>60 mm</b> de lado: cabe um celular pequeno. Para um maior, aumente os números dos passos 3, 5 e 12 juntos."),
   ("Inclinar", "Hoje chega uma setinha nova: a <b>seta curva do lado</b>. Ela é a menor das três e quase não aparece; o passo 6 mostra onde está."),
   ("Os clipes", "Os passos com animação mostram o gesto inteiro: o mouse andando, o <b>botão certo acendendo</b> e as <b>teclas acesas</b> quando o gesto é de teclado."),
   ("Travou?", "Todo passo tem um quadro laranja embaixo com o conserto dos erros mais comuns."),
 ],
 "passos": [

  dict(n=1, titulo="Abra o Tinkercad e crie um Projeto 3D", img="aula9/p01_vazio.jpg", clipe="criar.gif",
    corpo="Entre no Tinkercad com a sua conta. No canto de cima à direita, clique em <span class=ui>+ Criar</span> e, na primeira linha, em <span class=ui>Projeto 3D</span>.<br><br>Abre o editor com o plano azul quadriculado <b>vazio</b> e um nome sorteado — deixe assim, no último passo você troca.",
    ck="O editor abriu com o plano azul claro quadriculado vazio.",
    sos=[("Não sei entrar","Chame o professor. Não crie conta nova: os seus projetos estão na antiga."),
         ("Abriu outra coisa","Volte com a seta ⟵ do navegador e clique de novo em <span class=ui>+ Criar</span>, escolhendo a primeira linha."),
         ("A tela ficou branca","O Tinkercad é pesado. Espere até meio minuto. Se continuar branca, recarregue com <span class=ui>F5</span>.")]),

  dict(n=2, titulo="Arraste uma Caixa para o plano: a base", img="aula9/g02_depois.jpg", clipe="caixa.gif",
    corpo="Na coluna da direita, a forma <b>vermelha</b> do meio da segunda fileira, à esquerda, é a <span class=ui>Caixa</span>. Segure o botão esquerdo nela, <b>arraste até o meio do plano</b> e solte.",
    ck="Tem um cubo vermelho no meio do plano e o painel branco escrito <span class=ui>Caixa</span> no alto.",
    sos=[("Peguei a caixa cinza listrada","Essa é o <b>buraco</b>. Aperte <span class=ui>Delete</span> e arraste a vermelha.")]),

  dict(n=3, titulo="Base: Comprimento 60, Largura 60, Altura 6", img="aula9/g03_depois.jpg", clipe="medidas_base.gif",
    corpo="No painel, escreva <b>60</b> em <span class=ui>Comprimento</span>, <b>60</b> em <span class=ui>Largura</span> e <b>6</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada).<br><br>A base é um <b>quadrado</b> fininho, de 6 mm de espessura.",
    ck="O cubo virou uma placa quadrada, baixa, no meio do plano.",
    sos=[("Digitei e nada mudou","Falta o <span class=ui>Enter</span> depois de cada número."),
         ("A base ficou alta","O 6 foi parar em outro campo. Confira: a <b>altura</b> é 6.")]),

  dict(n=4, titulo="Solte outra Caixa na base: o encosto", img="aula9/g04_depois.jpg", clipe="caixa_encosto.gif",
    corpo="Clique num lugar vazio do plano. Arraste <b>outra Caixa vermelha</b> e solte <b>no fundo da base</b>, na parte de trás da tampa.<br><br>A caixa nasce <b>em cima</b> da base, e aparece o quadrado verde (o plano de trabalho foi para o alto da base).",
    ck="Tem uma caixa vermelha pousada na tampa da base, perto do fundo, com o quadrado verde em volta.",
    sos=[("A caixa caiu no chão","Você soltou fora da base. Arraste de novo para a <b>tampa</b> da base.")]),

  dict(n=5, titulo="Encosto: Comprimento 6, Largura 60, Altura 70", img="aula9/g05_depois.jpg", clipe="medidas_encosto.gif",
    corpo="No painel, escreva <b>6</b> em <span class=ui>Comprimento</span>, <b>60</b> em <span class=ui>Largura</span> e <b>70</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada).<br><br>O encosto é uma <b>parede</b> fina e alta, do mesmo tamanho da base de lado a lado.",
    ck="Uma parede alta e fina se ergue em cima da base, no fundo dela.",
    sos=[("A parede ficou deitada","Confira: <b>altura 70</b>, comprimento 6 (a espessura) e largura 60.")]),

  dict(n=6, titulo="Incline o encosto para trás: a setinha do lado", img="aula9/g06_depois.jpg", clipe="inclina.gif",
    corpo="Com o encosto selecionado, procure a <b>setinha curva do lado</b>: a terceira seta curva, <b>bem pequenininha</b>, quase invisível, <b>à direita e um pouco acima</b> da quina de trás da tampa do encosto. Segure o botão esquerdo nela e <b>arraste para cima</b>.<br><br>Aparece um <b>transferidor</b> de pé, com um número. Arraste até o número mostrar <b>−20°</b> (ou perto: −15°, −27°) e solte. O encosto <b>se deita para trás</b>: o topo vai para longe de você.",
    ck="O encosto está <b>inclinado para trás</b>, e o transferidor mostrou uns −20°.",
    sos=[("Não acho a setinha","Ela só aparece direito quando o mouse chega perto. Aproxime a câmera com o <b>+</b> e passe o mouse acima e à direita da quina de trás do encosto."),
         ("O encosto veio para a frente","Você arrastou para baixo. Aperte Ctrl + Z e arraste para <b>cima</b>."),
         ("O ângulo ficou grande demais","Volte um pouquinho sem soltar, ou aperte Ctrl + Z e arraste de novo, mais devagar.")]),

  dict(n=7, titulo="Selecione tudo: Ctrl + A", img="aula9/g07_depois.jpg", clipe="seleciona.gif",
    corpo="Clique num <b>lugar vazio</b> do plano e aperte <span class=ui>Ctrl</span> + <span class=ui>A</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>A</span>). A base e o encosto ficam selecionados: <span class=ui>Shapes(2)</span>.",
    ck="A base e o encosto têm contorno azul, e o painel diz <span class=ui>Shapes(2)</span>.",
    sos=[("Selecionou só um","Clique num lugar vazio do plano e aperte Ctrl + A de novo.")]),

  dict(n=8, titulo="Abra o Alinhar", img="aula9/g08_depois.jpg", clipe="alinhar.gif",
    corpo="Na barra de cima, clique no botão <span class=ui>Alinhar</span> (o ícone de linhas de tamanhos diferentes, ao lado do espelho). Aparecem as bolinhas pretas.",
    ck="Apareceram as bolinhas pretas em volta da base e do encosto.",
    sos=[("As bolinhas não apareceram","O Alinhar só abre com <b>duas ou mais</b> peças selecionadas. Volte ao passo 7.")]),

  dict(n=9, titulo="FIXE a base: clique nela", img="aula9/g09_depois.jpg", clipe="fixa.gif",
    corpo="A base vai ser a <b>régua</b>: tudo se alinha por ela. Clique <b>na base</b> (a parte da frente, a mais baixinha): ela fica <b>fixa</b> e só o encosto vai andar.",
    ck="A base foi clicada e as bolinhas continuam na tela.",
    sos=[("A seleção sumiu","Você clicou fora das peças. Aperte Ctrl + Z, abra o Alinhar de novo e clique <b>na base</b>."),
         ("Cliquei no encosto","Aí é a base que vai andar. Aperte Ctrl + Z e clique na base, na parte da frente.")]),

  dict(n=10, titulo="Encosto atrás: a bolinha de cima, à esquerda", img="aula9/g10_depois.jpg", clipe="alinha_atras.gif",
    corpo="Na coluna da <b>esquerda</b> há três bolinhas: frente, meio e atrás. Clique na <b>de cima</b>, a que alinha <b>atrás</b>.<br><br>O encosto <b>recua</b> até o fundo da base. Aperte <span class=ui>Esc</span> para fechar o Alinhar.",
    ck="O encosto está encostado no <b>fundo</b> da base, inclinado para trás.",
    sos=[("As bolinhas mudaram de lugar","É normal. Procure a de <b>cima</b> da coluna da esquerda."),
         ("A base é que andou","Você não fixou a base. Aperte Ctrl + Z e volte ao passo 9.")]),

  dict(n=11, titulo="Solte mais uma Caixa na frente da base: o batente", img="aula9/g11_depois.jpg", clipe="caixa_batente.gif",
    corpo="Clique num lugar vazio do plano. Arraste <b>mais uma Caixa vermelha</b> e solte <b>na frente da base</b>, na parte da frente da tampa.<br><br>O quadrado verde aparece de novo.",
    ck="Tem uma caixinha vermelha pousada na tampa da base, na frente.",
    sos=[("A caixa caiu no chão","Você soltou fora da base. Arraste de novo para a <b>tampa</b>.")]),

  dict(n=12, titulo="Batente: Comprimento 6, Largura 60, Altura 14", img="aula9/g12_depois.jpg", clipe="medidas_batente.gif",
    corpo="No painel, escreva <b>6</b> em <span class=ui>Comprimento</span>, <b>60</b> em <span class=ui>Largura</span> e <b>14</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada).<br><br>O batente é um <b>murinho</b> baixo que segura o celular para ele não escorregar.",
    ck="Um murinho vermelho baixo atravessa a frente da base, de lado a lado.",
    sos=[("O murinho ficou alto demais","Confira: <b>altura 14</b>. Os números são 6, 60 e 14.")]),

  dict(n=13, titulo="Escolha a base e o batente: clique e Shift + clique", img="aula9/g13_depois.jpg", clipe="duas.gif",
    corpo="Clique num lugar vazio do plano. Clique <b>na base</b> (a faixa entre o encosto e o batente) e, segurando <span class=ui>Shift</span>, clique <b>no batente</b>.<br><br>O Shift <b>junta</b> a segunda peça à seleção. O encosto fica de fora: só a base e o batente.",
    ck="A base e o batente têm contorno azul, e o painel diz <span class=ui>Shapes(2)</span>.",
    sos=[("O painel diz Shapes(3)","O encosto entrou. Clique num lugar vazio e refaça: primeiro a base, depois Shift + clique no batente."),
         ("A base é difícil de clicar","Só a faixa de tampa entre o encosto e o batente é dela. Clique bem no meio dessa faixa.")]),

  dict(n=14, titulo="Abra o Alinhar de novo", img="aula9/g14_depois.jpg", clipe="alinhar2.gif",
    corpo="Na barra de cima, clique no botão <span class=ui>Alinhar</span>. As bolinhas pretas aparecem em volta da base e do batente.",
    ck="Apareceram as bolinhas pretas em volta da base e do batente.",
    sos=[("As bolinhas não apareceram","Você precisa de duas peças selecionadas. Volte ao passo 13.")]),

  dict(n=15, titulo="FIXE a base de novo", img="aula9/g15_depois.jpg", clipe="fixa2.gif",
    corpo="Clique em cima da <b>base</b> (a faixa da tampa entre o encosto e o batente): ela fica <b>fixa</b> e só o batente vai andar.",
    ck="A base foi clicada e as bolinhas continuam na tela.",
    sos=[("A seleção sumiu","Você clicou fora. Aperte Ctrl + Z e refaça os passos 13 a 15.")]),

  dict(n=16, titulo="Batente rente à frente: a bolinha de baixo, à esquerda", img="aula9/g16_depois.jpg", clipe="alinha_frente.gif",
    corpo="Na coluna da <b>esquerda</b>, clique na bolinha <b>de baixo</b>, a que alinha <b>na frente</b>.<br><br>O batente fica <b>rente à frente</b> da base. Aperte <span class=ui>Esc</span> para fechar o Alinhar.",
    ck="O batente está na beirada da frente da base, de lado a lado.",
    sos=[("O batente foi para o meio","Você clicou na bolinha do <b>meio</b>. A que alinha na frente é a de <b>baixo</b>.")]),

  dict(n=17, titulo="Esc e Ctrl + A: tudo selecionado", img="aula9/g17_depois.jpg", clipe="seleciona3.gif",
    corpo="Aperte <span class=ui>Esc</span> para fechar o Alinhar. Clique num lugar vazio do plano e aperte <span class=ui>Ctrl</span> + <span class=ui>A</span>: as <b>três</b> peças ficam selecionadas, <span class=ui>Shapes(3)</span>.",
    ck="O painel diz <span class=ui>Shapes(3)</span>: base, encosto e batente selecionados.",
    sos=[("O painel diz outro número","Clique num lugar vazio e aperte Ctrl + A de novo.")]),

  dict(n=18, titulo="Agrupe: Grupo de união", img="aula9/g18_depois.jpg", clipe="uniao.gif",
    corpo="Na barra de cima há três botõezinhos de juntar peças, à direita do meio. Clique no <b>do meio</b>, o <span class=ui>Grupo de união</span>.<br><br>As três peças viram <b>uma só</b>: o painel diz <span class=ui>Union</span>.",
    ck="O porta-celular é uma peça só, e o painel diz <span class=ui>Union</span>.",
    sos=[("O painel não mudou","Clique no botão do meio dos três, o <span class=ui>Grupo de união</span>.")]),

  dict(n=19, titulo="Gire a câmera: veja de lado", img="aula9/g19_depois.jpg", clipe="girar.gif",
    corpo="Clique num lugar vazio. Segure o botão <b>direito</b> do mouse em cima do <b>plano de trabalho</b> e arraste um pouco para a direita e para cima.<br><br>A câmera <b>gira</b> e você vê o porta-celular de lado: a base, o encosto <b>inclinado para trás</b> e o batente na frente. É onde o celular se apoia.",
    ck="De lado se vê o encosto inclinado para trás, a base e o batente baixinho na frente.",
    sos=[("A peça saiu do lugar","Você usou o botão <b>esquerdo</b>. Aperte Ctrl + Z e repita com o <b>direito</b>."),
         ("A câmera foi longe","Use a casinha da barra da esquerda para voltar à vista inicial.")]),

  dict(n=20, titulo="Dê um nome ao seu projeto", img="aula9/g20_depois.jpg", clipe="batiza.gif",
    corpo="Clique na <b>casinha</b> da barra da esquerda para voltar à vista inicial. Depois clique no <b>nome do projeto</b>, no canto de cima à esquerda, apague, escreva <b>Porta-celular da ANA</b> (ou o seu nome) e aperte <span class=ui>Enter</span>.<br><br>O Tinkercad salva sozinho. O porta-celular está guardado na sua conta.",
    ck="No canto de cima à esquerda aparece o <b>nome que você escreveu</b>.",
    sos=[("O nome não mudou","Falta o <span class=ui>Enter</span>."),
         ("O campo não abriu","Clique <b>em cima das letras</b> do nome.")]),
 ],
}
