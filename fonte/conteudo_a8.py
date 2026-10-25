# -*- coding: utf-8 -*-
"""Aula 8 — Dado: furos redondos por Orifício, Ctrl + D que se REPETE e esfera solta na face.

Medido na bancada (fonte/cap8.py). Pegadinhas:
  · a Esfera solta na tampa já nasce no CENTRO (alinhar não muda um pixel);
  · o centro da esfera precisa ficar na SUPERFÍCIE: Ctrl + ↓ dez vezes, senão o
    furo é uma bolha que não toca a tampa;
  · Ctrl + D REPETE o último empurrão: a segunda cópia anda sozinha o mesmo que
    a primeira — é assim que se faz uma fila de furos;
  · na face da frente a esfera também afunda com Ctrl + ↓: o ↓ vale na direção
    da face (para dentro do dado).
"""

AULA = {
 "n": 8,
 "slug": "aula8",
 "titulo": "Dado",
 "subtitulo": "Um cubo com furos redondos: três na tampa, em diagonal, e um na frente — e uma descoberta: o Ctrl + D se repete sozinho.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 8 · furos redondos e repetir",
 "fim": "Acabou a Aula 8. Você fez um <b>dado</b> de 60 mm com <b>três furos</b> na tampa e <b>um</b> na frente. Aprendeu duas coisas: o <b>centro</b> da esfera tem de ficar <b>na superfície</b> (por isso o Ctrl + ↓ dez vezes) e o <b>Ctrl + D se repete</b>: depois de copiar e empurrar uma vez, o segundo Ctrl + D já empurra a cópia do mesmo jeito. A peça está salva na sua conta com o nome que você deu. <i>Desafio:</i> complete as faces de um dado de verdade — o 4 é o oposto do 3; o 6, do 1.",
 "avisos": [
   ("Projeto novo", "Esta aula começa num projeto novo, vazio. As peças das aulas anteriores continuam guardadas na sua conta."),
   ("Milímetros", "O dado tem <b>60 mm</b> de lado: o tamanho de uma bola de tênis."),
   ("Tampa e frente", "Hoje só <b>duas faces</b> ganham furos: a de cima e a da frente. As outras ficam lisas."),
   ("Os clipes", "Os passos com animação mostram o gesto inteiro: o mouse andando, o <b>botão certo acendendo</b> e as <b>teclas acesas</b> quando o gesto é de teclado."),
   ("Travou?", "Todo passo tem um quadro laranja embaixo com o conserto dos erros mais comuns."),
 ],
 "passos": [

  dict(n=1, titulo="Abra o Tinkercad e crie um Projeto 3D", img="aula8/p01_vazio.jpg", clipe="criar.gif",
    corpo="Entre no Tinkercad com a sua conta. No canto de cima à direita, clique em <span class=ui>+ Criar</span> e, na primeira linha, em <span class=ui>Projeto 3D</span>.<br><br>Abre o editor com o plano azul quadriculado <b>vazio</b> e um nome sorteado — deixe assim, no último passo você troca.",
    ck="O editor abriu com o plano azul claro quadriculado vazio.",
    sos=[("Não sei entrar","Chame o professor. Não crie conta nova: os seus projetos estão na antiga."),
         ("Abriu outra coisa","Volte com a seta ⟵ do navegador e clique de novo em <span class=ui>+ Criar</span>, escolhendo a primeira linha."),
         ("A tela ficou branca","O Tinkercad é pesado. Espere até meio minuto. Se continuar branca, recarregue com <span class=ui>F5</span>.")]),

  dict(n=2, titulo="Arraste uma Caixa para o plano", img="aula8/g02_depois.jpg", clipe="caixa.gif",
    corpo="Na coluna da direita, a forma <b>vermelha</b> do meio da segunda fileira, à esquerda, é a <span class=ui>Caixa</span>. Segure o botão esquerdo nela, <b>arraste até o meio do plano</b> e solte.",
    ck="Tem um cubo vermelho no meio do plano e o painel branco escrito <span class=ui>Caixa</span> no alto.",
    sos=[("Peguei a caixa cinza listrada","Essa é o <b>buraco</b>. Aperte <span class=ui>Delete</span> e arraste a vermelha.")]),

  dict(n=3, titulo="Dado 60 × 60 × 60", img="aula8/g03_depois.jpg", clipe="medidas.gif",
    corpo="No painel, escreva <b>60</b> em <span class=ui>Comprimento</span>, <b>60</b> em <span class=ui>Largura</span> e <b>60</b> em <span class=ui>Altura</span> (<span class=ui>Enter</span> depois de cada).<br><br>Um <b>cubo</b> perfeito: os três lados iguais.",
    ck="Os três campos mostram <b>60</b>, e o cubo está grande, ocupando boa parte do plano.",
    sos=[("Digitei e nada mudou","Falta o <span class=ui>Enter</span> depois de cada número."),
         ("Ficou um tijolo","Um dos números ficou diferente de 60. Confira os três campos.")]),

  dict(n=4, titulo="Solte uma Esfera no meio da tampa", img="aula8/g04_depois.jpg", clipe="esfera.gif",
    corpo="Clique num lugar vazio do plano. Na coluna da direita, a <b>bola azul</b> do canto direito da segunda fileira é a <span class=ui>Esfera</span>. Segure o botão esquerdo nela e <b>solte no meio da tampa</b> do dado.<br><br>A esfera nasce <b>em cima</b> da tampa (aparece o <b>quadrado verde</b>, o plano de trabalho que foi para o alto) e <b>já no meio</b>.",
    ck="Uma esfera azul está pousada no meio da tampa do dado, com o quadrado verde em volta.",
    sos=[("A esfera caiu no chão","Você soltou fora do dado. Arraste de novo, soltando em cima da <b>tampa</b>."),
         ("Peguei a esfera cinza listrada","Essa já é o buraco. Pule o próximo passo, mas continue com o seguinte.")]),

  dict(n=5, titulo="Transforme a esfera em Orifício", img="aula8/g05_depois.jpg", clipe="orificio.gif",
    corpo="Com a esfera selecionada, no painel clique em <span class=ui>Orifício</span> (a bolinha cinza listrada, ao lado de <span class=ui>Sólido</span>).<br><br>A esfera fica <b>cinza e transparente</b>: agora é um <b>buraco</b>.",
    ck="A esfera ficou cinza e listrada, e no painel o <span class=ui>Orifício</span> está marcado.",
    sos=[("Nada mudou de cor","Confira que a esfera está selecionada (com as alças) e clique na bolinha do <span class=ui>Orifício</span>."),
         ("O dado é que ficou listrado","Você estava com o dado selecionado. Clique em <span class=ui>Sólido</span> para desfazer e selecione a esfera.")]),

  dict(n=6, titulo="Afunde a esfera: Ctrl + ↓, dez vezes", img="aula8/g06_depois.jpg", clipe="afunda.gif",
    corpo="A esfera está <b>pousada</b> em cima da tampa, só encostando: se agrupasse assim, não cavaria nada. O <b>centro</b> dela precisa ficar <b>na superfície</b>, de modo que metade entre no dado.<br><br>Com a esfera selecionada, segure <span class=ui>Ctrl</span> e aperte a <b>seta para baixo</b> <span class=ui>↓</span> <b>dez vezes</b>. Cada toque desce 1 mm: a esfera tem 20 mm de largura, então 10 mm é a <b>metade</b>.",
    ck="A esfera cinza afundou: <b>metade</b> dela está dentro do dado, e o quadrado verde continua em cima.",
    sos=[("A esfera andou de lado","Você soltou o <span class=ui>Ctrl</span>. A seta sozinha anda no plano; <b>com Ctrl</b> é que sobe e desce."),
         ("Desceu demais e sumiu","Aperte <span class=ui>Ctrl</span> e a seta para cima ↑ algumas vezes até aparecer o topo dela."),
         ("Não desce nada","Clique uma vez na esfera para selecioná-la. Atalho de teclado só vale para a peça marcada.")]),

  dict(n=7, titulo="Leve a esfera para o canto: Shift + ← e Shift + ↓", img="aula8/g07_depois.jpg", clipe="canto.gif",
    corpo="Agora vamos fazer uma <b>fileira diagonal</b> de três furos: um no canto, um no meio, um no outro canto. Com a esfera ainda selecionada: segure <span class=ui>Shift</span> e aperte <span class=ui>←</span> <b>uma vez</b> (10 mm) e, <b>sem Shift</b>, <span class=ui>←</span> <b>seis vezes</b> (6 mm): são 16 mm para a esquerda. Faça o mesmo com <span class=ui>↓</span>: <span class=ui>Shift</span> + <span class=ui>↓</span> uma vez e <span class=ui>↓</span> seis vezes: 16 mm para a frente.<br><br>A esfera vai para o <b>canto da frente, à esquerda</b> da tampa.",
    ck="O furo está no <b>canto da frente, à esquerda</b> da tampa, a uns 14 mm da borda.",
    sos=[("Foi para o lado errado","Cada Shift + seta é 10 mm e cada seta sozinha é 1 mm. Volte com a seta contrária."),
         ("A câmera mexeu","A esfera não estava selecionada. Clique nela e refaça.")]),

  dict(n=8, titulo="Ctrl + D e empurre a cópia para o meio", img="aula8/g08_depois.jpg", clipe="copia.gif",
    corpo="Aperte <span class=ui>Ctrl</span> + <span class=ui>D</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>D</span>): nasce uma <b>cópia</b> em cima do furo.<br><br>Empurre a cópia para o <b>meio</b> da tampa: <span class=ui>Shift</span> + <span class=ui>→</span> uma vez e <span class=ui>→</span> seis vezes (16 mm para a direita); <span class=ui>Shift</span> + <span class=ui>↑</span> uma vez e <span class=ui>↑</span> seis vezes (16 mm para trás).",
    ck="Há <b>dois furos</b> na tampa: um no canto da frente e outro no meio dela.",
    sos=[("A cópia não nasceu","O atalho só vale com a esfera selecionada. Clique nela e aperte Ctrl + D de novo."),
         ("Os dois ficaram juntos","Faltou empurrar a cópia. Use as setas de novo.")]),

  dict(n=9, titulo="Ctrl + D de novo: a cópia se repete sozinha", img="aula8/g09_depois.jpg", clipe="repete.gif",
    corpo="Aperte <span class=ui>Ctrl</span> + <span class=ui>D</span> <b>mais uma vez</b>, sem mexer em seta nenhuma.<br><br>Olhe: nasce a <b>terceira</b> esfera <b>já no outro canto</b>. O Tinkercad <b>lembra</b> o último empurrão e o <b>repete</b> na nova cópia. Dois toques de Ctrl + D, e uma fila de três.",
    ck="Há <b>três furos</b> em diagonal na tampa: um em cada canto da diagonal e um no meio.",
    sos=[("A terceira esfera não foi para o canto","O Ctrl + D só repete se você <b>acabou de empurrar</b> a cópia anterior. Empurre a nova cópia a mão: 16 mm para a direita e 16 para trás."),
         ("Nasceu uma esfera a mais","Aperte Ctrl + Z uma vez e confira que são só três.")]),

  dict(n=10, titulo="Solte outra Esfera na face da frente", img="aula8/g10_depois.jpg", clipe="esfera2.gif",
    corpo="Clique num lugar vazio do plano. Arraste <b>outra Esfera</b> da coluna da direita e solte <b>no meio da frente do dado</b> — na parede da frente, e não na tampa.<br><br>O <b>quadrado verde</b> fica de pé, colado na parede, e a esfera <b>nasce ali</b>, saindo da parede como o olho do robô da Aula 7.",
    ck="Uma esfera azul está colada no meio da parede da frente, e o quadrado verde está de pé.",
    sos=[("A esfera foi para a tampa","Você soltou na parte de cima. Solte mais para baixo, na frente."),
         ("A esfera caiu no chão","Você soltou fora do dado. Arraste de novo, soltando em cima da <b>parede da frente</b>.")]),

  dict(n=11, titulo="Transforme em Orifício", img="aula8/g11_depois.jpg", clipe="orificio2.gif",
    corpo="Com a esfera selecionada, no painel clique em <span class=ui>Orifício</span>. A esfera da frente também vira buraco.",
    ck="A esfera da frente ficou cinza e listrada.",
    sos=[("Virou buraco a esfera errada","Clique em <span class=ui>Sólido</span> para desfazer e selecione a da frente.")]),

  dict(n=12, titulo="Afunde: Ctrl + ↓, dez vezes", img="aula8/g12_depois.jpg", clipe="afunda2.gif",
    corpo="Segure <span class=ui>Ctrl</span> e aperte <span class=ui>↓</span> <b>dez vezes</b>. Na face da frente a seta para baixo também <b>afunda</b>: ela empurra a esfera <b>para dentro</b> do dado, na direção da parede. É a mesma regra da tampa: o <b>centro</b> na superfície.",
    ck="A esfera da frente afundou: metade dela está dentro da parede.",
    sos=[("A esfera subiu em vez de afundar","Aperte Ctrl e a seta para cima ↑ dez vezes e refaça com ↓."),
         ("A esfera andou na parede","Faltou o <span class=ui>Ctrl</span>.")]),

  dict(n=13, titulo="Selecione tudo: Ctrl + A", img="aula8/g16_depois.jpg", clipe="seleciona.gif",
    corpo="Clique num <b>lugar vazio</b> do plano e aperte <span class=ui>Ctrl</span> + <span class=ui>A</span> (Mac: <span class=ui>Cmd</span> + <span class=ui>A</span>). O dado e as quatro esferas ficam selecionados: <span class=ui>Shapes(5)</span>.",
    ck="O dado e as esferas têm contorno azul, e o painel diz <span class=ui>Shapes(5)</span>.",
    sos=[("O painel diz outro número","Conte: o dado e quatro esferas são cinco peças. Se faltar uma, clique num lugar vazio e refaça.")]),

  dict(n=14, titulo="Agrupe: Grupo de união", img="aula8/g17_depois.jpg", clipe="uniao.gif",
    corpo="Na barra de cima há três botõezinhos de juntar peças, à direita do meio. Clique no <b>do meio</b>, o <span class=ui>Grupo de união</span>.<br><br>As esferas-buraco <b>cavam</b> o dado e tudo vira <b>uma peça só</b>: o painel diz <span class=ui>Union</span>. Os furos aparecem nas paredes.",
    ck="O dado virou uma peça só, com <b>três furos na tampa</b> e <b>um na frente</b>, e o painel diz <span class=ui>Union</span>.",
    sos=[("Os furos não apareceram","As esferas não afundaram. Aperte Ctrl + Z, volte aos passos 6 e 12 e afunde dez vezes."),
         ("Sumiu uma esfera","Ela não estava selecionada. Desagrupe com Ctrl + Shift + G, selecione tudo de novo e agrupe.")]),

  dict(n=15, titulo="Olhe de cima: três furos em diagonal", img="aula8/g18_depois.jpg", clipe="vista_cima.gif",
    corpo="Clique num <b>lugar vazio</b> do plano. No <b>cubo</b> de vistas, no canto de cima à esquerda, clique na face escrita <span class=ui>SUPERIOR</span>.<br><br>De cima se vê a tampa com os <b>três furos em diagonal</b>, igualmente espaçados: o do meio e um em cada ponta.",
    ck="De cima se veem três furos redondos, em diagonal, igualmente espaçados.",
    sos=[("A câmera não mudou","Clique <b>na palavra</b> SUPERIOR do cubinho."),
         ("Só vejo dois furos","A terceira esfera não saiu no passo 9. Desagrupe, refaça o passo 9 e agrupe de novo.")]),

  dict(n=16, titulo="Volte à vista inicial: o furo do um", img="aula8/g18b_depois.jpg", clipe="vista_inicial.gif",
    corpo="Clique na <b>casinha</b> da barra da esquerda. A câmera volta à vista inicial.<br><br>Agora se veem as <b>duas faces</b>: três furos em cima e <b>um furo no meio da frente</b>, que é o do <b>um</b>.",
    ck="Na vista inicial: três furos em diagonal na tampa e um furo no meio da face da frente.",
    sos=[("Não vejo o furo da frente","Ele não afundou (passo 12). Desagrupe, afunde dez vezes e agrupe de novo.")]),

  dict(n=17, titulo="Gire a câmera com o botão direito", img="aula8/g18d_depois.jpg", clipe="girar.gif",
    corpo="Segure o botão <b>direito</b> do mouse em cima do <b>plano de trabalho</b> e arraste um pouco para a direita e para cima.<br><br>A câmera <b>gira</b> em volta do dado: dá para ver os furos por outro lado e conferir que são <b>buracos de verdade</b>, com fundo redondo.",
    ck="A câmera mudou e o dado aparece de outro lado, com os furos redondos nas paredes.",
    sos=[("A peça saiu do lugar","Você usou o botão <b>esquerdo</b>. Aperte Ctrl + Z e repita com o <b>direito</b>.")]),

  dict(n=18, titulo="Aproxime: o botão +", img="aula8/g18c_depois.jpg", clipe="zoom.gif",
    corpo="Na barra da esquerda, clique no <span class=ui>+</span> <b>duas vezes</b>. A câmera <b>chega perto</b> do dado.<br><br>O <span class=ui>−</span>, logo abaixo, afasta. E a <b>casinha</b> devolve a câmera à vista inicial.",
    ck="O dado ficou maior na tela: a câmera se aproximou.",
    sos=[("Não aproximou","Clique no <span class=ui>+</span>, o primeiro botão debaixo do ícone de centralizar."),
         ("Aproximou demais","Use o <span class=ui>−</span> ou a casinha.")]),

  dict(n=19, titulo="Dê um nome ao seu projeto", img="aula8/g19_depois.jpg", clipe="batiza.gif",
    corpo="Clique na <b>casinha</b> da barra da esquerda para voltar à vista inicial. Depois clique no <b>nome do projeto</b>, no canto de cima à esquerda, apague, escreva <b>Dado da ANA</b> (ou o seu nome) e aperte <span class=ui>Enter</span>.<br><br>O Tinkercad salva sozinho. O dado está guardado na sua conta.",
    ck="No canto de cima à esquerda aparece o <b>nome que você escreveu</b>.",
    sos=[("O nome não mudou","Falta o <span class=ui>Enter</span>."),
         ("O campo não abriu","Clique <b>em cima das letras</b> do nome.")]),
 ],
}
