# 9. Criar um gráfico de barras horizontais que apresente os 5 bairros com as médias de valores de aluguel mais elevadas.

import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

data = pd.read_csv(url,sep=';')

testing = data.groupby('Bairro')[['Valor']].mean().sort_values('Valor', ascending=False).head(5)
testing.plot(kind='barh',figsize=(14,10),color='Purple')
plt.show()

print(testing)