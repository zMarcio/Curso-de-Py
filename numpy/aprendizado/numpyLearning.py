import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/numpy/dados/apples_ts.csv'

data = np.loadtxt(url, delimiter=',', usecols=np.arange(1, 88, 1))

# print(data) # Todos os dados
# print('-'*10)
# print(data.ndim) # Diz as dimensões de um array.
# print('-'*10)
# print(data.size) # Diz o tamanho em elementos de um array.
# print('-'*10)
# print(data.shape) # Diz quantas linha e colunas tem em um array, respectivamente.
# print('-'*10)
# print(data.T) # Organiza esse array, fazendo a transposição do array, separando em linha e coluna.

dado_transposto = data.T # Organiza esse array, fazendo a transposição do array, separando em linha e coluna.

datas = dado_transposto[:,0] # pega a primeira linha, que seria a das datas, lembrando que pega a linha com todas as colunas

datas = np.arange(1,88)
# Esse preços é do geral, ou seja. todas cidades do grafico
precos = dado_transposto[:,1:6] # Pega rows que desejamos, no caso 6 linhas, lembrando que pega a linha com todas as colunas

# plt.plot(datas,precos[:,0]) # Monta o grafico, lembrando que primeiro eixo X e depois eixo Y
# plt.show() # Cria o gráfico


# Aqui seria os dados por cidade
Moscow = precos[:,0]

# Precos por anos e por cidade
Moscow_ano1 = Moscow[0:12] 
Moscow_ano2 = Moscow[12:24]
Moscow_ano3 = Moscow[24:36]
Moscow_ano4 = Moscow[36:48]

# Dados dos anos:
data_ano = np.arange(1,13,1)

plt.plot(data_ano,Moscow_ano1)
plt.plot(data_ano,Moscow_ano2)
plt.plot(data_ano,Moscow_ano3)
plt.plot(data_ano,Moscow_ano4)
plt.show()

# Kaliningrad = precos[:,1]
# Peterburg = precos[:,2]
# Krasnodar = precos[:,3]
# Ekaterinbug = precos[:,4]

# # Visualização dos dados por gráfico
# plt.plot(datas,Moscow)
# plt.show()
# plt.plot(datas,Kaliningrad)
# kali = plt.show()
# plt.plot(datas,Peterburg)
# pete = plt.show()
# plt.plot(datas,Krasnodar)
# kras = plt.show()
# plt.plot(datas,Ekaterinbug)
# eka = plt.show()

