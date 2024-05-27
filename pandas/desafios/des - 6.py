# 6. Calcular a média de quartos por apartamento;

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

data = pd.read_csv(url,sep=';')


# print(data)


print(data['Quartos'].mean())