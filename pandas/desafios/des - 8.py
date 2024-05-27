# 8. Analisar quais bairros possuem a média de valor de aluguel mais elevadas;

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

data = pd.read_csv(url,sep=';')


print(data.groupby('Bairro')[['Valor']].mean().sort_values('Valor', ascending=False))