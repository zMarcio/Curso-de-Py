# 5 - Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

from math import pow as pw

dig_Num1 = int(input('Digite um numero: '))
dig_Num2 = int(input('Digite um segundo numero: '))


print(f'{dig_Num1} elevado a {dig_Num2}: {pw(dig_Num1,dig_Num2)}')
