#  11. Analisando as Vendas do E-commerce
# Uma empresa de e-commerce deseja analisar as vendas dos seus produtos. 
# Os dados de vendas foram armazenados em um dicionário. 
# Escreva um código que calcule o total de vendas e identifique o produto mais vendido.
# python
vendas = {
    'Produto A': 300,
    'Produto B': 80,
    'Produto C': 60,
    'Produto D': 200,
    'Produto E': 250,
    'Produto F': 30
}
total_vendas = 0
p = 0
d = ''
for prod,qtd_vendas in vendas.items():
    total_vendas += qtd_vendas
    if qtd_vendas > p:
        d = prod
        p = qtd_vendas

print(f'total de vendas {total_vendas}, produto mais vendido: {d} e com a quantidade de vendas: {p}')
    
    