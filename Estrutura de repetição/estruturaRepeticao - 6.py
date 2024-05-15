# 5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse 
# número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.

fat = 1

fat1 = int(input('Diga seu fatorial: '))

aux = fat1

while aux != 0:
    fat += fat * (aux - 1)
    aux -= 1



print(fat)
    
    

