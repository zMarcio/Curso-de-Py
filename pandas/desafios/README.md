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

10. Claro, aqui está o texto com o desafio, sem a resposta:

---

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
