# Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. 
# Deixe claro que o valor do denominador não pode ser 0.

num1 = float(input('Digite um numero(Numerador): '))
num2 = float(input('Digite um segundo numero(Denominador, ele não pode ser zero): '))


while num2 == 0:
    print('Denominador preciso ser diferente de 0')
    num2 = float(input('Digite um segundo numero(Denominador, ele não pode ser zero): '))

print(f'{num1} / {num2} = {num1/num2}')