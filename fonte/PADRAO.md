# PADRÃO — curso de modelagem 3D no Tinkercad

O formato da aula (19 a 21 passos, quadro verde, quadro laranja, clipe por
gesto novo) vem dos cursos de Roblox e Flowlab e **não se reinventa**. Este
arquivo registra só o que é DIFERENTE aqui, e cada regra nasceu de um defeito
que apareceu na bancada — nenhuma é preferência de estilo.

---

## 0. Como se roda

```
fonte/cap0.py          passos 1–3: site, menu Criar, item Projeto 3D
fonte/cap1.py          passos 4–20: a peça inteira, no editor, em headless
fonte/faz_gifs1.py     monta os 16 clipes a partir das capturas
fonte/build_curso.py   guardas + site na raiz + PDF
```

Precisa de `TINK_PERFIL` apontando para um perfil do Chromium **já logado** no
Tinkercad. A senha nunca passa por aqui: quem digita é o dono, na janela.

```
TINK_PERFIL=/caminho/do/perfil  ./pwenv/bin/python fonte/cap1.py
TINK_SABOTA=1 ...                pula a descida do furo (prova do guarda)
```

---

## 1. O alvo vem do DOM, não de OCR

Nos cursos irmãos o botão do clipe se acha por leitura óptica da tela. Aqui se
acha no DOM, por nome acessível, dica (tooltip) ou texto. Isso muda o guarda:
em vez de *"a seta cai perto de alguma coisa escrita"*, dá para exigir o
invariante de verdade —

> **o rótulo do elemento em que a máquina clicou tem de aparecer no texto do
> passo que usa aquele clipe** (`confere_gesto.py`).

`acha()` procura em duas passadas: primeiro elemento-folha ou com `aria-label`;
só se não achar, o **menor** elemento cujo texto inteiro é o nome. A segunda
passada existe porque os itens do menu «Criar» são `<a>` com ícone dentro.
E só vale o que está **dentro da janela**: «Projeto 3D» já casou com um
elemento a 1441 px de altura, fora da tela.

---

## 2. Posição de peça é MEDIDA, nunca combinada

A plaquinha muda de tamanho e de lugar a cada medida digitada. Soltar o nome
num ponto fixo da tela deixou as letras fora da peça. O certo é
`bbox_vermelho()` na captura anterior e soltar a partir dela.

E o retângulo em que se procura a peça **não é** o do plano de trabalho: o
painel de propriedades tem uma bolinha **vermelha** («Sólido») dentro dele. Com
o recorte errado, uma peça de 247×84 px «mediu» 514×374.

---

## 3. Os três fatos do Tinkercad que ninguém acerta de cabeça

1. **O número grande vai em `Largura`.** Na vista inicial, quem corre na
   horizontal da tela é a largura, e a forma Texto escreve nessa direção. Pôr
   o 90 em `Comprimento` deixa a plaquinha apontando para longe e o nome
   atravessado nela.
2. **O campo do nome chama `Text`, em inglês**, num painel todo em português.
   Procurar «Texto» acha o *título do painel* (o nome da forma), não o campo.
3. **O furo nasce em cima da peça.** Ao soltar uma forma sobre a face de outra,
   o Tinkercad cria um plano de trabalho ali (o quadrado verde) e a nova peça
   começa em z = 4 mm. Agrupar assim não cava nada. `Ctrl + ↓` desce 1 mm por
   toque.

E um quarto, menor: o painel do **Cilindro** só tem `Lados`, `Chanfro` e
`Segmentos` — não tem comprimento nem largura. Quem traz os três campos é a
`Caixa`.

---

## 4. Tipo de gesto é gravado, não adivinhado

`alvos.json` guarda `tipo` em cada gesto: `clique`, `arrasto` ou `tecla`
(e `botao` quando é o direito).

- **Nunca desenhar atalho de teclado como clique.** `Ctrl + ↓` e `Ctrl + A`
  saíram na primeira montagem com a seta caminhando até a peça e um anel
  vermelho em cima dela. A criança copia a animação, clica ali e não acontece
  nada — a animação é a parte da página que ela realmente imita.
- **Arrasto de girar a câmera é com o botão DIREITO**, e o desenho do mouse
  mostra qual botão afunda. Desenhado como arrasto comum, a criança segura o
  esquerdo e arrasta a *peça* para fora do lugar.

---

## 5. Enquadramento do clipe é calculado — e inclui o que MUDA

A janela é a menor 16:10 que contém, com margem:

1. o gesto inteiro (de onde a seta sai até onde ela chega), **e**
2. a **região em que a tela mudou** entre o quadro de antes e o de depois,
   medida em blocos de 8 px (`caixa_mudanca()`).

O item 2 não estava lá no começo, e o dono viu o estrago antes de mim: nos
clipes de encolher a caixinha e de virar Orifício, a janela saía só do ponto do
clique — então ela enquadrava o painel e **cortava a plaquinha ao meio** na
borda esquerda. A peça é justamente o que a criança precisa ver mudar.

Três regras de desenho vieram junto, e cada uma é um jeito diferente de o
marcador estragar o quadro:

- **A janela pode passar da borda da captura** (até `SOBRA` = 70 px), e o que
  passa vira margem cinza. Presa dentro da captura, alvo colado na quina (o
  nome do projeto, a casinha) ficava a ~21 px da borda e o anel de clique saía
  cortado — um risco vermelho que ninguém reconhece como clique.
- **O anel encolhe para caber inteiro** no quadro.
- **O desenho do mouse é ancorado no rodapé**, no mesmo lugar das teclas, e não
  segue o cursor. Colado nele, o mouse tapava a palavra que o passo manda ler:
  no clipe da Altura o rótulo do campo saiu como *"ura"*. É o mesmo defeito do
  círculo que escondia «Projeto 3D» — **marca de passo não pode esconder o que
  o passo manda ler**.

O `faz_gifs1.py` confere tudo isso antes de gravar: os pontos do gesto e os dois
cantos da região mudada têm de cair dentro do recorte, e a seta precisa de pelo
menos 26 px de folga até a borda (senão o anel só cabe encolhido, que é o mesmo
defeito disfarçado de certo).

---

## 6. Privacidade: o painel do dono não vai para o site

O painel do Tinkercad mostra o **nome real** do dono e as capas de dezenas de
projetos particulares. O curso é público.

- O passo 1 é fotografado numa sessão **sem conta** (contexto novo, sem perfil,
  com `locale="pt-BR"` — sem o locale o Tinkercad serve tudo em inglês).
- Os passos 2 e 3 recortam só o canto de cima à direita.
- `sem_vazamento()` reprova a captura se qualquer texto do dono cair dentro do
  recorte. Na primeira execução ele reprovou — e disse o nome dele.

---

## 7. Os guardas, e a prova de cada um

Os três rodam no começo do `build_curso.py` e **param o build**.

| guarda | invariante | sabotagem que o prova |
|---|---|---|
| `confere_aulas.py` | o passo tem foto, clipe, quadro verde e laranja; não delega; diz onde clicar; nenhuma foto repetida; nada mais velho que `projeto.txt` | duas fotos iguais (já pegou uma de verdade: passos 18 e 20) |
| `confere_alvos.py` | o **fim** do gesto cai onde a tela mudou, com controle negativo | `--prova` arrasta um alvo para um canto morto |
| `confere_gesto.py` | o rótulo do alvo aparece no texto do passo | trocar o clipe de dois passos |

Duas armadilhas de número herdado, para não repetir:

- o mínimo de pixels mudados **não é** o 400 do Flowlab. Digitar 30 onde estava
  20 muda 217 px, e o guarda chamava isso de seta no vazio. O 60 daqui é
  medido: janela inerte do mesmo par dá **0 px**.
- as janelas de **controle negativo** são declaradas **por tamanho de quadro**.
  Janela que cai fora da imagem faz o numpy devolver fatia vazia, a soma dá 0,
  e o controle passa a aprovar tudo sem medir nada.

---

## 8. Um projeto só do Tinkercad

Todas as execuções usam **o mesmo** projeto (`TINK_PROJ`) e o limpam no começo,
para não encher a conta do dono. Por isso `cap1.py` escreve
`aula1/projeto.txt` a cada execução: como os arquivos têm sempre os mesmos
nomes, uma figura que sobrou de uma execução anterior não chamaria atenção de
ninguém. O guarda compara a data de cada quadro com esse arquivo.

O nome do projeto é **devolvido ao nome sorteado** no começo de cada execução,
senão o passo 20 (dar nome) não muda nada na tela e vira animação de nada.
