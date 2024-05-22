alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
pesos = [65, 80, 58, 70, 95]

imc = [round((peso / altura**2), 1) for altura, peso in zip(alturas, pesos)]
print(imc)

t1 = ['Aliança','Boné','Calça']
t2 = [1000,39.99,299.99]

test1 = { x : y for x,y in zip(t1,t2) }

print(test1)