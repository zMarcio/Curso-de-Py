num1 = float(input('Digite um numero: '))
num2 = float(input('Digite um segundo numero: '))

op = input('Digite qual operação você deseja fazer(+, -, *, /): ').strip()


if '+' in op:
    op2 = num1 + num2
    if op2 < 0 and op2 % 1 == 0 and op2 % 2 == 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é par, inteiro e negativo')
    elif op2 < 0 and op2 % 1 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, decimal e negativo')
    elif op2 < 0 and op2 % 1 == 0 and op2 % 2 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, inteiro e negativo')
    elif op2 > 0 and op2 % 1 == 0 and op2 % 2 == 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é par, inteiro e positivo')
    elif op2 > 0 and op2 % 1 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, decimal e positivo')
    elif op2 > 0 and op2 % 1 == 0 and op2 % 2 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, inteiro e positivo')

if '-' in op:
    op2 = num1 - num2
    if op2 < 0 and op2 % 1 == 0 and op2 % 2 == 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é par, inteiro e negativo')
    elif op2 < 0 and op2 % 1 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, decimal e negativo')
    elif op2 < 0 and op2 % 1 == 0 and op2 % 2 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, inteiro e negativo')
    elif op2 > 0 and op2 % 1 == 0 and op2 % 2 == 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é par, inteiro e positivo')
    elif op2 > 0 and op2 % 1 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, decimal e positivo')
    elif op2 > 0 and op2 % 1 == 0 and op2 % 2 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, inteiro e positivo')

if '*' in op:
    op2 = num1 * num2
    if op2 < 0 and op2 % 1 == 0 and op2 % 2 == 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é par, inteiro e negativo')
    elif op2 < 0 and op2 % 1 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, decimal e negativo')
    elif op2 < 0 and op2 % 1 == 0 and op2 % 2 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, inteiro e negativo')
    elif op2 > 0 and op2 % 1 == 0 and op2 % 2 == 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é par, inteiro e positivo')
    elif op2 > 0 and op2 % 1 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, decimal e positivo')
    elif op2 > 0 and op2 % 1 == 0 and op2 % 2 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, inteiro e positivo')

if '/' in op:
    if num1 == 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: 0')
    if num2 == 0:
        print('Denominador é 0, impossivel a solução')
        exit()
    op2 = num1 / num2
    if op2 < 0 and op2 % 1 == 0 and op2 % 2 == 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é par, inteiro e negativo')
    elif op2 < 0 and op2 % 1 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, decimal e negativo')
    elif op2 < 0 and op2 % 1 == 0 and op2 % 2 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, inteiro e negativo')
    elif op2 > 0 and op2 % 1 == 0 and op2 % 2 == 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é par, inteiro e positivo')
    elif op2 > 0 and op2 % 1 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, decimal e positivo')
    elif op2 > 0 and op2 % 1 == 0 and op2 % 2 != 0:
        print(f'Operação escolhida: {op}, numeros: {num1} e {num2}, Resultado: {op2}, então ele é impar, inteiro e positivo')
