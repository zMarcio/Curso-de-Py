# Momento dos projetos
# 6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada 
# no seguinte formato:

# Tabuada do 2:
# 2 x 1 = 2
# 2 x 2 = 4
# [...]
# 2 x 10 = 20

i = 0

numTab = int(input('Digite um número que deseja saber a tabuada: '))

print(f'Tabuada do {numTab}')
while i != 11:
    print(f'{numTab} x {i} = {numTab*i}')
    i += 1