# -*- coding: utf-8 -*-
"""Aula 12 — Projeto livre e mostra: o caminho de um projeto próprio, com um totem de exemplo.

Medido na bancada (fonte/cap12.py). A aula NÃO manda baixar nem publicar nada: os
diálogos «Enviar para» e «Exportar» só são ABERTOS e lidos. Pegadinhas:
  · cilindro e cone soltos na tampa nascem CENTRADOS; mudar só a altura mantém o
    centro (mudar a base cresce a partir do canto: por isso a coluna e o chapéu
    têm base 20 — a que já nascem);
  · agrupar apagaria as cores (Aula 7): o totem fica SOLTO;
  · a base verde (e não azul): azul e vermelho têm brilho parecido e o clipe não
    «via» a mudança.
"""
import ast
INTRO = ast.literal_eval(open(__file__.replace("conteudo_a12.py", "_intro12.txt")).read())

AULA = {
 "n": 12,
 "slug": "aula12",
 "titulo": "Projeto livre e mostra",
 "subtitulo": "O caminho de um projeto seu, do rabisco ao arquivo: planejar, montar com cores, conferir de todos os lados e mostrar.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 12 · projeto livre e mostra",
 "fim": "Acabou a Aula 12 — e acabou o curso. Em doze aulas você fez um <b>chaveiro</b>, um <b>porta-lápis</b>, uma <b>caneca</b>, uma <b>casinha</b>, um <b>carrinho</b>, um <b>foguete</b>, um <b>robô</b>, um <b>dado</b>, um <b>porta-celular</b>, uma <b>régua</b>, um <b>encaixe</b> e um <b>totem</b>. O mesmo método serviu para todos: <b>formas</b> básicas, <b>medidas</b> exatas, <b>buracos</b>, <b>Alinhar</b>, <b>cópias</b> e <b>cores</b>. O totem está salvo na sua conta com o nome que você deu. <b>O seu projeto livre vem agora:</b> escolha um objeto da sua casa, desenhe no papel, e monte com as mesmas ferramentas.",
 "avisos": [
   ("Aula de projeto", "O totem é o <b>exemplo</b>. Na sua vez, escolha <b>o seu</b>: um bicho, uma casa, um robô, um foguete. O roteiro serve para qualquer um."),
   ("Nada é publicado hoje", "Os botões <span class=ui>Enviar para</span> e <span class=ui>Exportar</span> abrem janelas com as opções. A aula só <b>olha</b> as janelas: nada é baixado nem enviado. Quem decide mostrar para fora é o professor."),
   ("Cor e grupo", "Cada peça tem a <b>sua cor</b>. Se você usar o <span class=ui>Grupo de união</span>, tudo vira uma cor só (Aula 7). Para o totem colorido, <b>não agrupe</b>."),
   ("Os clipes", "Os passos com animação mostram o gesto inteiro: o mouse andando, o <b>botão certo acendendo</b> e as <b>teclas acesas</b> quando o gesto é de teclado."),
   ("Travou?", "Todo passo tem um quadro laranja embaixo com o conserto dos erros mais comuns."),
 ],
 "passos": INTRO + [

  dict(n=4, titulo="PLANEJE antes de montar", img="aula12/p01_vazio.jpg", clipe=None,
    corpo="Antes de arrastar qualquer forma, <b>desenhe no papel</b> o que você vai fazer, <b>visto de frente</b>, com as <b>formas</b> do Tinkercad: caixa, cilindro, esfera, cone, telhado.<br><br>O exemplo de hoje é um <b>totem</b>: uma <b>base</b> larga, uma <b>coluna</b> e um <b>chapéu</b> de cone. Três peças, três cores.<br><br>Escreva do lado de cada peça: a <b>forma</b>, os <b>três números</b> (comprimento, largura, altura) e a <b>cor</b>. O plano azul vazio é o que você tem agora.",
    ck="Você tem um desenho no papel com as peças, as medidas e as cores. (O editor está vazio, esperando.)",
    sos=[("Não sei o que fazer","Olhe ao redor: uma garrafa é um cilindro, uma casa tem caixa e telhado, um sorvete é cone e esfera. Escolha algo simples, de 3 ou 4 peças."),
         ("O desenho ficou grande demais","Tudo bem: reduza. Um projeto de 3 peças bem-feitas vale mais que um de 20 pela metade.")]),

  dict(n=5, titulo="Arraste uma Caixa: a base", img="aula12/g02_depois.jpg", clipe="caixa.gif",
    corpo="Na coluna da direita, a forma <b>vermelha</b> do meio da segunda fileira, à esquerda, é a <span class=ui>Caixa</span>. Segure o botão esquerdo nela, <b>arraste até o meio do plano</b> e solte.",
    ck="Tem um cubo vermelho no meio do plano e o painel diz <span class=ui>Caixa</span>.",
    sos=[("Peguei a caixa cinza listrada","Essa é o <b>buraco</b>. Aperte <span class=ui>Delete</span> e arraste a vermelha.")]),

  dict(n=6, titulo="Base: Comprimento 40, Largura 40, Altura 10", img="aula12/g03_depois.jpg", clipe="medidas_base.gif",
    corpo="No painel, escreva <b>40</b> em <span class=ui>Comprimento</span>, <b>40</b> em <span class=ui>Largura</span> e <b>10</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada). Uma placa quadrada e baixa.",
    ck="O cubo virou uma placa quadrada e baixa.",
    sos=[("Digitei e nada mudou","Falta o <span class=ui>Enter</span> depois de cada número.")]),

  dict(n=7, titulo="Pinte a base de verde", img="aula12/g04_depois.jpg", clipe="azul.gif",
    corpo="No painel, clique na <b>bolinha vermelha</b> ao lado de <span class=ui>Sólido</span>: abre a janela <span class=ui>Cores sólidas</span>. Na fileira do <b>meio</b>, clique na bolinha <b>verde</b> (a quarta). Depois, <b>clique de novo na bolinha de cor</b> para fechar a janela.",
    ck="A base está verde, e a bolinha do painel também.",
    sos=[("Ficou verde-claro","Você pegou a bolinha da fileira de cima. A normal é a do <b>meio</b>."),
         ("A janela não fecha","Clique na bolinha de cor do painel de novo. O Esc não fecha essa janela.")]),

  dict(n=8, titulo="Arraste um Cilindro para a tampa da base", img="aula12/g05_depois.jpg", clipe="cilindro.gif",
    corpo="Clique num lugar vazio. A forma <b>laranja</b> do meio da segunda fileira é o <span class=ui>Cilindro</span>: arraste e solte <b>no meio da tampa</b> da base.<br><br>Ele nasce <b>em cima</b> da base, e <b>centrado</b>: o quadrado verde aparece em volta.",
    ck="Um cilindro laranja está pousado no meio da base verde, com o quadrado verde em volta.",
    sos=[("O cilindro caiu no chão","Você soltou fora da base. Arraste de novo, soltando em cima da <b>tampa</b>."),
         ("Peguei o cilindro cinza listrado","Esse é o buraco. Aperte Delete e arraste o laranja.")]),

  dict(n=9, titulo="Coluna: só a altura, 40", img="aula12/g06_depois.jpg", clipe="medidas_coluna.gif",
    corpo="Clique na <b>alça do canto</b> de cima à esquerda da base do cilindro e confira os dois números: <b>20</b> e <b>20</b> (se for outro, escreva 20). Depois clique na <b>alça do meio da tampa</b> e escreva <b>40</b> na altura (<span class=ui>Enter</span>).<br><br>A base fica em <b>20</b> (o tamanho com que o cilindro nasce): assim a coluna continua <b>centrada</b> na base. Mudar a base é que a tira do centro.",
    ck="O cilindro virou uma coluna alta e fina, no meio da base.",
    sos=[("Os números sumiram","Clique no cilindro e na alça do meio da tampa de novo."),
         ("A coluna saiu torta","Você mexeu na base do cilindro. Aperte Ctrl + Z e mude só a altura.")]),

  dict(n=10, titulo="Pinte a coluna de amarelo", img="aula12/g07_depois.jpg", clipe="amarelo.gif",
    corpo="Com a coluna selecionada, clique na bolinha de cor do painel. Na fileira do meio, clique na bolinha <b>amarela</b> (a terceira). Clique de novo na bolinha de cor para fechar a janela.",
    ck="A coluna está amarela.",
    sos=[("Ficou laranja","A amarela é a <b>terceira</b> da fileira do meio; a laranja é a segunda.")]),

  dict(n=11, titulo="Arraste um Cone para a tampa da coluna", img="aula12/g08_depois.jpg", clipe="cone.gif",
    corpo="Clique num lugar vazio. Na fileira da pirâmide, o <b>cone roxo</b> com o nome <span class=ui>Cone</span>: solte-o <b>no meio da tampa</b> da coluna.",
    ck="Um cone roxo está pousado no meio da tampa da coluna.",
    sos=[("O cone caiu no chão","Você soltou fora da coluna. Arraste de novo para a <b>tampa</b>.")]),

  dict(n=12, titulo="Chapéu: só a altura, 24", img="aula12/g09_depois.jpg", clipe="medidas_cone.gif",
    corpo="Clique na <b>alça do canto</b> da base do cone e confira os dois números: <b>20</b> e <b>20</b> (se for outro, escreva 20). Depois clique na <b>alça do meio da ponta</b> e escreva <b>24</b> na altura (<span class=ui>Enter</span>).<br><br>A base do cone fica em 20, igual à da coluna.",
    ck="O cone ficou um pouco mais alto, com a base do tamanho da coluna.",
    sos=[("Os números sumiram","Clique no cone e na alça do meio da ponta de novo.")]),

  dict(n=13, titulo="Pinte o chapéu de vermelho", img="aula12/g10_depois.jpg", clipe="vermelho.gif",
    corpo="Com o cone selecionado, clique na bolinha de cor do painel. Na fileira do meio, clique na bolinha <b>vermelha</b> (a primeira à esquerda). Clique de novo na bolinha de cor para fechar a janela.",
    ck="O chapéu está vermelho.",
    sos=[("Ficou rosa","A vermelha é a <b>primeira</b> bolinha da fileira do meio.")]),

  dict(n=14, titulo="Selecione tudo: três peças", img="aula12/g11_depois.jpg", clipe="seleciona.gif",
    corpo="Clique num <b>lugar vazio</b> do plano e aperte <span class=ui>Ctrl</span> + <span class=ui>A</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>A</span>). O painel diz <span class=ui>Shapes(3)</span>: base, coluna e chapéu.<br><br><b>Não agrupe!</b> O <span class=ui>Grupo de união</span> apagaria as cores (Aula 7). Clique num lugar vazio para soltar a seleção.",
    ck="O painel diz <span class=ui>Shapes(3)</span>. As três peças têm contorno azul.",
    sos=[("O painel diz outro número","Conte as peças do seu projeto. O totem tem três.")]),

  dict(n=15, titulo="Gire a câmera: veja por trás", img="aula12/g12_depois.jpg", clipe="girar.gif",
    corpo="Segure o botão <b>direito</b> do mouse em cima do <b>plano de trabalho</b> e arraste um pouco para a direita e para cima.<br><br>A câmera <b>gira</b>: confira o seu projeto <b>de todos os lados</b>. É assim que se acha o que ficou torto antes de mostrar.",
    ck="A câmera mudou e o totem aparece de outro lado: base verde, coluna amarela e chapéu vermelho.",
    sos=[("A peça saiu do lugar","Você usou o botão <b>esquerdo</b>. Aperte Ctrl + Z e repita com o <b>direito</b>.")]),

  dict(n=16, titulo="Olhe de frente: o desenho do papel", img="aula12/g13_depois.jpg", clipe="vista_frente.gif",
    corpo="No cubo de vistas, no canto de cima à esquerda, clique na face escrita <span class=ui>FRONTAL</span>.<br><br>De frente é <b>o mesmo desenho que você fez no papel</b>: compare. Se um tamanho não bateu, volte à peça e corrija o número.",
    ck="De frente se vê o totem como no desenho do papel: base larga, coluna e chapéu.",
    sos=[("A câmera não mudou","Clique <b>na palavra</b> FRONTAL do cubinho.")]),

  dict(n=17, titulo="Dê um nome ao seu projeto", img="aula12/g14_depois.jpg", clipe="batiza.gif",
    corpo="Clique na <b>casinha</b> da barra da esquerda para voltar à vista inicial. Depois clique no <b>nome do projeto</b>, no canto de cima à esquerda, apague, escreva <b>Totem da ANA</b> (ou o nome do seu projeto) e aperte <span class=ui>Enter</span>.<br><br>O Tinkercad salva sozinho: o totem fica na sua conta.",
    ck="No canto de cima à esquerda aparece o <b>nome que você escreveu</b>.",
    sos=[("O nome não mudou","Falta o <span class=ui>Enter</span>."),
         ("O campo não abriu","Clique <b>em cima das letras</b> do nome.")]),

  dict(n=18, titulo="MOSTRE: o botão Enviar para", img="aula12/g15_depois.jpg", clipe="enviar.gif",
    corpo="No canto de cima à direita, clique em <span class=ui>Enviar para</span>. Abre uma janela com a <b>imagem do seu projeto</b> (uma foto dele) e, embaixo, opções de enviar para outros programas e para o Google Drive.<br><br>A <b>imagem</b> é o jeito mais fácil de <b>mostrar</b> o projeto: o botãozinho de <b>baixar</b> ao lado dela guarda a foto no computador. <b>Hoje, só olhe:</b> não envie nada para lugar nenhum sem o professor.",
    ck="Abriu a janela <span class=ui>Enviar</span> com a foto do totem e as opções de enviar.",
    sos=[("Não achei o botão","Fica no canto de cima à direita, o último dos três, depois de <span class=ui>Importar</span> e <span class=ui>Exportar</span>."),
         ("A foto está vazia","Espere um segundo: ela carrega.")]),

  dict(n=19, titulo="MOSTRE: o botão Exportar", img="aula12/g16_depois.jpg", clipe="exportar.gif",
    corpo="Feche a janela com o <b>×</b> (ou aperte <span class=ui>Esc</span>). Clique em <span class=ui>Exportar</span>. Abre uma janela com os <b>arquivos</b> do projeto: <span class=ui>.OBJ</span>, <span class=ui>.STL</span> e <span class=ui>GLTF</span>, para <b>impressão 3D</b>, e <span class=ui>.SVG</span>, para <b>corte a laser</b>.<br><br>O <b>.STL</b> é o arquivo que uma impressora 3D lê: ele é a peça pronta para <b>sair do computador</b>. <b>Hoje, só olhe:</b> não baixe. Feche a janela com o <b>×</b>.",
    ck="Abriu a janela com <span class=ui>.OBJ</span>, <span class=ui>.STL</span>, <span class=ui>GLTF</span> e <span class=ui>.SVG</span>.",
    sos=[("Abriu a janela errada","Feche com o × e clique no botão do <b>meio</b>, <span class=ui>Exportar</span>."),
         ("Cliquei no .STL e baixou um arquivo","Sem problema: ele fica na pasta de downloads do computador. Apague o arquivo se o professor pedir.")]),
 ],
}
for i, p in enumerate(AULA["passos"], 1):
    p["n"] = i
