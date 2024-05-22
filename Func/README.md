# Desafios

## 1. Análise de Lista

Escreva um código que realiza as seguintes operações em uma lista de números:
- Leitura do tamanho da lista
- Identificação do maior e menor valor
- Cálculo da soma dos valores da lista
- Exibição de uma mensagem com os resultados

Mensagem de saída:
```
"A lista possui [tam] números em que o maior número é [maior] e o menor número é [menor]. A soma dos valores presentes nela é igual a [soma]"
```

## 2. Tabuada

Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, conforme a escolha da pessoa usuária. Por exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:
```
Tabuada do 7:
7 x 0 = 0
7 x 1 = 7
[...]
7 x 10 = 70
```

## 3. Múltiplos de 3

Crie uma função que leia uma lista e retorne uma nova lista com os múltiplos de 3. Utilize o `return` na função e salve a nova lista na variável `mult_3`.

## 4. Quadrados dos Números

Crie uma lista dos quadrados dos números de 1 a 10 utilizando as funções `lambda` e `map()` para calcular o quadrado de cada elemento da lista.

## 5. Pontuação dos Atletas

Escreva um código que calcula a pontuação de atletas baseado em 5 notas digitadas pelos jurados. Elimine a maior e a menor nota e calcule a média das 3 notas restantes. Retorne a média para exibir a mensagem:
```
"Nota da manobra: [media]"
```

## 6. Desempenho dos Estudantes

Crie uma função que receba uma lista de 4 notas e retorne:
- Maior nota
- Menor nota
- Média
- Situação (Aprovado(a) ou Reprovado(a))

Exiba os dados em uma mensagem:
```
"O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"
```

## 7. Nomes Completos

Trate duas listas com os nomes e sobrenomes de estudantes, concatenando-os para apresentar seus nomes completos na forma "Nome Sobrenome". As listas são:
```
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]
```

Exiba a mensagem para cada estudante:
```
"Nome completo: Nome Sobrenome"
```

## 8. Pontuação do Time de Futebol

Escreva uma função `calcula_pontos` que receba duas listas de números inteiros representando os gols marcados e sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual. Use as regras: vitória vale 3 pontos, empate vale 1 ponto, derrota 0 pontos. Exemplo de uso:
```
gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]
```

Mensagem de saída:
```
"A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%"
```

## 9. Cálculo de Gastos de Viagem

Crie três funções que calculam os gastos com hotel, gasolina e passeios para uma viagem de Recife para uma das quatro cidades: Salvador, Fortaleza, Natal e Aracaju. Considere:
- Custo da diária do hotel: 150 reais
- Consumo de gasolina: 14 km/l, custo de 5 reais por litro
- Gastos com passeios e alimentação por dia: Salvador (200), Fortaleza (400), Natal (250), Aracaju (300)
- Distâncias: Salvador (850 km), Fortaleza (800 km), Natal (300 km), Aracaju (550 km)

Simule uma viagem de 3 dias para Salvador.

Mensagem de saída:
```
"Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"
```

## 10. Filtragem de Palavras

Crie um código que recebe uma frase e filtra apenas as palavras com tamanho maior ou igual a 5 caracteres. Use `lambda` e `filter()` para a filtragem.

Mensagem de saída exibindo as palavras filtradas em uma lista.