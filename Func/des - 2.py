# Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. 
# Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

# Tabuada do 7:
# 7 x 0 = 0
# 7 x 1 = 7
# [...]
# 7 x 10 = 70

def tab(x:int) -> str:
    for i in range(1,11):
        print(f'{x} x {i} = {i*x}')

tab(7)