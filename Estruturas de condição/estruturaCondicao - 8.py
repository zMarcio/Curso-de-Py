num1 = int(input('Digite o preço do 1 numero: '))
num2 = int(input('Digite o preço do 2 numero: '))
num3 = int(input('Digite o preço do 3 numero: '))

if num3 >= num2 and num3 >= num1:
    if num2 >= num1:
        print(f'Decrescente: {num3} {num2} {num1}')
    else:
        print(f'Decrescente: {num3} {num1} {num2}')
elif num2 >= num3 and num2 >= num1:
    if num3 >= num1:
        print(f'Decrescente: {num2} {num3} {num1}')
    else:
        print(f'Decrescente: {num2} {num1} {num3}')
elif num1 >= num3 and num1 >= num2:
    if num3 >= num2:
        print(f'Decrescente: {num1} {num3} {num2}')
    else:
        print(f'Decrescente: {num1} {num2} {num3}')

