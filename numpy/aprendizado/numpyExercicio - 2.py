import numpy as np



clientes = np.array([[1, 'João', 30, 'Rua A', 100, 'eletrônicos'],
                     [2, 'Maria', 25, 'Rua B', 200, 'moda'],
                     [3, 'Pedro', 35, 'Rua C', 50, 'esportes']])


# Pode ser assim que ele pega do 4 para frente
intecao_compras = clientes[:,4:]
# Ou assim que ele pega até uma anterior da que botou na direita, ou seja vai até o 5
intecao_compras_exp = clientes[:,4:6]
print(intecao_compras)
print('-'*50)
print(intecao_compras_exp)
