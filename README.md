# G14_Programacao_Dinamica_PA-26.1

Número da Dupla: 14  
Conteúdo da Disciplina: Programação Dinâmica  
Vídeo da Apresentação: a adicionar

## Alunas

| Matrícula | Aluna |
| --- | --- |
| 231026840 | Laryssa Félix |
| 231027005 | Maria Samara |

## Sobre

### ProvaMax: Planejador Inteligente de Estudos com Programação Dinâmica

Este projeto tem como objetivo demonstrar a aplicação prática do paradigma de Programação Dinâmica por meio da implementação do algoritmo **Knapsack**.

O sistema simula uma situação real em que um estudante possui tempo limitado antes de uma prova e precisa decidir quais conteúdos estudar para obter o maior retorno possível. Nesta versão do sistema, os conteúdos são fornecidos por meio de uma lista pré-definida no código-fonte, utilizada para demonstrar o funcionamento do algoritmo.

A partir dessas informações, o sistema calcula uma pontuação de prioridade para cada conteúdo e utiliza Programação Dinâmica para selecionar a melhor combinação de assuntos que respeita o tempo disponível.

Além de encontrar a pontuação máxima, o projeto permite visualizar os conteúdos escolhidos, os conteúdos não escolhidos, o tempo utilizado e a matriz de Programação Dinâmica construída durante a execução.

## Modelagem do Problema

O problema é modelado como uma variação do problema clássico da mochila.

Cada conteúdo da prova é tratado como um item que pode ser escolhido ou descartado. Como um conteúdo não pode ser estudado parcialmente, cada item só possui duas possibilidades: entrar ou não entrar no plano de estudos.

| Conceito no Knapsack | Conceito no Projeto |
| --- | --- |
| Item | Conteúdo da prova |
| Peso | Tempo necessário para estudar |
| Valor | Prioridade do conteúdo |
| Capacidade | Tempo disponível antes da prova |

Cada conteúdo possui:

- Nome
- Tempo necessário de estudo
- Importância na prova
- Dificuldade
- Domínio atual do aluno

Exemplo:

| Conteúdo | Tempo | Importância | Dificuldade | Domínio atual |
| --- | ---: | ---: | ---: | ---: |
| Knapsack | 3h | 10 | 8 | 4 |
| LIS | 2h | 7 | 5 | 6 |
| Bellman-Ford | 4h | 9 | 9 | 3 |

Neste exemplo, **Knapsack**, **LIS** e **Bellman-Ford** aparecem como conteúdos que o estudante pode precisar revisar para uma prova de algoritmos. O algoritmo utilizado pelo sistema para montar o plano de estudos é o **Knapsack 0/1 com Programação Dinâmica**.

A partir desse conjunto, o sistema deve responder perguntas como:

- Quais conteúdos devem ser estudados dentro do tempo disponível?
- Qual é a maior pontuação possível?
- Quanto tempo será utilizado?
- Quais conteúdos ficaram fora do planejamento?
- Como a matriz de Programação Dinâmica foi preenchida?

## Fórmula de Prioridade

Para que o projeto não considere apenas a importância do conteúdo, foi definida uma fórmula de prioridade que combina três fatores:

```text
prioridade = importância + dificuldade - domínio_atual
```

Onde:

- **Importância** representa o quanto o conteúdo pesa na prova.
- **Dificuldade** representa o quanto o conteúdo é complexo.
- **Domínio atual** representa o quanto o aluno já conhece aquele conteúdo.

Assim, conteúdos importantes, difíceis e pouco dominados recebem maior prioridade.

Exemplo:

```text
importância = 9
dificuldade = 8
domínio atual = 3

prioridade = 9 + 8 - 3 = 14
```

## Algoritmo Utilizado: Knapsack

Para resolver o problema, foi utilizado o algoritmo **Knapsack** com abordagem iterativa de Programação Dinâmica.

O funcionamento do algoritmo pode ser resumido em:

1. Recebe a lista de conteúdos e o tempo total disponível.
2. Cria uma matriz de Programação Dinâmica.
3. Para cada conteúdo, avalia todos os limites de tempo possíveis.
4. Decide entre:
   - não estudar o conteúdo atual;
   - estudar o conteúdo atual, caso exista tempo suficiente.
5. Armazena na matriz a melhor pontuação possível para cada subproblema.
6. Ao final, reconstrói a solução ótima a partir da matriz.

No contexto do sistema:

- Cada linha da matriz representa a análise de um conteúdo.
- Cada coluna representa uma quantidade de tempo disponível.
- Cada célula guarda a melhor pontuação possível para aquele subproblema.
- O valor final da matriz representa a maior pontuação possível.
- A reconstrução da matriz indica quais conteúdos fazem parte do plano ótimo.

## Funcionamento do Sistema

O sistema desenvolvido permite:

- Utilizar uma lista pré-definida de conteúdos de estudo.
- Calcular a prioridade de cada conteúdo.
- Executar o algoritmo Knapsack 0/1.
- Construir a matriz de Programação Dinâmica.
- Reconstruir os conteúdos escolhidos.
- Calcular a pontuação máxima.
- Calcular o tempo total utilizado.
- Identificar os conteúdos não escolhidos.
- Exibir os resultados formatados no terminal.
- Executar testes automatizados da lógica principal.

## Screenshots

<!-- Os prints serão adicionados quando a implementação final da interface estiver pronta. -->

### Tela Inicial

Representa o estado inicial do sistema, onde o usuário poderá escolher uma das funcionalidades disponíveis.

image

### Conteúdos Disponíveis

Apresenta a lista pré-definida de conteúdos utilizada pelo sistema como entrada para o algoritmo.

image

### Execução do Planejamento

Exibe o resultado da execução do algoritmo Knapsack 0/1 para o tempo disponível informado.

image

### Conteúdos Escolhidos

Mostra os conteúdos selecionados para compor o plano ótimo de estudos.

image

### Conteúdos Não Escolhidos

Mostra os conteúdos que ficaram fora do plano por causa do limite de tempo.

image

### Matriz de Programação Dinâmica

Demonstra a matriz preenchida pelo algoritmo para evidenciar o uso de Programação Dinâmica.

image


## Instalação

### Linguagem

Python 3.10+

### Pré-requisitos

- Python 3 instalado
- Git instalado

### Passos

Clone o repositório:

```bash
git clone <url-do-repositorio>
cd G14_Programacao_Dinamica_PA-26.1
```

## Uso

Para executar o projeto, utilize o seguinte comando:

```bash
python3 main.py
```

Após executar, o sistema utiliza uma lista pré-definida de conteúdos, calcula suas prioridades e gera automaticamente o plano de estudos ótimo utilizando o algoritmo Knapsack 0/1.

Para executar os testes automatizados:

```bash
python3 -m unittest discover -s tests
```

## Regras do Sistema

O sistema trabalha com uma lista de conteúdos cadastrados.

Cada conteúdo deve possuir:

- Nome
- Tempo necessário de estudo
- Importância
- Dificuldade
- Domínio atual

As notas de importância, dificuldade e domínio atual devem estar entre 0 e 10.

O tempo de estudo deve ser maior que zero.

O tempo disponível representa a capacidade total da mochila. Portanto, a soma dos tempos dos conteúdos escolhidos não pode ultrapassar esse limite.

Como o problema é do tipo 0/1, cada conteúdo pode ser escolhido no máximo uma vez.

## Como o Plano de Estudos é Encontrado

O sistema utiliza Programação Dinâmica para avaliar combinações possíveis de conteúdos.

Processo:

1. Calcula a prioridade de cada conteúdo.
2. Cria uma matriz com `n + 1` linhas e `T + 1` colunas.
3. Percorre os conteúdos um por um.
4. Para cada conteúdo, testa todos os limites de tempo de `0` até `T`.
5. Decide se vale mais manter a solução anterior ou incluir o conteúdo atual.
6. Armazena o melhor resultado na matriz.
7. Reconstrói a solução ótima voltando pela matriz.

Onde:

- `n` é a quantidade de conteúdos.
- `T` é o tempo total disponível.

## Exemplo de Entrada

| Conteúdo | Tempo | Importância | Dificuldade | Domínio atual | Prioridade |
| --- | ---: | ---: | ---: | ---: | ---: |
| Knapsack | 3h | 10 | 8 | 4 | 14 |
| LIS | 2h | 7 | 5 | 6 | 6 |
| Bellman-Ford | 4h | 9 | 9 | 3 | 15 |

Tempo disponível:

```text
7h
```

## Exemplo de Saída

```text
Plano de estudos sugerido
Pontuacao maxima: 29
Tempo utilizado: 7h
Conteudos escolhidos:
- Knapsack
- Bellman-Ford
```

Nesse exemplo, o sistema escolhe Knapsack e Bellman-Ford porque essa combinação utiliza exatamente as 7 horas disponíveis e gera a maior pontuação possível.

Aqui, Bellman-Ford é apenas um conteúdo de estudo selecionado pelo planejamento, assim como Knapsack e LIS. Ele não é o algoritmo executado pelo sistema.

## Comparação com Estratégia Gulosa

Como melhoria do projeto, também será utilizada uma estratégia gulosa para comparação.

Uma abordagem gulosa pode escolher primeiro os conteúdos com maior prioridade individual. Porém, essa decisão local nem sempre gera o melhor resultado global, pois um conteúdo muito prioritário pode ocupar tempo demais e impedir uma combinação melhor.

A Programação Dinâmica, por outro lado, avalia subproblemas e reutiliza resultados já calculados. Isso permite encontrar a melhor combinação possível dentro do limite de tempo.

## Complexidade

Considerando:

- `n` como a quantidade de conteúdos;
- `T` como o tempo total disponível.

A complexidade do algoritmo Knapsack 0/1 implementado é:

```text
Tempo: O(n * T)
Espaço: O(n * T)
```

O espaço também é `O(n * T)` porque a matriz completa é mantida para permitir a reconstrução dos conteúdos escolhidos e a visualização da tabela de Programação Dinâmica.

## Observações Importantes

- O algoritmo não escolhe conteúdos de forma parcial.
- O tempo total dos conteúdos escolhidos nunca ultrapassa o tempo disponível.
- A solução ótima é reconstruída a partir da matriz de Programação Dinâmica.
- A matriz pode ser exibida para demonstrar o funcionamento interno do algoritmo.
- O projeto demonstra a aplicação prática de Programação Dinâmica em um cenário de planejamento de estudos.

## Justificativa do Algoritmo

O algoritmo Knapsack foi escolhido porque o problema possui uma estrutura compatível com decisões binárias: cada conteúdo deve ser estudado ou não estudado.

Como o estudante possui um limite de tempo antes da prova, é necessário selecionar a combinação de conteúdos que maximiza o retorno esperado sem ultrapassar esse limite. Essa situação é equivalente ao problema da mochila, em que itens possuem pesos e valores, e a mochila possui uma capacidade máxima.

A Programação Dinâmica é adequada porque evita recalcular os mesmos subproblemas várias vezes. Em vez de testar todas as combinações de forma bruta, o algoritmo armazena os melhores resultados intermediários em uma matriz e utiliza essas respostas para construir a solução final.

Esse comportamento torna o algoritmo eficiente, explicável e adequado para demonstrar o conteúdo da disciplina.

## Estrutura do Projeto

```text
G14_Programacao_Dinamica_PA-26.1
├── main.py
│   └── Programa principal contendo a lista pré-definida de conteúdos e a execução do algoritmo
│
├── src/
│   ├── subject.py
│   │   └── Classe responsável por representar um conteúdo de estudo
│   │
│   ├── priority.py
│   │   └── Cálculo da prioridade dos conteúdos
│   │
│   └── knapsack.py
│       └── Implementação do algoritmo Knapsack 0/1
│
└── tests/
    ├── test_priority.py
    │   └── Testes da fórmula de prioridade
    │
    └── test_knapsack.py
        └── Testes do algoritmo de Programação Dinâmica
```
