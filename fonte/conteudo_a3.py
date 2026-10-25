# -*- coding: utf-8 -*-
"""Aula 3 — Caneca com alça: o porta-lápis ganha uma alça (um anel em pé).

Tudo o que esta aula afirma sobre a tela foi MEDIDO na bancada (fonte/cap3.py).
Cinco coisas desta aula ninguém acerta de cabeça:

  · copiar e colar vale ENTRE projetos (Ctrl + C num, Ctrl + V no outro);
  · o anel precisa de DOIS giros: a seta de cima o põe em pé, a de baixo o vira
    de frente — e o transferidor mostra o ângulo ao vivo (passos 7 e 8);
  · o Alinhar move TODAS as formas: é preciso FIXAR a caneca clicando nela
    antes, ou é ela que anda até o anel (passo 11);
  · depois de alinhar, o anel está DENTRO da caneca: para empurrá-lo sozinho é
    preciso tirar a caneca da seleção com Shift + clique (passo 15);
  · Shift + seta anda 10 mm; a seta sozinha anda 1 mm (passo 16).
"""

AULA = {
 "n": 3,
 "slug": "aula3",
 "titulo": "Caneca com alça",
 "subtitulo": "O seu porta-lápis ganha uma alça — um anel que você vira em pé, centra com o Alinhar e empurra até colar na lateral.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 3 · girar e posicionar",
 "fim": "Acabou a Aula 3. O seu porta-lápis virou uma <b>caneca com alça</b>. Você aprendeu a <b>copiar uma peça para outro projeto</b>, a <b>girar</b> uma forma pelas setas curvas (com o transferidor mostrando o ângulo), a <b>fixar</b> uma peça no Alinhar para só a outra andar e a <b>empurrar</b> com o teclado: <b>Shift + seta</b> anda 10 mm, e a seta sozinha anda 1 mm. A peça está salva na sua conta com o nome que você deu — o porta-lápis da Aula 2 continua lá, intacto.",
 "avisos": [
   ("Parte do porta-lápis", "Hoje você começa do <b>porta-lápis da Aula 2</b>. Se o seu projeto não existe mais, refaça a Aula 2 antes (leva uns 25 minutos)."),
   ("O original fica guardado", "Você vai <b>copiar</b> o porta-lápis para um projeto novo. O da Aula 2 não muda: dá para brincar à vontade."),
   ("Milímetros", "Todo número é em milímetro. A alça terá cerca de <b>36 mm</b> de ponta a ponta — o tamanho de um dedão grande."),
   ("Os clipes", "Os passos com animação mostram o gesto inteiro: o mouse andando, o <b>botão certo acendendo</b> e as <b>teclas acesas</b> quando o gesto é de teclado."),
   ("Travou?", "Todo passo tem um quadro laranja embaixo com o conserto dos erros mais comuns."),
 ],
 "passos": [

  dict(n=1, titulo="Abra o seu porta-lápis", img="aula3/p01_porta_lapis.jpg", clipe=None,
    corpo="No Tinkercad, na lista dos seus projetos, clique no cartão do <b>porta-lápis</b> que você fez na Aula 2 (o que você batizou). Ele abre no editor.<br><br>A peça está lá: o copo laranja, alto, com o fundo e o vazio por dentro.",
    ck="O editor mostra o copo laranja do porta-lápis, com o nome do projeto no canto de cima à esquerda.",
    sos=[("Não acho o cartão","Procure pelo nome que você deu na Aula 2. Se der muito trabalho, chame o professor: todos os cartões novos têm um nome sorteado esquisito."),
         ("Abriu um projeto vazio","Você abriu outro cartão ou criou um projeto novo. Volte à lista e escolha o do porta-lápis."),
         ("O porta-lápis não está mais lá","Refaça a Aula 2 antes de seguir: hoje o ponto de partida é ele.")]),

  dict(n=2, titulo="Selecione tudo e copie: Ctrl + A, depois Ctrl + C", img="aula3/g02_depois.jpg", clipe="seleciona.gif",
    corpo="Clique num <b>lugar vazio do plano</b> para o teclado ir para lá. Segure <span class=ui>Ctrl</span> e aperte <span class=ui>A</span>: o porta-lápis fica selecionado, com contorno azul.<br><br>Agora, segure <span class=ui>Ctrl</span> e aperte <span class=ui>C</span>: ele foi <b>copiado</b>. <b>Nada muda na tela</b> — é como copiar um texto: a cópia está guardada e espera.<br><br>Em computador Mac, use <span class=ui>Cmd</span> no lugar de <span class=ui>Ctrl</span>.",
    ck="O porta-lápis tem contorno azul. (Depois do Ctrl + C não aparece nada: está certo.)",
    sos=[("Ctrl + A não faz nada","Clique uma vez num lugar vazio do plano antes: o atalho só funciona com o editor em foco."),
         ("Selecionou e eu não sei se copiei","Aperte Ctrl + C de novo. Copiar duas vezes não faz mal.")]),

  dict(n=3, titulo="Crie um projeto novo", img="aula3/p04_novo_vazio.jpg", clipe="criar.gif",
    corpo="Volte à lista de projetos (o <b>logotipo do Tinkercad</b>, no canto de cima à esquerda, leva para lá). No canto de cima à direita, clique em <span class=ui>+ Criar</span> e, na primeira linha, em <span class=ui>Projeto 3D</span>.<br><br>Abre um projeto <b>vazio</b>, com um nome sorteado (o seu será outro, diferente do da figura). O porta-lápis original continua guardado no projeto de antes.",
    ck="O editor abriu com o plano azul quadriculado <b>vazio</b>, e com um nome sorteado no canto de cima à esquerda.",
    sos=[("Perdi a cópia ao trocar de projeto","Não perde: a cópia fica guardada enquanto você não copiar outra coisa. Se tiver dúvida, volte ao porta-lápis e aperte Ctrl + A e Ctrl + C de novo."),
         ("Abriu o projeto antigo","Você clicou num cartão em vez do botão. Use o <span class=ui>+ Criar</span> do canto de cima à direita.")]),

  dict(n=4, titulo="Cole: Ctrl + V", img="aula3/g05_depois.jpg", clipe="cola.gif",
    corpo="Clique num <b>lugar vazio do plano</b> e aperte <span class=ui>Ctrl</span> + <span class=ui>V</span> (no Mac, <span class=ui>Cmd</span> + <span class=ui>V</span>).<br><br>O porta-lápis aparece no projeto novo, <b>inteiro</b>: o copo, o fundo e o vazio.",
    ck="O copo laranja apareceu no plano do projeto novo, já selecionado.",
    sos=[("Não colou nada","A cópia se perdeu. Volte ao porta-lápis, aperte Ctrl + A e Ctrl + C, abra o projeto novo e tente de novo."),
         ("Colou duas vezes","Aperte Ctrl + Z para desfazer uma. Ficou um copo em cima do outro e só um deve ficar.")]),

  dict(n=5, titulo="Arraste um Tórulo para a esquerda do copo", img="aula3/g06_depois.jpg", clipe="torulo.gif",
    corpo="Na coluna da direita, procure o <b>anel azul</b>, com o nome <span class=ui>Tórulo</span> (fica na fileira de baixo; role a coluna se precisar).<br><br>Segure o botão esquerdo em cima dele, <b>arraste para a esquerda do copo</b> — um pedaço vazio do plano — e solte.<br><br>O anel azul está <b>deitado</b>, como uma rosquinha na mesa. Abre o painel <span class=ui>Tórulo</span>, com <span class=ui>Raio</span> e <span class=ui>Tubo</span>.",
    ck="Tem um anel azul deitado ao lado esquerdo do copo, e o painel branco escrito <span class=ui>Tórulo</span> no alto.",
    sos=[("Não acho o Tórulo","Ele é azul e fica no fim da coluna de formas. Role a coluna com o mouse."),
         ("Soltei em cima do copo","Arraste o anel de novo para o plano vazio, ao lado. Em cima do copo ele nasceria lá no alto."),
         ("As alças ficaram escondidas","Aproxime com o <b>−</b> da barra da esquerda para o plano ficar menor, ou arraste o anel para um lugar com mais espaço.")]),

  dict(n=6, titulo="Raio = 14 e Tubo = 4", img="aula3/g07_depois.jpg", clipe="raio_tubo.gif",
    corpo="No painel do Tórulo, no campo <span class=ui>Raio</span>, apague e escreva <b>14</b>, aperte <span class=ui>Enter</span>. No campo <span class=ui>Tubo</span>, escreva <b>4</b> e <span class=ui>Enter</span>.<br><br><span class=ui>Raio</span> é o tamanho do círculo grande, do meio do anel até o meio do tubo. <span class=ui>Tubo</span> é a grossura do próprio anel.",
    ck="Os campos mostram <b>14</b> e <b>4</b>, e o anel ficou um pouco maior e mais grosso.",
    sos=[("Digitei e nada mudou","Falta o <span class=ui>Enter</span> depois de cada número."),
         ("O número ficou estranho","Clique no campo, aperte Ctrl + A (no Mac, Cmd + A) e escreva de novo.")]),

  dict(n=7, titulo="Ponha o anel EM PÉ: a seta curva de cima", img="aula3/g08_depois.jpg", clipe="gira_cima.gif",
    corpo="Acima do anel há uma <b>seta curva</b> pequenininha, em cima do triângulo preto. Segure o botão esquerdo nela e <b>arraste devagar</b> para a direita e para baixo.<br><br>Aparece um <b>transferidor</b> colorido, com um número em cima. Arraste <b>até o número mostrar 90°</b> (pode vir com sinal de menos: <b>−90°</b>) e solte.<br><br>O anel levanta: ele fica <b>em pé</b>, como uma roda de bicicleta, e de frente para a lateral do plano — fininho, visto de lado.",
    ck="O anel está <b>em pé</b>: visto da câmera, é uma <b>pílula</b> fina e alta, e o transferidor mostrou 90° (ou −90°).",
    sos=[("O número não pára em 90","Arraste de pouquinho em pouquinho, olhando o número. Se passar, volte um pouco sem soltar."),
         ("Girou para o lado errado","Pode ficar −90° ou 90°: os dois servem. O que importa é o anel ficar em pé."),
         ("Não acho a seta curva","Ela fica acima do triângulo preto de <span class=ui>subir</span>. Aproxime a câmera com o <b>+</b> se estiver muito pequena.")]),

  dict(n=8, titulo="Vire o anel DE FRENTE: a seta curva de baixo", img="aula3/g09_depois.jpg", clipe="gira_baixo.gif",
    corpo="Abaixo do anel há <b>outra seta curva</b>, a de baixo. Segure o botão esquerdo nela e <b>arraste em volta do anel, num arco</b>, subindo para a direita (uma linha reta não chega nos 90°).<br><br>O transferidor aparece de novo. Arraste até o número mostrar <b>90°</b> (ou <b>−90°</b>) e solte.<br><br>O anel gira como uma porta e fica <b>de frente para você</b>: agora dá para ver o buraco do anel, como a roda de um carro visto de lado.",
    ck="O anel mostra o <b>buraco no meio</b>, de frente para você, em pé na mesa.",
    sos=[("O transferidor trava em 40 ou 50","Você está arrastando em linha reta. Faça um arco, como se desenhasse o pedaço de um círculo em volta do anel."),
         ("O anel voltou a ficar deitado","Você girou a seta de cima de novo. Aperte Ctrl + Z e use a <b>de baixo</b>."),
         ("Passei de 90","Continue arrastando até voltar ao número certo, ou aperte Ctrl + Z e recomece.")]),

  dict(n=9, titulo="Selecione tudo: Ctrl + A", img="aula3/g10_depois.jpg", clipe="seleciona2.gif",
    corpo="Clique num <b>lugar vazio</b> do plano, segure <span class=ui>Ctrl</span> e aperte <span class=ui>A</span> (no Mac, <span class=ui>Cmd</span> + <span class=ui>A</span>).<br><br>O copo e o anel ficam selecionados juntos: o painel passa a dizer <span class=ui>Shapes(2)</span>.",
    ck="O copo e o anel têm contorno azul, e o painel diz <span class=ui>Shapes(2)</span>.",
    sos=[("Selecionou só um","Clique num lugar vazio do plano e aperte Ctrl + A de novo."),
         ("O painel diz Shapes(3) ou mais","Sobrou uma peça no plano. Apague a que está sobrando (clique nela e <span class=ui>Delete</span>) e refaça.")]),

  dict(n=10, titulo="Abra o Alinhar", img="aula3/g11_depois.jpg", clipe="alinhar.gif",
    corpo="Na barra de cima, clique no botão <span class=ui>Alinhar</span> (ícone com linhas de tamanhos diferentes, ao lado do espelho).<br><br>Aparecem as <b>nove bolinhas pretas</b> em volta das duas peças, como na Aula 2: três embaixo, três do lado esquerdo e três do lado direito. E no alto, uma frase: <i>Clique nas alças para alinhar as formas</i>.",
    ck="Apareceram as bolinhas pretas em volta do copo e do anel.",
    sos=[("As bolinhas não apareceram","O Alinhar só abre com <b>duas ou mais</b> peças selecionadas. Volte ao passo 9."),
         ("Não acho o botão","Fica na barra de cima, no meio, ao lado do espelho. Passe o mouse e espere o nome aparecer.")]),

  dict(n=11, titulo="FIXE o copo: clique nele", img="aula3/g12_depois.jpg", clipe="fixa.gif",
    corpo="Este é o passo que ninguém adivinha. O Alinhar <b>move todas as peças</b> até uma linha comum: se você alinhar assim, é o <b>copo</b> que anda até o anel, e não o contrário.<br><br>A frase do alto avisa: <i>clique em uma forma selecionada para fixá-la no local</i>. Clique <b>no copo</b>: ele fica <b>parado</b>, e só o anel vai se mexer.",
    ck="O copo foi clicado e as bolinhas continuam na tela; daqui em diante só o anel vai andar.",
    sos=[("Cliquei e a seleção sumiu","Você clicou fora do copo. Aperte Ctrl + Z, abra o Alinhar de novo e clique bem <b>em cima do copo</b>."),
         ("Não sei se fixou","Siga os próximos passos: se o copo andar, volte ao passo 10 e fixe antes de clicar nas bolinhas.")]),

  dict(n=12, titulo="Centro em Y: a bolinha do meio, à esquerda", img="aula3/g13_depois.jpg", clipe="alinha_y.gif",
    corpo="Clique na <b>bolinha do meio</b> da coluna da <b>esquerda</b>.<br><br>O anel se <b>alinha</b> com o copo de <b>frente para trás</b>: o centro do anel passa a estar na mesma linha do centro do copo.",
    ck="O anel deslizou um pouco (para a frente ou para trás) e ficou na mesma linha do copo; o copo não se mexeu. A mudança é pequena: o que importa é o copo ficar parado.",
    sos=[("As bolinhas mudaram de lugar","É normal: depois de cada clique elas se reposicionam. Procure de novo a do meio da esquerda."),
         ("O copo é que andou","Você não fixou o copo. Aperte Ctrl + Z e volte ao passo 11.")]),

  dict(n=13, titulo="Centro em Z: a bolinha do meio, à direita", img="aula3/g14_depois.jpg", clipe="alinha_z.gif",
    corpo="Clique na <b>bolinha do meio</b> da coluna da <b>direita</b>.<br><br>O anel <b>sobe</b> e fica na <b>altura do meio</b> do copo — no ar, com uma sombra no plano embaixo. É a altura certa para uma alça.",
    ck="O anel está <b>no ar</b>, na altura do meio do copo, com a sombra dele no plano.",
    sos=[("Não vejo bolinha na direita","Elas ficam do lado direito, em fila inclinada. Se alguma estiver cinza, é a que você acabou de clicar."),
         ("O anel não subiu","Você clicou numa bolinha de outro lado. A do <b>meio da direita</b> é a que alinha na altura.")]),

  dict(n=14, titulo="Centro em X: a bolinha do meio, embaixo", img="aula3/g15_depois.jpg", clipe="alinha_x.gif",
    corpo="Clique na <b>bolinha do meio</b> da fileira de <b>baixo</b>.<br><br>O anel <b>desliza</b> para o meio do copo e <b>some lá dentro</b>: agora o centro dele está no mesmo ponto do centro do copo, nos três sentidos. Não se assuste: no próximo passo você o tira de lá, para o lado.",
    ck="O anel <b>sumiu para dentro do copo</b>; o contorno azul continua em volta das duas peças.",
    sos=[("O anel ficou do lado de fora","Você ainda não clicou na bolinha do meio de baixo. Clique nela."),
         ("O copo andou","Você não fixou o copo no passo 11. Aperte Ctrl + Z três vezes, fixe o copo e refaça.")]),

  dict(n=15, titulo="Esc e Shift + clique: deixe só o anel selecionado", img="aula3/g16_depois.jpg", clipe="so_o_anel.gif",
    corpo="Aperte <span class=ui>Esc</span>: o Alinhar fecha e as duas peças <b>continuam selecionadas</b>.<br><br>Segure <span class=ui>Shift</span> e <b>clique no copo</b>: o Shift <b>tira o copo da seleção</b>. O painel passa a dizer <span class=ui>Tórulo</span>: agora só o anel está selecionado, mesmo escondido dentro do copo.",
    ck="O painel do alto diz <span class=ui>Tórulo</span> (e não <span class=ui>Shapes(2)</span>): só o anel está selecionado.",
    sos=[("O painel ainda diz Shapes(2)","O clique não pegou no copo. Segure o Shift e clique bem no meio do corpo do copo."),
         ("Desmarcou tudo","Você soltou o Shift antes do clique. Aperte Ctrl + A de novo e refaça, com o Shift apertado <b>durante</b> o clique.")]),

  dict(n=16, titulo="Empurre o anel: Shift + ←, quatro vezes", img="aula3/g17_depois.jpg", clipe="empurra.gif",
    corpo="Com só o anel selecionado, segure <span class=ui>Shift</span> e aperte a <b>seta para a esquerda</b> <span class=ui>←</span> <b>quatro vezes</b>, uma de cada vez.<br><br>Cada toque com o Shift anda <b>10 mm</b> (a seta sem o Shift anda só 1). O anel sai de dentro do copo e para <b>do lado esquerdo</b>, com a ponta da direita <b>enfiada na parede</b> do copo: 4 × 10 = 40 mm.",
    ck="O anel apareceu do lado esquerdo do copo, <b>encostado nele</b>, na altura do meio.",
    sos=[("O anel foi demais ou de menos","Cada toque é 10 mm. Volte com Shift + → ou avance com Shift + ← até dar quatro no total."),
         ("A seta mexeu a câmera","O anel não estava selecionado. Volte ao passo 15."),
         ("O anel não se mexeu","Clique uma vez no plano para dar foco e refaça o passo 15.")]),

  dict(n=17, titulo="Selecione tudo de novo: Ctrl + A", img="aula3/g18_depois.jpg", clipe="seleciona3.gif",
    corpo="Clique num <b>lugar vazio</b> do plano, segure <span class=ui>Ctrl</span> e aperte <span class=ui>A</span> (no Mac, <span class=ui>Cmd</span> + <span class=ui>A</span>). O copo e o anel ficam selecionados juntos.",
    ck="O copo e o anel têm contorno azul, e o painel diz <span class=ui>Shapes(2)</span>.",
    sos=[("Só um ficou selecionado","Clique num lugar vazio do plano e aperte Ctrl + A de novo.")]),

  dict(n=18, titulo="Agrupe: Grupo de união", img="aula3/g19_depois.jpg", clipe="uniao.gif",
    corpo="Na barra de cima há três botõezinhos de juntar peças, à direita do meio. Clique no <b>do meio</b>, o <span class=ui>Grupo de união</span> (ao passar o mouse aparece o nome).<br><br>O anel e o copo viram <b>uma peça só</b>, de uma cor só: a <b>alça</b> está colada. O painel passa a dizer <span class=ui>Union</span>.",
    ck="O copo e a alça viraram <b>uma peça só</b>, toda laranja, e o painel diz <span class=ui>Union</span>.",
    sos=[("O anel ficou azul e solto","O grupo não fechou. Clique no botão do meio, o <span class=ui>Grupo de união</span>, e não no da esquerda."),
         ("Sumiu o anel","Ele ficou dentro do copo. Aperte Ctrl + Z, volte ao passo 16 e empurre o anel quatro vezes."),
         ("Não acho os botões","Ficam na barra de cima, no grupo do meio, perto do espelho e do alinhar.")]),

  dict(n=19, titulo="Olhe de frente: a alça está colada?", img="aula3/g20_depois.jpg", clipe="vista_frente.gif",
    corpo="Clique num <b>lugar vazio</b> do plano para soltar a peça. No canto de cima à esquerda, no <b>cubo</b> de vistas, clique na face escrita <span class=ui>FRONTAL</span>.<br><br>A câmera desce e você vê a caneca <b>de frente</b>: o copo e, do lado, o anel da alça <b>na altura do meio</b>, encostado no copo, sem fresta entre os dois.",
    ck="De frente se vê o copo e a alça em anel, no meio da altura, <b>encostada</b> na lateral — e não solta no ar.",
    sos=[("Dá para ver uma fresta entre o anel e o copo","O anel não chegou na parede. Desagrupe com Ctrl + Shift + G, clique só no anel (Shift + clique no copo) e empurre-o 1 mm com a seta ← sem o Shift."),
         ("A alça sumiu","Ela ficou dentro do copo. Volte ao passo 16."),
         ("A câmera não mudou","Clique <b>na palavra</b> FRONTAL do cubinho. Para voltar à vista inicial, use a casinha da barra da esquerda.")]),

  dict(n=20, titulo="Dê um nome ao seu projeto", img="aula3/g21_depois.jpg", clipe="batiza.gif",
    corpo="Clique na <b>casinha</b> da barra da esquerda para voltar à vista inicial. Depois clique no <b>nome do projeto</b>, no canto de cima à esquerda (o sorteado). Apague, escreva <b>Caneca da ANA</b> (ou o seu nome) e aperte <span class=ui>Enter</span>.<br><br>O Tinkercad salva sozinho. A caneca está guardada na sua conta, e o porta-lápis da Aula 2 também.",
    ck="No canto de cima à esquerda aparece o <b>nome que você escreveu</b>, no lugar do sorteado.",
    sos=[("O nome não mudou","Falta o <span class=ui>Enter</span>. Clique no nome de novo e faça de novo."),
         ("Clicou e o campo não abriu","Clique <b>em cima das letras</b> do nome, e não ao lado.")]),
 ],
}
