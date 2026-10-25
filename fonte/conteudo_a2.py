# -*- coding: utf-8 -*-
"""Aula 2 — Porta-lápis: esvaziar um cilindro por dentro.

Tudo o que esta aula afirma sobre a tela foi MEDIDO na bancada (fonte/cap2.py).
Quatro coisas desta aula ninguém acerta de cabeça:

  · o Cilindro NÃO tem campo de medida no painel: o tamanho se muda nos
    NÚMEROS que aparecem quando se clica numa alça (passos 5 a 8);
  · o furo nasce no chão, na mesma altura do corpo, e precisa SUBIR 5 mm para
    sobrar um fundo (passo 13);
  · depois do Alinhar é preciso apertar Esc, senão o botão de agrupar não
    responde (passo 18);
  · a conferência do fundo é olhando DE CIMA (passo 19).
"""

AULA = {
 "n": 2,
 "slug": "aula2",
 "titulo": "Porta-lápis",
 "subtitulo": "Um copo para os lápis: um cilindro alto, esvaziado por dentro, com fundo — o truque do furo da Aula 1, agora em escala maior.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 2 · esvaziar por dentro",
 "fim": "Acabou a Aula 2. Você fez um <b>copo</b>: um cilindro de 50 mm de largura e 70 de altura, esvaziado por dentro por um <b>furo</b> menor que sobe 5 mm do chão — por isso sobrou um fundo. Aprendeu três coisas novas: mudar o tamanho pelos <b>números das alças</b>, subir uma forma com <b>Ctrl + ↑</b> e <b>centrar</b> uma forma dentro da outra com o <b>Alinhar</b>. A peça está salva na sua conta com o nome que você deu — é só abrir o Tinkercad e ela está lá.",
 "avisos": [
   ("Projeto novo", "Esta aula começa num projeto novo, vazio. A peça da Aula 1 continua guardada na sua conta, do jeito que você deixou."),
   ("Milímetros", "Todo número é em milímetro. <b>50 mm</b> é o diâmetro de uma latinha de refrigerante pequena; <b>70 mm</b> é um pouco menos que a altura de um copo de requeijão."),
   ("O que é novo hoje", "O cilindro não tem campo de medida no painel. O tamanho se muda nos <b>números que aparecem quando você clica numa alça</b>. Também chegam o <span class=ui>Alinhar</span> e a seta <b>Ctrl + ↑</b>."),
   ("Os clipes", "Os passos com animação mostram o gesto inteiro: o mouse andando, o <b>botão certo acendendo</b> e o que muda na tela. Dá para trocar para a foto nas abas."),
   ("Travou?", "Todo passo tem um quadro laranja embaixo com o conserto dos erros mais comuns."),
 ],
 "passos": [

  dict(n=1, titulo="Abra o Tinkercad", img="aula2/d01_site.jpg", clipe=None,
    corpo="No navegador, vá para <span class=ui>tinkercad.com</span> e entre com a sua conta, como na Aula 1.<br><br>Sem entrar, você até consegue mexer, mas <b>nada fica salvo</b>: ao fechar a aba, a peça some.",
    ck="Você entrou: no canto de cima à direita aparece a bolinha da sua conta.",
    sos=[("Não tenho conta","Chame o professor. Se a escola te deu um código de turma, ele vai te dizer onde usá-lo — não clique em <span class=ui>Inscrever-se</span> por conta própria."),
         ("Esqueci minha senha","Chame o professor antes de criar outra conta. Conta nova começa vazia, e o que você fez na aula passada fica na antiga."),
         ("Minha página abriu em inglês","Role até o rodapé da página e troque o idioma para <b>Português</b>: todos os nomes desta aula são os de português.")]),

  dict(n=2, titulo="Clique no botão Criar", img="aula2/d02_depois.jpg", clipe="criar.gif",
    corpo="No canto de cima à direita, ao lado da bolinha da sua conta, clique no botão branco <span class=ui>+ Criar</span>.<br><br>Abre um menuzinho com três linhas.",
    ck="Abriu um quadro branco embaixo do botão, com três opções escritas: <span class=ui>Projeto 3D</span>, <span class=ui>Circuitos</span> e <span class=ui>Codeblocks</span>.",
    sos=[("Não acho o botão Criar","Ele fica na <b>faixa azul</b> do alto da página, bem à direita, logo antes da bolinha da sua conta."),
         ("Cliquei e não abriu nada","Clique uma vez só, em cima da palavra <span class=ui>Criar</span>. Dois cliques rápidos abrem e fecham o menu na mesma hora."),
         ("Abriu outra coisa","Você clicou na bolinha da conta, que fica ao lado. Feche apertando <span class=ui>Esc</span> e clique um pouco mais para a esquerda.")]),

  dict(n=3, titulo="Escolha Projeto 3D", img="aula2/d03_marcado.jpg", clipe=None,
    corpo="No menuzinho que abriu, clique na <b>primeira linha</b>: <span class=ui>Projeto 3D</span> — a do desenho de cubo, marcada de vermelho na figura.<br><br>O Tinkercad abre o editor e dá ao projeto um <b>nome sorteado</b>, meio esquisito. Deixe assim: no último passo você troca.",
    ck="A página mudou: sumiu a faixa azul e apareceu um <b>plano azul claro quadriculado</b> no meio da tela.",
    sos=[("Cliquei em Circuitos sem querer","Volte com a seta ⟵ do navegador e clique de novo em <span class=ui>+ Criar</span>, escolhendo a primeira linha."),
         ("A tela ficou branca e não carrega","O Tinkercad é pesado. Espere até meio minuto. Se continuar branca, recarregue com <span class=ui>F5</span>."),
         ("Abriu um projeto que eu já tinha","Você clicou numa capa da lista em vez do botão. Volte e use o <span class=ui>+ Criar</span> do canto de cima.")]),

  dict(n=4, titulo="Arraste um Cilindro para o plano", img="aula2/g04_depois.jpg", clipe="cilindro.gif",
    corpo="Na coluna da direita, a forma <b>laranja</b> do meio da segunda fileira é o <span class=ui>Cilindro</span>. (A de cima, cinza listrada, é o cilindro-<b>buraco</b>: hoje você pega a laranja.)<br><br>Segure o botão esquerdo em cima dela, <b>arraste até o meio do plano</b> e solte.<br><br>Abre o painel <span class=ui>Cilindro</span>, com <span class=ui>Lados</span>, <span class=ui>Chanfro</span> e <span class=ui>Segmentos</span>. <b>Não tem campo de medida</b> como a Caixa tinha: o tamanho do cilindro se muda de outro jeito, nos próximos passos.",
    ck="Tem um cilindro laranja no meio do plano, com quadradinhos brancos em volta, e o painel branco escrito <span class=ui>Cilindro</span> no alto.",
    sos=[("Peguei o cilindro cinza listrado","Esse é o <b>buraco</b>. Aperte <span class=ui>Delete</span> e arraste o laranja, o da segunda fileira."),
         ("O cilindro não parou no plano","Se a peça caiu longe, ela ainda está no plano: clique nela e arraste. O que importa é estar solta no plano, sem cobrir outra peça."),
         ("Não apareceu o painel","Clique uma vez no cilindro: o painel abre quando ele está selecionado.")]),

  dict(n=5, titulo="Clique na alça do canto", img="aula2/g06_depois.jpg", clipe="alca.gif",
    corpo="Em volta do cilindro há <b>quadradinhos brancos</b> — são as <b>alças</b>. Clique no quadradinho do canto de <b>cima à esquerda</b>.<br><br>Aparecem <b>dois números</b> no plano: um <b>em cima</b> do cilindro e outro <b>à esquerda</b>. São as medidas dele, em milímetro (o cilindro nasce com <b>20</b>).<br><br>O número de cima é a <b>largura</b>; o da esquerda é o <b>comprimento</b>.",
    ck="Apareceram dois números <b>20.00</b>, um em cima e outro à esquerda do cilindro, e o quadradinho clicado ficou vermelho.",
    sos=[("Não apareceu número nenhum","Você clicou em outro quadradinho ou fora da peça. Clique no cilindro de novo e depois no quadradinho de <b>cima à esquerda</b> da base."),
         ("Apareceu um número só, no meio","Esse é o quadradinho do <b>meio de cima</b>: ele mede a <b>altura</b> (passo 8). Hoje o certo é o do canto."),
         ("Arrastei o quadradinho e a peça mudou de tamanho","Sem problema: vamos digitar o tamanho exato agora. Mas clique só uma vez, sem arrastar.")]),

  dict(n=6, titulo="Largura = 50", img="aula2/g07_depois.jpg", clipe="largura.gif",
    corpo="Clique no número de <b>cima</b>. Ele vira um campo de escrever. Apague o 20, escreva <b>50</b> e aperte <span class=ui>Enter</span>.<br><br>O cilindro fica mais <b>largo</b>. O número da esquerda continua 20: ele mede outra direção.",
    ck="O cilindro ficou mais largo — como uma pizza que cresceu para o lado — e o número de cima agora mostra <b>50.00</b>.",
    sos=[("Digitei e nada mudou","Falta o <span class=ui>Enter</span> no fim. Sem ele o número não vale."),
         ("O número ficou estranho (tipo 20.0050)","O 20 antigo não foi apagado. Clique no número, aperte Ctrl + A (no Mac, Cmd + A) para selecionar tudo e escreva de novo."),
         ("Os números sumiram","Clique no cilindro e, de novo, no quadradinho do canto de cima à esquerda: eles aparecem outra vez.")]),

  dict(n=7, titulo="Comprimento = 50", img="aula2/g08_depois.jpg", clipe="comprimento.gif",
    corpo="Clique no número que está à <b>esquerda</b> do cilindro, no plano, apague o 20, escreva <b>50</b> e aperte <span class=ui>Enter</span>.<br><br>Agora o cilindro tem <b>50 × 50</b>: redondo de verdade. Se um número fosse diferente do outro, ele ficaria <b>oval</b>.",
    ck="O cilindro está redondo e largo: os dois números mostram <b>50.00</b>.",
    sos=[("Ficou oval","Os dois números têm de ser iguais. Clique na alça do canto de novo e confira os dois."),
         ("Digitei no número de cima de novo","O da <b>esquerda</b> é o comprimento. O de cima você já fez no passo anterior.")]),

  dict(n=8, titulo="Altura = 70: a alça de cima", img="aula2/g09_depois.jpg", clipe="altura.gif",
    corpo="Clique no quadradinho do <b>meio da tampa</b> (o do centro, em cima do cilindro). Aparece <b>um</b> número, ao lado: a <b>altura</b>.<br><br>Clique nele, apague o 20, escreva <b>70</b> e aperte <span class=ui>Enter</span>.<br><br>O cilindro vira um tubo alto: o corpo do porta-lápis.",
    ck="O cilindro ficou <b>alto</b>, bem mais alto que largo, e o número ao lado mostra <b>70.00</b>.",
    sos=[("Apareceram dois números","Você clicou num quadradinho de canto. O da altura fica no <b>meio</b> da tampa de cima."),
         ("A peça ficou altíssima","O 20 antigo não foi apagado e o número virou outro (2070, por exemplo). Clique no número, aperte Ctrl + A (no Mac, Cmd + A), escreva <b>70</b> e Enter."),
         ("Não achei o quadradinho do meio","Aproxime com o <b>+</b> da barra da esquerda, ou clique na peça de novo para ver as alças.")]),

  dict(n=9, titulo="Traga um segundo Cilindro, ao lado", img="aula2/g10_depois.jpg", clipe="cilindro2.gif",
    corpo="Clique num lugar vazio do plano (para soltar a seleção). Arraste <b>outro Cilindro laranja</b> da coluna da direita e solte <b>no plano, ao lado do tubo</b> — <b>não em cima dele</b>.<br><br>Esse segundo cilindro vai virar o <b>buraco</b>. Soltar em cima do tubo faria ele nascer lá no alto, na altura da tampa.",
    ck="Tem <b>dois</b> cilindros no plano: o tubo alto e um cilindro menor ao lado.",
    sos=[("O cilindro novo nasceu com outro tamanho","Normal: ele nasce com o tamanho do último que você mexeu. Não importa: os passos seguintes dão o tamanho certo."),
         ("O cilindro nasceu em cima do tubo","Arraste-o para o plano, para longe do tubo. Ele precisa estar <b>no chão</b>."),
         ("Soltei um cilindro cinza listrado","Esse já é o buraco, e tudo bem: pule o passo seguinte. Mas ele nasce com o tamanho padrão: siga os passos de medida.")]),

  dict(n=10, titulo="Transforme o cilindro em Orifício", img="aula2/g11_depois.jpg", clipe="orificio.gif",
    corpo="Com o cilindro pequeno selecionado, no painel branco clique em <span class=ui>Orifício</span> (a bolinha cinza listrada, à direita de <span class=ui>Sólido</span>).<br><br>O cilindro fica <b>cinza e listrado</b>: agora ele é um <b>buraco</b> — onde ele tocar uma peça sólida, vai cavar.",
    ck="O cilindro pequeno ficou <b>cinza e listrado</b>, e no painel o <span class=ui>Orifício</span> está marcado.",
    sos=[("Nada mudou de cor","Clique <b>na palavra</b> ou na bolinha do <span class=ui>Orifício</span>, e confirme que o cilindro pequeno está selecionado (com as alças)."),
         ("O tubo é que ficou listrado","Você estava com o tubo selecionado. Clique no <span class=ui>Sólido</span> para desfazer e selecione o cilindro pequeno.")]),

  dict(n=11, titulo="Encolha o furo: 42 × 42", img="aula2/g12_depois.jpg", clipe="furo_planta.gif",
    corpo="Com o furo selecionado, clique na <b>alça do canto</b> de cima à esquerda, como no passo 5. Clique no número da <b>esquerda</b>, escreva <b>42</b>, <span class=ui>Enter</span>. Depois clique no número de <b>cima</b>, escreva <b>42</b>, <span class=ui>Enter</span>.<br><br>O furo tem <b>42 mm</b> de largura e o tubo tem 50: sobram <b>4 mm</b> de parede de cada lado (50 − 42 = 8, e 8 ÷ 2 = 4).",
    ck="O furo ficou <b>menor</b> que o tubo, e os dois números dele mostram <b>42.00</b>.",
    sos=[("Digitei 42 e o tubo é que mudou","Você estava com o tubo selecionado. Clique no <b>furo</b> (cinza listrado) e refaça."),
         ("O furo ficou oval","Os dois números têm de ser <b>42</b>. Clique na alça do canto de novo e confira.")]),

  dict(n=12, titulo="Altura do furo = 70", img="aula2/g13_depois.jpg", clipe="furo_altura.gif",
    corpo="Clique na <b>alça de cima</b> — o quadradinho do <b>meio da tampa</b> do furo —, clique no número que aparece, escreva <b>70</b> e aperte <span class=ui>Enter</span>.<br><br>O furo fica tão <b>alto</b> quanto o tubo. Ele ainda está <b>no chão</b>: no próximo passo você levanta.",
    ck="O furo cinza ficou alto, do tamanho do tubo, e o número ao lado mostra <b>70.00</b>.",
    sos=[("O número é outro","Se mostrar um valor diferente de 70, clique nele e escreva 70 de novo."),
         ("Apareceram dois números","Você clicou num canto. A altura fica no <b>meio</b> da tampa.")]),

  dict(n=13, titulo="Suba o furo 5 mm: Ctrl + ↑, cinco vezes", img="aula2/g14_depois.jpg", clipe="sobe.gif",
    corpo="Com o furo ainda selecionado, aperte <b>Ctrl + ↑</b> (a seta para cima) <b>cinco vezes</b>, uma por vez. Cada toque sobe a forma <b>1 mm</b>.<br><br>Por quê? Se o furo ficar no chão, ele <b>atravessa</b> o tubo todo e sobra só um canudo, sem fundo. Subindo 5 mm, os 5 mm de baixo do tubo <b>ficam inteiros</b>: é o <b>fundo</b> do porta-lápis.",
    ck="O furo está <b>um tiquinho mais alto</b> que no passo anterior: a base dele subiu e já não encosta no plano. Sem número na tela, a conferência de verdade vem nos passos 18 e 19.",
    sos=[("Não subiu","Confira se o furo continua selecionado (com as alças). No Mac use <span class=ui>Ctrl</span> mesmo, não o Cmd."),
         ("Subiu demais ou de menos","Cada toque é 1 mm. Aperte Ctrl + ↓ para descer um e Ctrl + ↑ para subir um, até dar 5 no total.")]),

  dict(n=14, titulo="Selecione tudo: Ctrl + A", img="aula2/g15_depois.jpg", clipe="seleciona.gif",
    corpo="Aperte <b>Ctrl + A</b>. O tubo e o furo ficam selecionados juntos: o painel passa a dizer <span class=ui>Shapes(2)</span> (duas formas).<br><br>No Mac, aperte <b>Cmd + A</b> no lugar do Ctrl.",
    ck="As duas formas têm contorno azul e o painel diz <span class=ui>Shapes(2)</span>.",
    sos=[("Selecionou só uma","Clique num lugar vazio do plano e aperte Ctrl + A de novo."),
         ("Não aconteceu nada","O Ctrl + A só funciona com a tela do editor em foco. Clique num lugar vazio do plano e tente de novo.")]),

  dict(n=15, titulo="Abra o Alinhar", img="aula2/g16_depois.jpg", clipe="alinhar.gif",
    corpo="Na barra de cima, clique no botão <span class=ui>Alinhar</span> (o ícone com linhas de tamanhos diferentes, ao lado do espelho).<br><br>Aparecem <b>nove bolinhas pretas</b> em volta das formas: <b>três embaixo</b> (esquerda, meio e direita), <b>três do lado esquerdo</b> (frente, meio e atrás) e três do lado direito (altura). Cada bolinha alinha as duas formas por aquele lado.",
    ck="Apareceram nove bolinhas pretas em volta das formas, e no alto uma frase: <i>Clique nas alças para alinhar as formas</i>.",
    sos=[("Não acho o botão Alinhar","Fica na barra de cima, no meio, entre o ícone de agrupar e o do espelho. Passe o mouse e espere: o nome aparece."),
         ("As bolinhas não apareceram","O Alinhar só abre com <b>duas ou mais</b> formas selecionadas. Volte ao passo 14.")]),

  dict(n=16, titulo="Centro em X: a bolinha do meio, embaixo", img="aula2/g17_depois.jpg", clipe="alinha_x.gif",
    corpo="Clique na <b>bolinha do meio</b> da fileira de <b>baixo</b>.<br><br>As duas formas se <b>centram</b> na direção da esquerda para a direita: o furo se encaixa no meio do tubo, de lado a lado.",
    ck="O furo ficou no <b>meio do tubo</b> da esquerda para a direita; ainda pode estar deslocado para a frente ou para trás.",
    sos=[("Alinhou na esquerda, não no meio","Você clicou na bolinha da ponta. Aperte Ctrl + Z e clique na do <b>meio</b>."),
         ("As bolinhas mudaram de lugar","É normal: depois de cada clique elas se reposicionam. Procure de novo a do meio.")]),

  dict(n=17, titulo="Centro em Y: a bolinha do meio, à esquerda", img="aula2/g18_depois.jpg", clipe="alinha_y.gif",
    corpo="Clique na <b>bolinha do meio</b> da coluna da <b>esquerda</b>.<br><br>Agora o furo também está centrado de <b>frente para trás</b>. Olhando de cima, ele ficaria no meio exato do tubo — com <b>4 mm de parede por toda a volta</b>.",
    ck="O furo está no meio do tubo nos dois sentidos: a abertura redonda aparece no centro da tampa.",
    sos=[("Clicou na bolinha errada","Aperte Ctrl + Z e clique na do <b>meio</b> da coluna da esquerda."),
         ("O furo ainda está torto","Faça os dois passos: o do meio embaixo (passo 16) e o do meio à esquerda (este).")]),

  dict(n=18, titulo="Aperte Esc e agrupe: Grupo de união", img="aula2/g19_depois.jpg", clipe="uniao.gif",
    corpo="Primeiro aperte <span class=ui>Esc</span>: ele fecha o Alinhar e <b>mantém as duas formas selecionadas</b>. Sem isso o botão de agrupar não responde.<br><br>Na barra de cima há três botõezinhos de juntar peças, à direita do meio. Clique no <b>do meio</b>, o <span class=ui>Grupo de união</span> (ao passar o mouse aparece o nome).<br><br>O furo <b>cava</b> o tubo, e as duas formas viram uma <b>peça só</b>: o painel passa a dizer <span class=ui>Union</span> (união).",
    ck="O tubo agora tem uma <b>abertura por dentro</b>, e o painel diz <span class=ui>Union</span> e <span class=ui>Tipo de grupo: união</span>.",
    sos=[("O botão não respondeu","Falta apertar <span class=ui>Esc</span> antes. Se as bolinhas pretas ainda estão na tela, o Alinhar não fechou."),
         ("Cavou tudo e sobrou um canudo","O furo ficou no chão. Aperte Ctrl + Z, selecione o furo e suba 5 mm (passo 13) antes de agrupar."),
         ("Agrupei e sumiu o furo, sobrou o tubo inteiro","Você usou o botão errado. Aperte Ctrl + Z e escolha o <b>Grupo de união</b>, e não o de ao lado.")]),

  dict(n=19, titulo="Olhe de cima: o fundo ficou?", img="aula2/g20_depois.jpg", clipe="vista_cima.gif",
    corpo="Clique num lugar vazio do plano para soltar a peça. No canto de cima à esquerda, no <b>cubo</b> de vistas, clique na face escrita <span class=ui>SUPERIOR</span>.<br><br>A câmera sobe e você olha <b>de cima</b>: o tubo é um <b>anel</b> de parede e, <b>dentro</b> dele, aparece o <b>fundo laranja</b>. Se desse para ver o plano branco no meio, o furo teria atravessado.",
    ck="Olhando de cima, aparece o aro da parede e um círculo <b>laranja</b> no fundo do furo — e não o plano branco.",
    sos=[("Dá para ver o plano no meio do furo","O furo atravessou: ficou no chão. Aperte Ctrl + Z até o furo voltar, suba 5 mm e agrupe de novo."),
         ("A câmera não mudou","Clique <b>na palavra</b> SUPERIOR do cubinho. Para voltar à vista inicial use a casinha da barra da esquerda."),
         ("Está tudo laranja, não vejo anel","Gire a câmera com o botão <b>direito</b> do mouse até enxergar a abertura em cima.")]),

  dict(n=20, titulo="Dê um nome ao seu projeto", img="aula2/g21_depois.jpg", clipe="batiza.gif",
    corpo="Clique no <b>nome do projeto</b>, no canto de cima à esquerda (o nome sorteado). Apague, escreva <b>Porta-lápis da ANA</b> (ou o seu nome) e aperte <span class=ui>Enter</span>. (A câmera pode continuar olhando de cima: não atrapalha.)<br><br>O Tinkercad salva sozinho. No outro dia, é só abrir o Tinkercad e a peça está lá.",
    ck="No canto de cima à esquerda aparece o <b>nome que você escreveu</b>, no lugar do sorteado.",
    sos=[("O nome não mudou","Falta o <span class=ui>Enter</span>. Clique no nome de novo e faça de novo."),
         ("Clicou e o campo não abriu","Clique <b>em cima das letras</b> do nome, e não ao lado.")]),
 ],
}
