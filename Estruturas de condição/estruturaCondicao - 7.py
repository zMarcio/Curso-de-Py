prod1 = float(input('Digite o preço do 1 produto: '))
prod2 = float(input('Digite o preço do 2 produto: '))
prod3 = float(input('Digite o preço do 3 produto: '))

if prod1 < prod2 and prod1 < prod3:
    print(f"Produto mais barato {prod1}")
elif prod2 < prod1 and prod2 < prod3:
    print(f"Produto mais barato {prod2}")   
elif prod3 < prod2 and prod3 < prod1:
    print(f"Produto mais barato {prod3}")
