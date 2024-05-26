import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

data = pd.read_csv(url,sep=',')

# O método describe() é uma das funções mais úteis do Pandas para a análise exploratória de dados. Essa função é usada para calcular algumas estatísticas descritivas básicas dos dados em um DataFrame ou em uma coluna específica de um DataFrame.
print(data['Notas'].describe())
print(data['Notas'].describe().mean())
print(data['Notas'].describe().max())
print(data['Notas'].describe().min())
print(data['Notas'].describe().median())
