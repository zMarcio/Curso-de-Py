lado1 = int(input('Digite o primeiro lado: '))
lado2 = int(input('Digite o segundo lado: '))
lado3 = int(input('Digeite o terceiro lado: '))

sumlds = lado1 + lado2

if lado3 < sumlds:
    if lado1 == lado2 == lado3:
        print('Equilatero')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Triangulo inválido')
