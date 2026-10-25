# -*- coding: utf-8 -*-
"""Aula 10 — Régua e escala: dez cubos de 10 mm viram uma barra de 10 cm.

Medido na bancada (fonte/cap10.py). Pegadinhas:
  · a RÉGUA fica SALVA no projeto: clicar no ícone de novo a REMOVE (e liga o
    modo de colocar; Esc sai dele);
  · a régua só mostra as distâncias quando UMA PEÇA está selecionada;
  · a Caixa nova nasce com o tamanho da última que se mexeu — por isso o passo
    do cubo de 10 manda conferir os três campos;
  · Ctrl + D se repete (Aula 8): copiar e empurrar 10 mm uma vez, e mais oito
    Ctrl + D fazem a fileira inteira.
"""
import ast
INTRO = ast.literal_eval(open(__file__.replace("conteudo_a10.py", "_intro10.txt")).read())

AULA = {
 "n": 10,
 "slug": "aula10",
 "titulo": "Régua e escala",
 "subtitulo": "Dez cubinhos de 1 cm viram uma barra de 10 cm — e a Régua do Tinkercad confirma o número.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 10 · medir e escalar",
 "fim": "Acabou a Aula 10. Você fez uma <b>barra de 10 cm</b> com dez cubos de 1 cm — repetindo com o <b>Ctrl + D</b> — e usou a <b>Régua</b> para <b>conferir</b> o número: 100 mm. Viu que, ao mover a peça, os números da régua <b>mudam junto</b>, e fez um cubo com o <b>dobro</b> do lado (20 mm). A peça está salva na sua conta com o nome que você deu. <i>Desafio:</i> um cubo com o dobro do lado cabe <b>oito</b> cubinhos dentro — confira com a régua.",
 "avisos": [
   ("Projeto novo", "Esta aula começa num projeto novo, vazio. As peças das aulas anteriores continuam guardadas na sua conta."),
   ("Milímetros e centímetros", "<b>10 mm</b> são <b>1 cm</b>, e <b>100 mm</b> são <b>10 cm</b>: o comprimento de uma régua escolar pequena."),
   ("A Régua", "A <span class=ui>Régua</span> é o botão do meio, no canto de cima da coluna da direita. Ela <b>fica salva</b> no projeto: para tirar, é só clicar nela de novo."),
   ("Os clipes", "Os passos com animação mostram o gesto inteiro: o mouse andando, o <b>botão certo acendendo</b> e as <b>teclas acesas</b> quando o gesto é de teclado."),
   ("Travou?", "Todo passo tem um quadro laranja embaixo com o conserto dos erros mais comuns."),
 ],
 "passos": INTRO + [

  dict(n=4, titulo="Conheça a tela", img="aula10/p01_vazio.jpg", clipe=None,
    corpo="O editor abriu com o plano azul quadriculado <b>vazio</b>. Hoje vão aparecer três lugares novos:<br><br><b>1.</b> A <b>coluna da direita</b> tem, no alto, três ícones. O <b>do meio</b> (um L com marquinhas) é a <span class=ui>Régua</span>.<br><b>2.</b> Embaixo, no canto do plano, o <span class=ui>Ajustar Grade</span> diz <b>1,0 mm</b>: é o tanto que a peça anda em cada empurrão fino.<br><b>3.</b> A <b>barra da esquerda</b> tem a casinha, o <b>+</b> e o <b>−</b>.",
    ck="Você acha o ícone da Régua no alto da coluna da direita, e o <span class=ui>Ajustar Grade</span> mostra 1,0 mm.",
    sos=[("Não acho a Régua","Fica no alto da coluna da direita, o ícone do <b>meio</b> entre os três."),
         ("O plano está torto","Clique na casinha da barra da esquerda.")]),

  dict(n=5, titulo="Arraste uma Caixa para a esquerda do plano", img="aula10/g02_depois.jpg", clipe="caixa.gif",
    corpo="Na coluna da direita, a forma <b>vermelha</b> do meio da segunda fileira, à esquerda, é a <span class=ui>Caixa</span>. Segure o botão esquerdo nela, <b>arraste até a esquerda do plano</b> e solte: a barra vai crescer para a direita.",
    ck="Tem um cubo vermelho no lado esquerdo do plano e o painel diz <span class=ui>Caixa</span>.",
    sos=[("Peguei a caixa cinza listrada","Essa é o <b>buraco</b>. Aperte <span class=ui>Delete</span> e arraste a vermelha.")]),

  dict(n=6, titulo="Cubo de 10 × 10 × 10", img="aula10/g03_depois.jpg", clipe="medidas.gif",
    corpo="No painel, escreva <b>10</b> em <span class=ui>Comprimento</span>, <b>10</b> em <span class=ui>Largura</span> e <b>10</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada).<br><br>Um cubinho de <b>1 cm</b> de lado.",
    ck="Os três campos mostram <b>10</b> e o cubo é pequeno, no lado esquerdo.",
    sos=[("Digitei e nada mudou","Falta o <span class=ui>Enter</span> depois de cada número."),
         ("O cubo é grande","Falta mudar um campo. Confira os três: 10, 10 e 10.")]),

  dict(n=7, titulo="Ctrl + D e Shift + →: uma cópia 10 mm adiante", img="aula10/g04_depois.jpg", clipe="copia.gif",
    corpo="Aperte <span class=ui>Ctrl</span> + <span class=ui>D</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>D</span>): nasce uma <b>cópia</b> em cima do cubo. Agora segure <span class=ui>Shift</span> e aperte <span class=ui>→</span> <b>uma vez</b>: a cópia anda <b>10 mm</b> para a direita, <b>encostando</b> no cubo.",
    ck="Há dois cubinhos lado a lado, encostados.",
    sos=[("A cópia não andou","Segure o <span class=ui>Shift</span> ao apertar a seta: sem ele a cópia anda só 1 mm."),
         ("Andou demais","Cada Shift + seta é 10 mm. Aperte Shift + ← para voltar um.")]),

  dict(n=8, titulo="Ctrl + D oito vezes: a fileira se faz sozinha", img="aula10/g05_depois.jpg", clipe="repete.gif",
    corpo="Aperte <span class=ui>Ctrl</span> + <span class=ui>D</span> <b>oito vezes</b>, uma de cada vez e <b>sem mexer em seta nenhuma</b>. Como na Aula 8, o Tinkercad <b>repete o último empurrão</b>: cada cópia nasce 10 mm adiante da anterior.<br><br>Conte: 2 cubos + 8 = <b>10 cubos</b>.",
    ck="Uma fileira de <b>dez</b> cubinhos, de ponta a ponta, atravessa a metade esquerda do plano.",
    sos=[("Sobraram cubos empilhados","Algum Ctrl + D foi sem a cópia anterior ter andado. Aperte Ctrl + Z até ficar a fileira certa."),
         ("Contei nove ou onze","Aperte Ctrl + Z uma vez (se sobrou um) ou Ctrl + D uma vez (se faltou).")]),

  dict(n=9, titulo="Selecione tudo: Ctrl + A", img="aula10/g06_depois.jpg", clipe="seleciona.gif",
    corpo="Clique num <b>lugar vazio</b> do plano e aperte <span class=ui>Ctrl</span> + <span class=ui>A</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>A</span>). Os dez cubos ficam selecionados: <span class=ui>Shapes(10)</span>.",
    ck="A fileira inteira tem contorno azul, e o painel diz <span class=ui>Shapes(10)</span>.",
    sos=[("O painel diz outro número","Conte os cubos. Se tiver 9 ou 11, volte ao passo 8.")]),

  dict(n=10, titulo="Agrupe: Grupo de união", img="aula10/g07_depois.jpg", clipe="uniao.gif",
    corpo="Na barra de cima há três botõezinhos de juntar peças, à direita do meio. Clique no <b>do meio</b>, o <span class=ui>Grupo de união</span>.<br><br>Os dez cubos viram <b>uma barra só</b>, lisinha: o painel diz <span class=ui>Union</span>.",
    ck="A fileira virou uma <b>barra lisa</b>, sem as divisões entre os cubos, e o painel diz <span class=ui>Union</span>.",
    sos=[("O painel não mudou","Clique no botão do meio dos três, o <span class=ui>Grupo de união</span>.")]),

  dict(n=11, titulo="Escolha a Régua", img="aula10/g08_depois.jpg", clipe="regua.gif",
    corpo="Clique num lugar vazio do plano. No alto da coluna da direita, clique no ícone do <b>meio</b>, a <span class=ui>Régua</span>.<br><br>O ícone fica <b>marcado</b> e o ponteiro passa a esperar: você vai dizer onde a régua começa.",
    ck="O ícone da Régua ficou marcado (com contorno azul).",
    sos=[("Não aconteceu nada","Clique no ícone do <b>meio</b>, não no do plano nem no do balãozinho."),
         ("Já tinha uma régua","Clicar de novo a <b>tira</b>. Clique uma vez mais para ela voltar a esperar.")]),

  dict(n=12, titulo="Clique no plano: a origem da régua", img="aula10/g09_depois.jpg", clipe="origem.gif",
    corpo="Clique <b>no plano de trabalho</b>, na ponta de baixo da barra, à esquerda. Aparece uma <b>régua desenhada no plano</b>: um traço para o lado e outro para o fundo, com marquinhas, e um <b>aro</b> onde você clicou. Esse aro é o <b>zero</b>, a origem.",
    ck="No plano aparecem duas retas com marquinhas e um aro no ponto clicado.",
    sos=[("Nada apareceu","Primeiro clique no ícone da Régua (passo 11). Depois, clique no plano, e não em cima da barra."),
         ("O aro ficou longe","Sem problema: a régua mede a distância dele até a peça.")]),

  dict(n=13, titulo="Clique na barra: ela mostra 100", img="aula10/g10_depois.jpg", clipe="mede.gif",
    corpo="Clique <b>em cima da barra</b>. Surgem <b>números</b> em volta dela. O de <b>baixo</b> diz <b>100.00</b>: é o comprimento da barra em milímetros — dez cubos de 10 mm. Os outros dizem <b>10.00</b> (a altura e a espessura) e outros, quanto falta da origem até a barra.",
    ck="Em baixo da barra aparece <b>100.00</b>. A conta bate: 10 × 10 = 100 mm = 10 cm.",
    sos=[("Não vejo números","A barra não está selecionada. Clique bem em cima dela."),
         ("O número é outro","Conte os cubos de novo: dez cubos de 10 mm dão 100.")]),

  dict(n=14, titulo="Empurre a barra: Shift + ↑ duas vezes", img="aula10/g10b_depois.jpg", clipe="empurra.gif",
    corpo="Com a barra selecionada, segure <span class=ui>Shift</span> e aperte <span class=ui>↑</span> <b>duas vezes</b>: a barra anda <b>20 mm</b> para o fundo.<br><br>Olhe os números: o <b>100.00</b> continua igual (a barra não mudou de tamanho) mas um dos outros <b>mudou</b>: a distância dela até a origem cresceu 20.",
    ck="O 100.00 continua, e a distância até a origem subiu 20 mm.",
    sos=[("A barra foi para o outro lado","Seta para <b>cima</b> é para o fundo do plano. Aperte Shift + ↓ duas vezes para voltar."),
         ("Os números sumiram","A barra perdeu a seleção. Clique nela de novo.")]),

  dict(n=15, titulo="Olhe de cima", img="aula10/g10c_depois.jpg", clipe="vista_cima.gif",
    corpo="Clique num lugar vazio do plano. No <b>cubo</b> de vistas, no canto de cima à esquerda, clique na face escrita <span class=ui>SUPERIOR</span>.<br><br>De cima, a barra é um <b>retângulo</b> comprido e a régua é uma <b>cruz</b>: um traço para o lado e outro para o fundo. Depois, clique na casinha para voltar.",
    ck="De cima se vê o retângulo da barra e as duas retas da régua formando um L.",
    sos=[("A câmera não mudou","Clique <b>na palavra</b> SUPERIOR do cubinho.")]),

  dict(n=16, titulo="Tire a régua: clique nela de novo", img="aula10/g10d_depois.jpg", clipe="tira_regua.gif",
    corpo="No ícone da <span class=ui>Régua</span>, clique <b>mais uma vez</b>. As retas <b>somem</b> do plano: a régua é <b>tirada</b> do projeto. Aperte <span class=ui>Esc</span> para o ícone sair do modo de colocar.",
    ck="As duas retas com marquinhas sumiram do plano, e a barra continua lá.",
    sos=[("A régua não sumiu","Clique de novo no ícone. Se o ícone ficou marcado, aperte Esc."),
         ("Sumiu a barra","Aperte Ctrl + Z uma vez: ela volta.")]),

  dict(n=17, titulo="Arraste outra Caixa: a escala", img="aula10/g11_depois.jpg", clipe="caixa2.gif",
    corpo="Arraste <b>outra Caixa vermelha</b> da coluna da direita e solte <b>no plano, ao lado da barra</b>. Confira os três campos do painel: a Caixa nasce com o <b>tamanho da última</b> que você mexeu, e hoje queremos <b>10, 10 e 10</b>.<br><br>É o cubinho de 1 cm de novo.",
    ck="Um cubinho vermelho está no plano, ao lado da barra, e os três campos mostram <b>10</b>.",
    sos=[("O cubo nasceu com outro tamanho","Corrija os três campos para 10, com <span class=ui>Enter</span> depois de cada."),
         ("Soltei em cima da barra","Arraste o cubo para um espaço vazio, ao lado.")]),

  dict(n=18, titulo="Escala: 20 × 20 × 20, o dobro", img="aula10/g12_depois.jpg", clipe="dobro.gif",
    corpo="Escreva <b>20</b> em <span class=ui>Comprimento</span>, <b>20</b> em <span class=ui>Largura</span> e <b>20</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada).<br><br>Isso é <b>escala 2:1</b>: o cubo tem o <b>dobro</b> do lado, e por isso é <b>8 vezes</b> maior em volume (2 × 2 × 2). Esse é o segredo de ampliar uma peça: <b>multiplique os três números</b> pelo mesmo valor.",
    ck="O cubo ficou <b>duas vezes</b> mais largo, mais fundo e mais alto, e os campos mostram <b>20</b>.",
    sos=[("O cubo ficou torto","Os três campos têm de ter o mesmo número. Confira: 20, 20 e 20."),
         ("Quero uma escala diferente","Multiplique os três pelo mesmo valor: para o triplo, 30.")]),

  dict(n=19, titulo="Dê um nome ao seu projeto", img="aula10/g13_depois.jpg", clipe="batiza.gif",
    corpo="Clique num lugar vazio e na <b>casinha</b> da barra da esquerda. Depois clique no <b>nome do projeto</b>, no canto de cima à esquerda, apague, escreva <b>Régua da ANA</b> (ou o seu nome) e aperte <span class=ui>Enter</span>.<br><br>O Tinkercad salva sozinho. A barra e o cubo estão guardados na sua conta.",
    ck="No canto de cima à esquerda aparece o <b>nome que você escreveu</b>.",
    sos=[("O nome não mudou","Falta o <span class=ui>Enter</span>."),
         ("O campo não abriu","Clique <b>em cima das letras</b> do nome.")]),
 ],
}
for i, p in enumerate(AULA["passos"], 1):
    p["n"] = i
