import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

data = pd.read_csv(url,sep=',')

# # Conferindo a quantidade de linhas e colunas
print(data.shape)