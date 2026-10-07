# -*- coding: utf-8 -*-
"""Aula 1 — Chaveiro com o seu nome: a primeira peça 3D no Tinkercad.

Tudo o que esta aula afirma sobre a tela foi MEDIDO na bancada (fonte/cap1.py),
não lembrado. Três coisas desta aula ninguém acerta de cabeça, e estão aqui
porque a máquina tropeçou nelas primeiro:

  · o número grande vai em LARGURA, não em Comprimento (passos 7 e 8);
  · o campo do nome chama «Text», em inglês, num painel todo em português (11);
  · a caixinha do furo nasce EM CIMA da plaquinha e precisa descer (15).
"""

AULA = {
 "n": 1,
 "slug": "aula1",
 "titulo": "Chaveiro com o seu nome",
 "subtitulo": "Você vai desenhar em 3D uma plaquinha com o seu nome em relevo e um furo para passar a argola.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 1 · sua primeira peça 3D",
 "fim": "Acabou a Aula 1. Você modelou uma peça de verdade: uma plaquinha com medidas suas, o seu nome em relevo e um furo que atravessa. Ela está salva na sua conta com o nome que você deu — amanhã é só abrir o Tinkercad e ela está lá, do jeitinho que você deixou.",
 "avisos": [
   ("Tudo no navegador", "O Tinkercad roda dentro do navegador, sem instalar nada. Você precisa estar com a sua conta aberta — se aparecer <span class=ui>Entrar</span> no canto de cima, entre antes de começar."),
   ("Nada de impressora", "Hoje a peça fica na tela. Ela é 3D de verdade: dá para girar e olhar por baixo. Imprimir é outra conversa, para outro dia."),
   ("Milímetros", "Todo número desta aula é em milímetro. <b>90 mm</b> é um pouco menos que a largura da sua mão aberta; <b>4 mm</b> é a espessura de umas quatro folhas de papel grossas."),
   ("Os clipes", "Os passos com animação mostram o gesto inteiro: o mouse andando, o <b>botão certo acendendo</b> e o que muda na tela. Dá para trocar para a foto nas abas."),
   ("Travou?", "Todo passo tem um quadro laranja embaixo com o conserto dos erros mais comuns."),
 ],
 "passos": [

  dict(n=1, titulo="Abra o Tinkercad", img="aula1/d01_site.jpg", clipe=None,
    corpo="No navegador, vá para <span class=ui>tinkercad.com</span>.<br><br>Esta é a página de entrada. No canto de cima à direita há dois botões: <span class=ui>Fazer login</span>, para quem já tem conta, e <span class=ui>Inscrever-se</span>, para criar uma.<br><br>Clique em <span class=ui>Fazer login</span> e entre com a sua conta.<br><br>Sem entrar, você até consegue mexer, mas <b>nada fica salvo</b>: ao fechar a aba, a peça some.",
    ck="Você entrou: no canto de cima à direita, no lugar dos dois botões, agora aparece a bolinha da sua conta.",
    sos=[("Não tenho conta","Chame o professor. Se a escola te deu um código de turma, ele vai te dizer onde usá-lo — não clique em <span class=ui>Inscrever-se</span> por conta própria."),
         ("Esqueci minha senha","Chame o professor antes de criar outra conta. Conta nova começa vazia, e o que você fez na aula passada fica na antiga."),
         ("Minha página abriu em inglês","Acontece quando o navegador está configurado em outro idioma. Role até o rodapé da página e troque o idioma para <b>Português</b>: todos os nomes desta aula são os de português.")]),

  dict(n=2, titulo="Clique no botão Criar", img="aula1/d02_depois.jpg", clipe="criar.gif",
    corpo="No canto de cima à direita, ao lado da bolinha da sua conta, clique no botão branco <span class=ui>+ Criar</span>.<br><br>Abre um menuzinho com três linhas.",
    ck="Abriu um quadro branco embaixo do botão, com três opções escritas: <span class=ui>Projeto 3D</span>, <span class=ui>Circuitos</span> e <span class=ui>Codeblocks</span>.",
    sos=[("Não acho o botão Criar","Ele fica na <b>faixa azul</b> do alto da página, bem à direita, logo antes da bolinha da sua conta. Se a janela estiver estreita, aumente o tamanho dela."),
         ("Cliquei e não abriu nada","Clique uma vez só, em cima da palavra <span class=ui>Criar</span>. Dois cliques rápidos abrem e fecham o menu na mesma hora."),
         ("Abriu outra coisa","Você clicou na bolinha da conta, que fica ao lado. Feche apertando <span class=ui>Esc</span> e clique um pouco mais para a esquerda.")]),

  dict(n=3, titulo="Escolha Projeto 3D", img="aula1/d03_marcado.jpg", clipe=None,
    corpo="No menuzinho que abriu, clique na <b>primeira linha</b>: <span class=ui>Projeto 3D</span> — a do desenho de cubo, marcada de vermelho na figura.<br><br>As outras duas são outros mundos do Tinkercad: <span class=ui>Circuitos</span> é para montar circuito com fio e placa, e <span class=ui>Codeblocks</span> é para construir peça com blocos de programação. Hoje é a primeira.<br><br>O Tinkercad abre o editor e já dá ao seu projeto um <b>nome sorteado</b>, meio esquisito, tipo <i>Shiny Jaban-Turing</i>. Deixe assim: no último passo você troca.",
    ck="A página mudou: sumiu a faixa azul e apareceu um <b>plano azul claro quadriculado</b> no meio da tela.",
    sos=[("Cliquei em Circuitos sem querer","Volte com a seta ⟵ do navegador e clique de novo em <span class=ui>+ Criar</span>, escolhendo a primeira linha."),
         ("A tela ficou branca e não carrega","O Tinkercad é pesado. Espere até meio minuto. Se continuar branca, recarregue com <span class=ui>F5</span>."),
         ("Abriu um projeto que eu já tinha","Você clicou numa capa da lista em vez do botão. Volte e use o <span class=ui>+ Criar</span> do canto de cima.")]),

  dict(n=4, titulo="Conheça a tela", img="aula1/p03_tela.jpg", clipe=None,
    corpo="Antes de construir, repare em quatro lugares:<br><br><b>1.</b> O <b>plano azul quadriculado</b> do meio é a sua mesa de trabalho. É em cima dele que tudo acontece.<br><b>2.</b> A <b>coluna da direita</b> é a palheta de formas: cubo, cilindro, esfera, cone, letras. É de lá que você puxa as peças.<br><b>3.</b> A <b>barra da esquerda</b> tem a <b>casinha</b> (volta a câmera para a posição inicial), o <b>+</b> e o <b>−</b> (aproxima e afasta).<br><b>4.</b> No canto de cima à esquerda está o <b>nome do projeto</b>, aquele sorteado. O Tinkercad salva sozinho o tempo todo; você não precisa apertar nada para salvar.",
    ck="Você consegue apontar na tela: o plano quadriculado, a coluna de formas da direita e a casinha da barra da esquerda.",
    sos=[("Minha coluna de formas está fechada","Clique na setinha <span class=ui>›</span> que fica na beirada direita do plano, na metade da altura."),
         ("O plano está torto ou muito longe","Clique na <b>casinha</b> da barra da esquerda: ela devolve a câmera para a posição de começo."),
         ("Está tudo em inglês","Role a página até o rodapé e troque o idioma para Português. Os nomes desta aula são os de português.")]),

  dict(n=5, titulo="Arraste uma Caixa para o plano", img="aula1/g04_depois.jpg", clipe="caixa.gif",
    corpo="Na coluna da direita, a primeira forma de cima é o <b>cubo vermelho</b>, com o nome <span class=ui>Caixa</span> embaixo.<br><br>Segure o botão esquerdo em cima dele, <b>arraste até o meio do plano</b> e solte.<br><br>Um cubo vermelho aparece no plano, já selecionado — dá para ver os quadradinhos brancos nos cantos dele.",
    ck="Tem um cubo vermelho no meio do plano, com quadradinhos brancos em volta, e abriu um painel branco escrito <span class=ui>Caixa</span> no alto.",
    sos=[("Arrastei e não caiu nada","Segure o botão um instante <b>antes</b> de começar a arrastar. Soltar muito rápido o Tinkercad entende como clique."),
         ("Peguei o cilindro","Sem problema: clique nele e aperte <span class=ui>Delete</span>, depois pegue o cubo, que é a primeira forma da coluna."),
         ("Caiu fora do plano","Clique em cima dele e arraste para dentro do quadriculado. Peça fora do plano não entra na peça final.")]),

  dict(n=6, titulo="Veja o painel de propriedades", img="aula1/p05_painel.jpg", clipe=None,
    corpo="Com a caixa selecionada, abriu um painel branco no canto de cima à direita do plano. Ele é o painel da forma, e aqui é onde a modelagem de verdade acontece.<br><br>Repare em duas partes:<br><br><b>1.</b> Em cima, duas bolinhas: <span class=ui>Sólido</span> (a vermelha, marcada) e <span class=ui>Orifício</span> (a listrada). Guarde esse par — no passo 14 ele é a aula inteira.<br><b>2.</b> Embaixo, em <span class=ui>Propriedades</span>, três campos com número: <span class=ui>Comprimento</span>, <span class=ui>Largura</span> e <span class=ui>Altura</span>. Todos marcam <b>20</b>, porque a caixa nasce com 20 mm de lado.<br><br>É digitando nesses três campos que a gente dá à peça o tamanho que quer — <b>não</b> puxando os quadradinhos com o mouse. Número é exato; mão treme.",
    ck="O painel mostra <span class=ui>Comprimento</span>, <span class=ui>Largura</span> e <span class=ui>Altura</span>, os três com <b>20</b>.",
    sos=[("O painel sumiu","Você clicou fora da caixa e ela foi desmarcada. Clique uma vez em cima da caixa e o painel volta."),
         ("Meu painel mostra Lados e Chanfro","Isso é o painel do <b>cilindro</b>, não o da caixa — e ele não tem campo de comprimento nenhum. Apague a peça com <span class=ui>Delete</span> e pegue a primeira forma da coluna, o cubo."),
         ("Os campos estão acinzentados","Clique uma vez dentro do campo para ele aceitar número.")]),

  dict(n=7, titulo="Comprimento = 30", img="aula1/g06_depois.jpg", clipe="comprimento.gif",
    corpo="No painel, clique dentro do campo <span class=ui>Comprimento</span>, apague o <b>20</b> e escreva <b>30</b>. Aperte <span class=ui>Enter</span>.<br><br>A caixa fica mais funda — ela cresce na direção que vai <b>para longe de você</b> na tela.<br><br>Esses 30 mm vão ser a <b>altura da plaquinha de cima a baixo</b>, a medida que dá espaço para as letras não ficarem espremidas.",
    ck="O campo <span class=ui>Comprimento</span> mostra <b>30</b> e a caixa ficou visivelmente mais funda que larga.",
    sos=[("Apertei Enter e voltou para 20","O campo não tinha sido selecionado. Dê dois cliques dentro dele para marcar o número todo e escreva por cima."),
         ("Digitei 30 e a caixa não mudou","Falta o <span class=ui>Enter</span>, ou falta clicar fora do campo. O Tinkercad só aplica quando você confirma."),
         ("Escrevi 300 sem querer","A caixa virou uma lousa gigante. Escreva 30 de novo e aperte Enter; nada quebrou.")]),

  dict(n=8, titulo="Largura = 90 (o lado comprido)", img="aula1/g07_depois.jpg", clipe="largura.gif",
    corpo="Agora o campo <span class=ui>Largura</span>: apague o <b>20</b> e escreva <b>90</b>. Aperte <span class=ui>Enter</span>.<br><br>A caixa se estica <b>para os lados</b> e vira uma plaquinha deitada. Esse é o lado comprido, o que vai receber o nome.<br><br>Olhe para o nome dos campos e desconfie: o lado <b>comprido</b> da sua peça saiu do campo chamado <span class=ui>Largura</span>, não do chamado <span class=ui>Comprimento</span>. Não é erro seu nem do Tinkercad: <i>comprimento</i> e <i>largura</i> aqui são só os nomes de <b>duas direções fixas da mesa</b> — uma vai para longe de você, a outra vai para os lados. Qual delas fica maior é você quem decide.",
    ck="A peça agora é uma plaquinha <b>deitada</b>, bem mais larga que funda, com <span class=ui>Largura</span> em <b>90</b> e <span class=ui>Comprimento</span> em <b>30</b>.",
    sos=[("Minha plaquinha ficou apontando para longe, em pé na tela","Você trocou os dois números: pôs o 90 no <span class=ui>Comprimento</span>. Ponha <b>30</b> no Comprimento e <b>90</b> na Largura. Se ficar como está, no passo 10 o nome vai entrar atravessado na peça."),
         ("A plaquinha saiu da tela","Ela cresceu mais que a janela. Clique no <b>−</b> da barra da esquerda duas vezes para afastar a câmera."),
         ("Digitei 90 na Altura","Virou um bloco alto em vez de uma plaquinha. Ponha a Altura de volta em 20 por enquanto — o passo 9 cuida dela.")]),

  dict(n=9, titulo="Altura = 4 (fina feito uma plaquinha)", img="aula1/g08_depois.jpg", clipe="altura.gif",
    corpo="Último campo: <span class=ui>Altura</span>. Apague e escreva <b>4</b>. Aperte <span class=ui>Enter</span>.<br><br>O bloco murcha e vira uma <b>plaquinha fina</b>, de 4 mm — a espessura de um chaveiro de verdade.<br><br>Pronto: 90 × 30 × 4. A sua peça já tem as três medidas, e todas foram você que escolheu.",
    ck="Sobrou uma plaquinha vermelha fina e deitada no meio do plano. Os três campos mostram <b>30</b>, <b>90</b> e <b>4</b>.",
    sos=[("Ficou fina demais para ver","Está certo: 4 mm é fino mesmo. Clique no <b>+</b> da barra da esquerda para aproximar."),
         ("Escrevi 0","O Tinkercad não aceita zero e devolve o número anterior. Escreva 4."),
         ("Quero mais grossa","Pode: 5 ou 6 também funciona. Só não passe de 8, senão o furo do passo 15 precisa descer mais do que a aula manda.")]),

  dict(n=10, titulo="Arraste a forma Texto para cima da plaquinha", img="aula1/g09_depois.jpg", clipe="texto.gif",
    corpo="Role a coluna da direita até achar a forma <span class=ui>Texto</span> — é a que já vem com umas letras vermelhas desenhadas nela.<br><br>Arraste ela e <b>solte bem no meio da plaquinha</b>.<br><br>Vai aparecer a palavra <b>TEXT</b> em pé sobre a peça, e um <b>quadrado verde claro</b> embaixo. Esse quadrado verde não é defeito: é o Tinkercad avisando que você soltou uma peça <b>em cima da face de outra</b>, e que agora aquela face virou a mesa. Ele some sozinho mais adiante.",
    ck="A palavra <span class=ui>TEXT</span> está em relevo sobre a plaquinha, e o painel do alto mudou de <span class=ui>Caixa</span> para <span class=ui>Texto</span>.",
    sos=[("Apareceu um quadrado verde e eu me assustei","É só um plano de trabalho novo, criado na face de cima da plaquinha. Ele some e não atrapalha nada."),
         ("O TEXT caiu fora da plaquinha","Clique em cima da palavra e arraste até o meio da peça. Se ela não chegar lá, afaste a câmera com o <b>−</b>."),
         ("Não acho a forma Texto","Role a coluna da direita para baixo. Ela fica umas quatro fileiras abaixo do cubo, com umas letras vermelhas inclinadas.")]),

  dict(n=11, titulo="Escreva o seu nome no campo Text", img="aula1/g10_depois.jpg", clipe="nome.gif",
    corpo="No painel da direita, o primeiro campo se chama <span class=ui>Text</span> — <b>em inglês mesmo</b>, no meio de um painel todo em português. Ele está logo abaixo das duas bolinhas, e dentro dele está escrito <i>TEXT</i>.<br><br>Clique dentro do campo, apague e escreva <b>o seu nome</b>, em maiúsculas. Aperte <span class=ui>Tab</span>.<br><br>As letras em relevo na plaquinha trocam na hora.<br><br>Nome curto cabe folgado. Se o seu for comprido, a aula continua igual — o passo 12 avisa o que fazer.",
    ck="O seu nome aparece em relevo sobre a plaquinha, lendo da esquerda para a direita.",
    sos=[("Não acho o campo Text","Procure a palavra em <b>inglês</b>: <span class=ui>Text</span>, sem o O. A palavra <i>Texto</i> que aparece mais acima é o <b>título do painel</b>, o nome da forma — aquilo não é campo, não dá para escrever nele."),
         ("Meu nome ficou maior que a plaquinha","Duas saídas: ou aumente a <span class=ui>Largura</span> da plaquinha (volte ao passo 8 e ponha 120), ou clique na palavra e puxe um quadradinho branco do canto para encolher as letras."),
         ("As letras ficaram atravessadas na peça","A plaquinha está virada: volte ao passo 8 e confira <span class=ui>Largura</span> em <b>90</b> e <span class=ui>Comprimento</span> em <b>30</b>."),
         ("Apertei Enter e fechou tudo","Nada se perdeu. Clique na palavra de novo e o painel volta.")]),

  dict(n=12, titulo="Traga uma segunda Caixa para a ponta esquerda", img="aula1/g11_depois.jpg", clipe="caixa2.gif",
    corpo="Agora o furo da argola. E aqui vem a ideia mais bonita do Tinkercad: <b>para fazer um buraco, você põe uma peça</b>.<br><br>Volte à coluna da direita, pegue o <span class=ui>Caixa</span> de novo e solte na <b>ponta esquerda da plaquinha</b>, no espaço vazio antes da primeira letra.<br><br>Ela cai em cima da peça, grandona. É assim mesmo — os dois próximos passos arrumam o tamanho e a altura.",
    ck="Tem um segundo cubo vermelho pousado na ponta esquerda da plaquinha, e o painel do alto voltou a dizer <span class=ui>Caixa</span>.",
    sos=[("Solte em cima da letra sem querer","Clique no cubo novo e arraste para a ponta vazia. Se encostar nas letras, o furo vai comer um pedaço do seu nome."),
         ("Por que não um cilindro, para o furo ficar redondo?","Porque o painel do cilindro só tem <span class=ui>Lados</span>, <span class=ui>Chanfro</span> e <span class=ui>Segmentos</span> — ele <b>não tem</b> campo de comprimento nem de largura, e você não conseguiria dar o tamanho exato. E furo não precisa ser redondo: quadrado segura argola igual."),
         ("Ele sumiu atrás da plaquinha","Clique na <b>casinha</b> da barra da esquerda para voltar a câmera ao lugar de sempre.")]),

  dict(n=13, titulo="Encolha a caixinha para 8 × 8", img="aula1/g12_depois.jpg", clipe="encolhe.gif",
    corpo="Com a caixinha nova selecionada, no painel da direita:<br><br><b>1.</b> <span class=ui>Comprimento</span>: escreva <b>8</b> e aperte Enter.<br><b>2.</b> <span class=ui>Largura</span>: escreva <b>8</b> e aperte Enter.<br><br>A <span class=ui>Altura</span> <b>deixe como está</b>, em 20. Ela precisa ser mais alta que a plaquinha — você vai entender no passo 15.<br><br>Agora é um palitinho fino de 8 × 8 mm em pé na ponta da peça. É o tamanho de um furo que a argola de chaveiro atravessa.",
    ck="A caixinha virou um palitinho fino e alto, sobrando na ponta esquerda da plaquinha sem encostar nas letras.",
    sos=[("Mudei a Altura para 8 também","Então o furo pode ficar raso. Ponha a Altura de volta em <b>20</b>."),
         ("Mudei o tamanho da plaquinha sem querer","Você estava com a peça errada selecionada. Clique uma vez no palitinho e confira: o painel tem de mostrar 8, 8 e 20."),
         ("O palitinho ficou encostado nas letras","Clique nele e arraste um pouco mais para a esquerda, para o espaço vazio.")]),

  dict(n=14, titulo="Transforme a caixinha em Orifício", img="aula1/g13_depois.jpg", clipe="orificio.gif",
    corpo="Aqui está o truque que faz o Tinkercad inteiro funcionar.<br><br>No alto do painel, ao lado da bolinha vermelha <span class=ui>Sólido</span>, clique na bolinha <b>listrada</b>, escrita <span class=ui>Orifício</span>.<br><br>O palitinho fica <b>listradinho e transparente</b>. Ele não virou buraco ainda — ele virou uma <b>peça com a função de cavar</b>. Quem cava é o passo 17.<br><br>Toda peça do Tinkercad pode ser as duas coisas: material que soma, ou vazio que subtrai. É com isso que se faz anel, caneca, encaixe, engrenagem.",
    ck="O palitinho ficou <b>listrado e meio transparente</b>, em vez de vermelho cheio.",
    sos=[("Não acho a bolinha Orifício","Ela é a <b>segunda</b> das duas bolinhas do alto do painel, a da direita, com riscos diagonais. A palavra embaixo dela é pequena."),
         ("Cliquei e a plaquinha inteira ficou listrada","Você estava com a plaquinha selecionada, não com o palitinho. Clique na bolinha <span class=ui>Sólido</span> para desfazer, depois clique no palitinho e tente de novo."),
         ("Ficou listrado mas não apareceu buraco nenhum","Está certo assim. O buraco só aparece no passo 17, quando as peças forem juntadas.")]),

  dict(n=15, titulo="Faça o furo DESCER: Ctrl + ↓, seis vezes", img="aula1/g14_depois.jpg", clipe="desce.gif",
    corpo="Este é o passo que ninguém adivinha — e sem ele a peça sai errada.<br><br>Lembra do quadrado verde do passo 10? Quando você soltou a caixinha em cima da plaquinha, o Tinkercad pôs a mesa <b>no alto dela</b>. Então o seu furo não está <i>dentro</i> da plaquinha: ele está <b>pousado em cima</b>, só encostando. Juntar assim não cava nada.<br><br>Com o palitinho ainda selecionado, segure <span class=ui>Ctrl</span> e aperte a <b>seta para baixo</b> <span class=ui>↓</span> <b>seis vezes</b>. Cada toque desce 1 mm.<br><br>Olhe a animação: o palitinho afunda e atravessa a plaquinha, sobrando um pedacinho embaixo. É isso que você quer. Um furo tem de sair do outro lado.",
    depois="Em computador Mac, use <span class=ui>Ctrl</span> do mesmo jeito — nesse atalho ele vale nos dois.",
    ck="O palitinho listrado <b>atravessou</b> a plaquinha: dá para ver uma pontinha dele aparecendo por baixo da peça.",
    sos=[("Apertei a seta e a peça andou para o lado","Você soltou o <span class=ui>Ctrl</span>. Seta sozinha anda no plano; <b>com Ctrl</b> é que sobe e desce. Traga a peça de volta com a seta contrária e tente de novo segurando o Ctrl."),
         ("Desceu demais e sumiu","Aperte <span class=ui>Ctrl</span> e a <b>seta para cima</b> ↑ algumas vezes até ele reaparecer."),
         ("Não sei se atravessou","Gire a câmera: segure o <b>botão direito</b> do mouse em cima do plano e arraste um pouquinho. Olhando de lado dá para ver se a pontinha sai por baixo."),
         ("Não desce nada","Clique uma vez no palitinho antes, para selecioná-lo. Atalho de teclado só vale para a peça que está marcada.")]),

  dict(n=16, titulo="Selecione tudo: Ctrl + A", img="aula1/g15_depois.jpg", clipe="seleciona.gif",
    corpo="Agora é hora de juntar as três peças: a plaquinha, as letras e o furo.<br><br>Clique uma vez num <b>espaço vazio</b> do plano, para nada ficar marcado. Depois segure <span class=ui>Ctrl</span> e aperte <span class=ui>A</span>.<br><br>Tudo que está no plano fica selecionado de uma vez: aparece um retângulo pontilhado em volta do conjunto inteiro.<br><br>Em computador Mac, é <span class=ui>Cmd</span> + <span class=ui>A</span>.",
    ck="Tem um retângulo pontilhado em volta da peça toda, e o painel do alto mudou para <span class=ui>Shapes</span> com um número — o número de peças marcadas, que tem de ser <b>3</b>.",
    sos=[("O painel diz Shapes(2)","Faltou uma peça. Quase sempre é o furo, que foi parar longe. Clique em cada pedaço com <span class=ui>Shift</span> apertado para marcar os três na mão."),
         ("Marcou coisa que eu não quero","Clique num espaço vazio para desmarcar tudo e comece de novo. Se tiver peça sobrando no plano, apague com <span class=ui>Delete</span> antes."),
         ("Ctrl + A não faz nada","Clique uma vez dentro do plano antes, para o teclado ir para lá.")]),

  dict(n=17, titulo="Agrupe: Grupo de união", img="aula1/g16_depois.jpg", clipe="uniao.gif",
    corpo="Na barra de cima, à direita do meio, há três botõezinhos de juntar peças. Passe o mouse em cima deles sem clicar: aparece o nome de cada um.<br><br>Clique no do meio, <span class=ui>Grupo de união</span>. É esse — o da esquerda é <span class=ui>Grupo do conjunto</span>, que só amarra as peças sem fundir, e <b>não cava furo nenhum</b>.<br><br>Na hora, as três peças viram uma só, tudo numa cor só, e o <b>buraco aparece</b>.<br><br>Ficou tudo cinza ou de uma cor que você não escolheu? É normal: ao fundir, o Tinkercad adota uma cor única para a peça inteira.",
    depois="Errou e quer voltar? <span class=ui>Ctrl</span> + <span class=ui>Shift</span> + <span class=ui>G</span> desagrupa e devolve as peças separadas, do jeito que estavam.",
    ck="Virou <b>uma peça só</b>, de uma cor só, e o painel do alto agora diz <span class=ui>Union</span>.",
    sos=[("Juntou mas não tem buraco","O furo não tinha descido. Desagrupe com <span class=ui>Ctrl</span>+<span class=ui>Shift</span>+<span class=ui>G</span>, volte ao passo 15 e desça o palitinho com <span class=ui>Ctrl</span>+↓."),
         ("Cliquei no botão errado e nada fundiu","Você pegou o <span class=ui>Grupo do conjunto</span>. Desagrupe e clique no do meio, o <span class=ui>Grupo de união</span>."),
         ("Sumiu o meu nome","O furo encostou nas letras e comeu uma. Desagrupe, arraste o palitinho mais para a ponta e agrupe de novo."),
         ("Não acho os botões","Eles ficam na <b>barra de cima</b>, no grupo do meio, perto dos ícones de espelhar e alinhar. Passe o mouse devagar que o nome aparece.")]),

  dict(n=18, titulo="Confira: dá para ver o chão pelo furo?", img="aula1/p17_pronta.jpg", clipe=None,
    corpo="Clique num espaço vazio do plano para tirar a moldura de seleção da frente e olhe a sua peça.<br><br>Esta é a conferência da aula inteira, e é uma só: <b>olhe pelo furo</b>. Se dá para enxergar o quadriculado do plano através dele, o furo atravessou e a peça está certa.<br><br>Se o furo só parece um risco desenhado em cima da plaquinha, ele não atravessou — e o conserto está no quadro laranja.",
    ck="Dá para ver o <b>plano azul quadriculado</b> através do furo, e o seu nome continua inteiro, sem letra faltando.",
    sos=[("O furo parece só um risco","Ele não atravessou. Desagrupe com <span class=ui>Ctrl</span>+<span class=ui>Shift</span>+<span class=ui>G</span>, clique no palitinho listrado, desça com <span class=ui>Ctrl</span>+↓ mais seis vezes e agrupe de novo."),
         ("Falta uma letra do meu nome","O furo pegou nela. Desagrupe, arraste o palitinho mais para a ponta esquerda e agrupe outra vez."),
         ("O furo ficou enorme","Desagrupe, clique no palitinho e ponha <span class=ui>Comprimento</span> e <span class=ui>Largura</span> em <b>8</b>."),
         ("Está tudo certo e eu quero outra cor","Clique na peça e, no painel, clique na bolinha <span class=ui>Sólido</span>: abre a cartela de cores.")]),

  dict(n=19, titulo="Gire a câmera — e volte com a casinha", img="aula1/g18_depois.jpg",
    clipe=[("Girar", "girar.gif"), ("Voltar", "vista_inicial.gif")],
    corpo="Sua peça é 3D de verdade, não um desenho. Prove isso:<br><br><b>1.</b> Segure o <b>botão direito</b> do mouse em cima do <b>plano de trabalho</b> (o quadriculado azul) e arraste devagar. O mundo gira em volta da peça — dá para olhar de lado, de cima e por baixo. Gire até ver a peça de perfil e confira a espessura: aqueles 4 mm do passo 9 estão ali.<br><b>2.</b> Para desfazer a bagunça, na barra da esquerda clique na <b>casinha</b>, a primeira figura de cima. A câmera volta na hora para a posição do começo.<br><br>Repare no primeiro clipe: é o botão <b>direito</b> que acende. Com o esquerdo você não gira a câmera — você <b>arrasta a peça</b> e tira ela do lugar.<br><br>Guarde a casinha. Ela é a saída de toda confusão de câmera: girou demais, perdeu a peça de vista, não acha nada — clique na casinha.",
    ck="Você girou a peça, viu a espessura dela de lado, e depois a casinha trouxe tudo de volta ao ângulo do começo.",
    sos=[("Arrastei e a peça saiu do lugar","Você usou o botão esquerdo. Desfaça com <span class=ui>Ctrl</span>+<span class=ui>Z</span> e tente com o <b>direito</b>."),
         ("Meu mouse não tem botão direito","No trackpad do notebook, use <b>dois dedos</b> ao mesmo tempo para arrastar. No Chromebook, segure <span class=ui>Alt</span> e arraste."),
         ("Cliquei na casinha e a peça continua sumida","Então ela ficou longe do centro do plano. Use o botão logo abaixo da casinha, o do losango, que enquadra tudo o que existe no plano."),
         ("Cliquei no + sem querer","Ele só aproxima. Clique no <b>−</b> para voltar, ou na casinha para acertar tudo de uma vez.")]),

  dict(n=20, titulo="Dê um nome ao seu projeto", img="aula1/g20_depois.jpg", clipe="batiza.gif",
    corpo="Falta uma coisa só. No canto de cima à esquerda está aquele nome sorteado que o Tinkercad deu no passo 3.<br><br>Clique em cima dele: o nome vira um campo de escrever. Apague e escreva <b>Chaveiro da</b> e o seu nome. Aperte <span class=ui>Enter</span>.<br><br>Não é enfeite. Daqui a um mês você vai ter dez projetos na lista, e procurar entre dez nomes sorteados é procurar agulha. O Tinkercad já salvou tudo sozinho — o que faltava era você poder <b>achar</b> de novo.",
    ck="No canto de cima à esquerda está o nome que você escolheu, no lugar do nome sorteado.",
    sos=[("Cliquei e não vira campo de escrever","Clique bem em cima das letras do nome, não no quadradinho colorido do lado."),
         ("Apaguei tudo e ficou sem nome","O Tinkercad devolve o nome antigo. Clique de novo e escreva."),
         ("Como abro isso amanhã?","Vá em <span class=ui>tinkercad.com</span>, entre na sua conta, clique em <span class=ui>Projetos</span> na coluna da esquerda e procure pelo nome que você acabou de dar.")]),
 ],
}
