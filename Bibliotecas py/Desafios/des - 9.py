# 9 - Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, identificando quais resultaram em um número inteiro. 
# A lista é a seguinte:
from math import sqrt as ra
numeros = [2, 8, 15, 23, 91, 112, 256]

# testing = str(ra(256))
# testing = testing.split('.')
# print(testing)

print(8.5 // 1 == 8.5)
# Há duas formas de se fazer esse problema, colocando a raíz para string e separa com split, pelo ponto, e se for zero a raíz é inteira.
# e a outra é com //, pegando a raíz gerada e fazendo a comparação com o msm numero
for i in numeros:
    testing = ra(i)
    # testing = str(ra(i))
    # testing = testing.split('.')
    # if testing[1] == '0':
    if testing // 1 == testing:
        print(f'O número {i} é inteiro e aqui sua raíz {testing}')
        # print(f'O número {i} é inteiro e aqui sua raíz {testing[0]}')
    else:
        print('Não é inteiro')