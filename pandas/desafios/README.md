# Desafios de Data Science

## Desafios

1. Importe o arquivo `alunos.csv` e armazene seu conteúdo em um DataFrame Pandas.

2. Visualize as primeiras 7 linhas do DataFrame e as 5 últimas.

3. Confira a quantidade de linhas e colunas desse DataFrame.

4. Explore as colunas do DataFrame e analise os tipos dos dados presentes em cada coluna.

### Extra

5. Calcule algumas estatísticas descritivas básicas dos dados do DataFrame (média, desvio padrão, etc). Dica: pesquise pelo método `describe`.

6. Calcular a média de quartos por apartamento;

7. Conferir quantos bairros únicos existem na nossa base de dados;

8. Analisar quais bairros possuem a média de valor de aluguel mais elevadas;

9. Criar um gráfico de barras horizontais que apresente os 5 bairros com as médias de valores de aluguel mais elevadas.

10.
## Desafio: Remover Linhas com o Método `drop()` da Biblioteca Pandas

Suponha que temos o seguinte DataFrame, salvo em uma variável chamada `dados`:

### Código para criação do DataFrame:

```python
import pandas as pd

dados = pd.DataFrame([['Feira', 'Cebola', 2.5],
                      ['Mercado', 'Cebola', 1.99],
                      ['Supermercado', 'Cebola', 1.69],
                      ['Feira', 'Tomate', 4],
                      ['Mercado', 'Tomate', 3.29],
                      ['Supermercado', 'Tomate', 2.99],
                      ['Feira', 'Batata', 4.2],
                      ['Mercado', 'Batata', 3.99],
                      ['Supermercado', 'Batata', 3.69]],
                     columns = ['Local', 'Produto', 'Preço'])
```

### DataFrame Resultante:

| Local        | Produto | Preço |
| ------------ | ------- | ----- |
| Feira        | Cebola  | 2.5   |
| Mercado      | Cebola  | 1.99  |
| Supermercado | Cebola  | 1.69  |
| Feira        | Tomate  | 4     |
| Mercado      | Tomate  | 3.29  |
| Supermercado | Tomate  | 2.99  |
| Feira        | Batata  | 4.2   |
| Mercado      | Batata  | 3.99  |
| Supermercado | Batata  | 3.69  |

### Desafio:

Qual dos códigos abaixo poderia ser utilizado para remover de forma permanente as linhas onde, na coluna "Local", temos "Supermercado"?

11 e 12. Durante o desenvolvimento do nosso projeto, nós aplicamos alguns filtros na nossa base de dados e salvamos os DataFrames resultantes em diferentes variáveis, sendo elas: df_1 e df_2.

13. Verifique se a base de dados possui dados nulos e, caso tenha, realize o tratamento desses dados nulos da forma que achar mais coerente com a situação.

14. Os alunos "Alice" e "Carlos", não fazem mais parte da turma. Sendo assim, remova-os da base de dados.

15. Aplique um filtro que selecione apenas os alunos que foram aprovados.

16. Salve o DataFrame que possui apenas os alunos aprovados em um arquivo csv chamado "alunos_aprovados.csv".

17. Ao conferir as notas dos alunos aprovados, notamos que algumas notas estavam incorretas. As alunas que tiraram nota 7.0, na verdade, tinham um ponto extra que não foi contabilizado. Sendo assim, substitua as notas 7.0 da base de dados por 8.0. Dica: pesquise pelo método replace.

18.
# Exemplo de DataFrame de Carros

Suponha que temos o seguinte DataFrame, com informações referentes a alguns carros em venda:

## Criação do DataFrame

Utilize o seguinte código para criar o DataFrame:

```python
import pandas as pd

dados = {
    'Nome': ['Jetta', 'Passat', 'Crossfox', 'DS5', 'Fusca'],
    'Motor': ['Motor 4.0 Turbo', 'Motor Diesel', 'Motor Diesel V8', 'Motor 2.0', 'Motor 1.6'],
    'Ano': [2019, 2003, 1991, 2019, 1990],
    'Quilometragem': [0.0, 5712.0, 37123.0, 0.0, 120000.0],
    'Valor': [88000.0, 106000.0, 72000.0, 89000.0, 32000.0],
    'IPVA': [2000.0, 5000.0, 1700.0, 2200.0, 1000.0],
    'Desconto': [380.0, 450.0, 277.0, 400.0, 150.0]
}

df = pd.DataFrame(dados)
```

## DataFrame

O DataFrame resultante é:

| Nome     | Motor           | Ano  | Quilometragem | Valor  | IPVA | Desconto |
| -------- | --------------- | ---- | ------------- | ------ | ---- | -------- |
| Jetta    | Motor 4.0 Turbo | 2019 | 0.0           | 88000  | 2000 | 380      |
| Passat   | Motor Diesel    | 2003 | 5712.0        | 106000 | 5000 | 450      |
| Crossfox | Motor Diesel V8 | 1991 | 37123.0       | 72000  | 1700 | 277      |
| DS5      | Motor 2.0       | 2019 | 0.0           | 89000  | 2200 | 400      |
| Fusca    | Motor 1.6       | 1990 | 120000.0      | 32000  | 1000 | 150      |

## Criação da Coluna "Valor_total"

Precisamos criar uma coluna chamada `Valor_total` que possui o valor do carro, somado com o IPVA e subtraídos os valores de desconto. O código correto para a criação dessa coluna é:

```python
df['Valor_total'] = df['Valor'] + df['IPVA'] - df['Desconto']
```

Após a execução deste código, o DataFrame será atualizado com a nova coluna `Valor_total`.
