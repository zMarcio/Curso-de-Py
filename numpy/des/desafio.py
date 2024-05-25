import numpy as np
import matplotlib.pyplot as plt
url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'
data = np.loadtxt(url, delimiter=',',usecols=np.arange(1,6,1),skiprows=1)

# # print(data)
# # print('-'*50)
# # print(data.shape)
# # print('-'*50)
# # print(data.ndim)
# # print('-'*50)
# # print(data.T)
# # infos = data.T

laranja_diamentro = data[:5000,0]
torange_diamentro = data[5000:,0]
laranja_peso = data[:5000,1]
toranje_peso = data[5000:,1]


# print('Aqui é o Diametro:')
# print(laranja_diamentro)
# print('-'*30)
# print(torange_diamentro)
# print('-'*30)
# print('Aqui é o peso:')
# print(laranja_peso)
# print('-'*30)
# print(toranje_peso)

plt.plot(laranja_diamentro,laranja_peso)
# plt.plot(torange_diamentro,toranje_peso)
# plt.show()

# Laranja 
# Y = laranja_peso
# X = laranja_diamentro
# n = np.size(laranja_peso)


# Toranje
# Y2 = toranje_peso
# X2 = torange_diamentro 
# n2 = np.size(toranje_peso)

# a = (n * np.sum(X*Y) - np.sum(X) * np.sum(Y))/(n*np.sum(X**2) - np.sum(X)**2)

# a1 = (n2 * np.sum(X2*Y2) - np.sum(X2) * np.sum(Y2))/(n2*np.sum(X2**2) - np.sum(X2)**2)

# b = np.mean(Y) - a*np.mean(X)

# b1 = np.mean(Y2) - a1*np.mean(X2)


# y = a*X+b
# y1 = a1*X2+b1

# # plt.plot(X,y)
# plt.plot(X2,y1)
# plt.show()


Y = laranja_peso
X = laranja_diamentro
n = np.size(X)

a = (n*np.sum(X*Y) - np.sum(X)*np.sum(Y))/(n*np.sum(X**2)-np.sum(X)**2)
b = np.mean(Y) - a*np.mean(X)

y = a*X+b

plt.plot(X,y)
plt.show()


