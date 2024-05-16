ano22 = int(input('Vendas 22: '))
ano23 = int(input('Vendas 23: '))

result = -1 * (ano22 - (ano23*100)/ano22)

# print(result)

if result > 20:
    print('bonificação para o time de vendas.')
elif result <= 20 and result >= 2:
    print('pequena bonificação para time de vendas.')
elif result >= -10 and result < 2:
    print('planejamento de políticas de incentivo às vendas.')
else:
    print('corte de gastos.')