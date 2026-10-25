# Curso de Tinkercad da Robotomia — plano

Escrito em 24-10-2026, ao retomar o curso (só a Aula 1 existia, e o índice
prometia a Aula 2 sem nada construído). Formato herdado dos cursos de Roblox e
Flowlab, e a fábrica é a da Aula 1 (`PADRAO.md`): 19 a 21 passos por aula,
quadro verde, quadro laranja, clipe por gesto novo, capturas reais.

⚠️ **As linhas 2 a 12 são PROMESSA, não inventário.** Cada aula só entra no ar
depois de a mecânica ter sido **provada no editor** (passo 1 do laço, abaixo).
Quando a medida contradisser a tabela, a tabela perde — e é corrigida aqui.

---

## 1. O que o aluno aprende, em ordem

Uma ideia por aula, e cada ideia usa a anterior.

| # | Aula | A peça que sai pronta | O que é novo |
|---|---|---|---|
| 1 | **Chaveiro com o seu nome** *(no ar)* | plaquinha 90×30×4 com nome em relevo e furo | Caixa, medidas, Texto, Orifício, agrupar, câmera |
| 2 | **Porta-lápis** *(no ar)* | copo de 50×70 mm com fundo de 5 mm | números das alças (o cilindro não tem campo), subir com `Ctrl+↑`, **Alinhar**, olhar de cima |
| 3 | **Caneca com alça** | caneca com alça de anel | Tórulo, **girar** uma forma em pé (seta de girar, 90°), posicionar com as setas, agrupar |
| 4 | **Casinha** | casa com telhado, porta e janelas | Telhado, furos de porta e janela, alinhar na base |
| 5 | **Carrinho** | carro com quatro rodas | girar 90°, **duplicar**, espelhar, rodas que se encontram com o corpo |
| 6 | **Foguete** | foguete com três aletas | Cone, **Duplicar e repetir** (`Ctrl+D`), peças em volta de um eixo |
| 7 | **Robô de formas** | robô com cabeça, corpo, braços e olhos | muitas formas, **cores**, esfera, empilhar no eixo certo |
| 8 | **Dado** | dado de seis lados com pontos | cubo com **furos esféricos**, os pontos de cada face, faces opostas somam 7 |
| 9 | **Porta-celular** | suporte inclinado para o celular | ângulo, cunha, ranhura, medir o aparelho |
| 10 | **Régua e escala** | cubo de 1 cm e uma régua de 10 cm | **Régua**, medir com exatidão, **escala** (a peça maior ou menor) |
| 11 | **Peça que encaixa** | pino e furo que se encaixam | folga/tolerância, encaixe macho e fêmea |
| 12 | **Projeto livre e mostra** | a peça do aluno | escolher, montar com o kit das 11 aulas, **compartilhar** |

**Por que nesta ordem:** a 1 e a 2 são o mesmo truque (um buraco dentro de um
corpo) em escala maior; a 3 acrescenta a alça (girar e posicionar). 4 a 7 são
as ações que sustentam qualquer modelo (furos de parede, duplicar, repetir,
pintar). 8 a 11 são as que pedem precisão (furo certo, ângulo, medida, folga)
— o que separa «um desenho bonito» de uma peça que **daria para imprimir**.
12 fecha como a Aula 12 do Flowlab: projeto próprio e mostra.

*(Em 25-10: a «Caneca e porta-lápis» virou DUAS aulas — a alça pede girar e
posicionar, e junto com o corpo passava de 21 passos —, e a «Pequena cidade»
saiu para o plano continuar em 12.)*

---

## 2. O formato de cada aula

Igual à Aula 1: 19 a 21 passos, cada um com a foto da tela de verdade; clipe
nos gestos novos (o mouse mostra **qual botão afunda**; teclado mostra **qual
tecla acende**); quadro verde = como o aluno sabe que deu certo, pelo que
APARECE; quadro laranja = sintoma na voz da criança + conserto; fim = o
projeto salvo.

---

## 3. A máquina e o seu limite

`fonte/bancada.py` dirige o editor do Tinkercad por Playwright, **em headless**,
achando cada botão no DOM (nome acessível, dica ou texto). Tudo o que
`PADRAO.md` diz da Aula 1 vale aqui.

⛔ **Precisa de um perfil do Chromium já logado.** O perfil mora fora do
repositório (`TINK_PERFIL`, padrão `/private/tmp/tinkprofile`) e **some com o
`/tmp`**. Quando ele não existe, o dono entra de novo numa janela que a
máquina abre — a senha nunca passa pelo chat, e eu nunca copio cookie do
navegador dele.

⛔ **Um projeto só do Tinkercad** (`TINK_PROJ`), limpo no começo de cada
execução, para não encher a conta do dono. Se o projeto antigo não existir
mais, cria-se UM novo e o endereço dele vai para `PADRAO.md` §8.

---

## 4. Como cada aula é construída (o laço)

1. **Provar a mecânica no editor**, antes de escrever a aula: cada forma, cada
   campo, cada atalho que a aula vai pedir — medido na tela, anotado no
   `PADRAO.md`. Foi assim que a Aula 1 achou as quatro pegadinhas (largura,
   campo `Text`, furo em z = 4, painel do Cilindro).
2. Escrever o roteiro dos 19 a 21 passos.
3. `capN.py`: o robô constrói a peça e fotografa cada gesto. **Peça se mede na
   captura anterior**, nunca se combina um ponto (`PADRAO.md` §2).
4. Montar clipes e JPEG; rodar os três guardas.
5. **Provar a peça**: dá para ver o chão pelo furo? a alça está colada na caneca?
   o dado tem 21 pontos? A prova olha o que a aula promete.
6. **Engenharia reversa**: reler a aula como aluno, passo a passo, sem usar o que
   eu sei, e consertar o que faltar, sobrar ou estiver errado. É a passada que
   acha o passo *certo e incompleto*, que nenhum guarda pega.
7. Build, publicar, conferir **no ar**.

---

## 5. O que pode dar errado, dito antes

- **Gesto de câmera e de seleção por arrasto** são os mais finos: o canvas é
  WebGL, e um clique 5 px fora seleciona o plano de trabalho em vez da peça.
- **Formas que colam no plano de trabalho** (a pegadinha do furo em z = 4) vão
  voltar em toda aula que solta uma forma em cima de outra.
- **Cor** no Tinkercad mora numa paleta que abre por cima do painel; o clipe
  precisa mostrar a paleta aberta.
- **Tempo:** a Aula 1 levou uma sessão inteira para a máquina; as seguintes
  reaproveitam `bancada.py`, e o custo cai para o das medidas novas.
