# 7. Conferir quantos bairros únicos existem na nossa base de dados;

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

data = pd.read_csv(url,sep=';')


print(len(data['Bairro'].unique()))