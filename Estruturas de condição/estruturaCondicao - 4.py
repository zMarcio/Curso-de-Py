
ano1 = float(input('Digite o preço do ano 1: '))
ano2 = float(input('Digite o preço do ano 2: '))
ano3 = float(input('Digite o preço do ano 3: '))

if ano1 > ano2 and ano1 > ano3:
    print(f"carro mais caro {ano1}")
elif ano2 > ano1 and ano2 > ano3:
    print(f"carro mais caro {ano2}")
elif ano3 > ano2 and ano3 > ano1:
    print(f"carro mais caro {ano3}")
elif ano1 < ano2 and ano1 < ano3:
    print(f"carro mais barato {ano1}")
elif ano2 < ano1 and ano2 < ano3:
    print(f"carro mais barato {ano2}")   
elif ano3 < ano2 and ano3 < ano1:
    print(f"carro mais barato {ano3}")
else:
    print(f'Não houve alteração do valor, aqui eles ano 1: {ano1}, ano 2: {ano2} e ano 3: {ano3}')
