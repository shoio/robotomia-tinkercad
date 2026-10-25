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
| 2 | **Caneca e porta-lápis** | caneca com alça e porta-lápis de furos | esvaziar por dentro (cilindro + orifício menor), alça, formas redondas |
| 3 | **Casinha** | casa com telhado, porta e janelas | Telhado/Cunha, **alinhar** formas, furos de porta e janela |
| 4 | **Carrinho** | carro com quatro rodas | girar uma forma em 90°, **duplicar**, simetria, rodas que se encontram com o corpo |
| 5 | **Foguete** | foguete com três aletas | Cone, **Duplicar e repetir** (`Ctrl+D`), peças em volta de um eixo |
| 6 | **Robô de formas** | robô com cabeça, corpo, braços e olhos | muitas formas, **cores**, esfera, empilhar no eixo certo |
| 7 | **Dado** | dado de seis lados com pontos | cubo com **furos esféricos**, os pontos de cada face, faces opostas somam 7 |
| 8 | **Porta-celular** | suporte inclinado para o celular | ângulo (girar com a régua), cunha, ranhura, medir o aparelho |
| 9 | **Régua e escala** | cubo de 1 cm e uma régua de 10 cm | **Régua**, medir com exatidão, **escala** (a peça maior ou menor) |
| 10 | **Peça que encaixa** | pino e furo que se encaixam | folga/tolerância, encaixe macho e fêmea |
| 11 | **Pequena cidade** | prédios de alturas diferentes numa base | repetir com variação, base, planejar antes de montar |
| 12 | **Projeto livre e mostra** | a peça do aluno, com link | escolher, montar com o kit das 11 aulas, **compartilhar** |

**Por que nesta ordem:** a 1 e a 2 são o mesmo truque (um buraco dentro de um
corpo) em escala maior. 3 a 6 são as ações que sustentam qualquer modelo
(alinhar, girar, duplicar, repetir, pintar). 7 a 10 são as que pedem precisão
(furo certo, ângulo, medida, folga) — o que separa «um desenho bonito» de uma
peça que **daria para imprimir**. 11 junta tudo num cenário, 12 fecha como a
Aula 12 do Flowlab: projeto próprio e mostra.

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
