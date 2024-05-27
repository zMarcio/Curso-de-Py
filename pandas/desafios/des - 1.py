# 1. Importe o arquivo `alunos.csv` e armazene seu conteúdo em um DataFrame Pandas.

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

data = pd.read_csv(url,sep=',')

print(data)