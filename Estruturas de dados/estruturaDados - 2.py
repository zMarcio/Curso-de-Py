# 2. Investigando Compras acima de 3000 Reais
# Utilizando os mesmos dados da questão anterior, 
# descubra quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem dessas compras em relação ao total de compras.

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

totalCompras = 0
for i in gastos:
    if i >= 3000:
        totalCompras+=1

print(totalCompras)