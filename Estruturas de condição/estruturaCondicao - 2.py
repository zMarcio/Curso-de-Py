num1 = 15/100
num2 = float(input("digite o seu percentual: "))/100

if num1 > num2:
    print('Houve um decrescimento')
elif num2 > num1:
    print('Houve um crescimento')
else:
    print('Não houve crescimento ou decrescimento')
