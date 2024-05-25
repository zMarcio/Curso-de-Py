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


# # Cidades do documento
# # Aqui seria os dados por cidade
Moscow = precos[:,0]
Kaliningrad = precos[:,1]
# Peterburg = precos[:,2]
# Krasnodar = precos[:,3]
# Ekaterinbug = precos[:,4]

# # Precos por anos e por cidade
# Moscow_ano1 = Moscow[0:12] 
# Moscow_ano2 = Moscow[12:24]
# Moscow_ano3 = Moscow[24:36]
# Moscow_ano4 = Moscow[36:48]

# # Dados dos anos:
data_ano = np.arange(1,13,1)

# Junta todos os dados para verificar junto, comparando um com outro no gráfico
# plt.plot(data_ano,Moscow_ano1)
# plt.plot(data_ano,Moscow_ano2)
# plt.plot(data_ano,Moscow_ano3)
# plt.plot(data_ano,Moscow_ano4)
# Uma legenda dizendo o que representa cada linha
# plt.legend(['ano - 1', 'ano - 2', 'ano - 3', 'ano - 4'])
# Aqui mostra o gráfico
# plt.show()

# Verifica se os arrays são iguais
# print(np.array_equal(Moscow_ano3,Moscow_ano4))

# # Verifica se tem valores proximos, ou diferença grande de um para outro
# print(np.allclose(Moscow_ano3,Moscow_ano4,10))

# # Mostra o grafico de kali com os meses, nele há um dado NAN, ou seja aconteceu algum erro
# plt.plot(datas,Kaliningrad)
# plt.show()


# Aqui nessa linha ele vai verificar se tem algum numero NAN, se tiver vai retornar True e o que não tiver False
# print(np.isnan(Kaliningrad))

# Aqui ele vai somar esse valores True, já que ele representa 1 em binário e vai retorna a quantidade de True que tem, ou seja de NAN`S
# print(sum(np.isnan(Kaliningrad)))


# Dois jeitos de se tirar um media
# print((Kaliningrad[3] + Kaliningrad[5])/2)
Kaliningrad[4] = np.mean([Kaliningrad[3],Kaliningrad[5]])

# plt.plot(datas,Kaliningrad)
# plt.show()


# Pega a média de Moscow
# result1 = np.mean([Moscow])
# Pega a média de Kaliningrad
# result2 = np.mean([Kaliningrad])

# print(round(result1,2))
# print(round(result2,2))


plt.plot(datas,Moscow)

x = datas

# Isso seria uma suposição
# y = 2*x+80

# Podemos tentar calcula um reta que se assemelha com o gráfico utilizando esse calculo
# np.sqrt(np.sum(np.power(Moscow-y,2)))


y = 0.52*x+80


# np.linalg.norm(Moscow-y)

# Montando a formula do coeficiente  angular
Y = Moscow
X = datas
n = np.size(Moscow)

# Coeficiente angular
a = (n * np.sum(X*Y) - np.sum(X) * np.sum(Y))/(n*np.sum(X**2) - np.sum(X)**2)
# Coeficiente linear
b = np.mean(Y) - a*np.mean(X)


y = a*X+b

print(np.linalg.norm(Moscow - y))
plt.plot(X,y)
plt.plot(100,100*a+b,'*r')
plt.show()

