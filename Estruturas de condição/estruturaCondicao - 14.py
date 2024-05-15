# Etanol até 15L desconto igual a 2%, acima 4% (valor 1.7R$)
# Diesel até 15L desconto igual a 3%, acima 5% (valor 2R$)

qCombustivel = input('Digite o tipo de combustivel: ').lower()
qtdLitro = float(input('Digite os litros comprados: '))

dicE = ['e', 'etanol']
dicD = ['d', 'diesel']

if qCombustivel in dicE:
    if qtdLitro <= 15:
        qtdLitro = qtdLitro * 1.7 - ((qtdLitro * 1.7) * 0.02)
        print(qtdLitro)
    else:
        qtdLitro = qtdLitro * 1.7 - ((qtdLitro * 1.7) * 0.04)
        print(qtdLitro)
elif qCombustivel in dicD:
    if qtdLitro <= 15:
        qtdLitro = qtdLitro * 2 - ((qtdLitro * 2) * 0.03)
        print(qtdLitro)
    else:
        qtdLitro = qtdLitro * 2 - ((qtdLitro * 2) * 0.05)
        print(qtdLitro)
else:
    print('Operações inválidas.')
