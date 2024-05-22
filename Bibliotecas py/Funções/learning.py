""" 
    1. Defina uma função chamada estatisticas que aceite 
    um número variável de argumentos numéricos.
    
    2. A função deve retornar a média, o maior e o menor número do conjunto.
    
    3. Peça ao usuário para inserir uma sequência de números, separados por espaços.
    
    4. Converta essa entrada do usuário em uma lista de números.
    
    5. Use a função estatisticas para calcular a média, o maior e o menor número da lista.
    
    6. Mostre ao usuário a média, o maior e o menor número.
"""

def estatisticas(*args):
    media = sum(args)/len(args)
    maior = max(args)
    menor = min(args)
    return media,maior,menor

digi_qtd = int(input('Diga quantos numeros você quer somar: '))
i = 0
list_nums = []

while i != digi_qtd:
    digit_num = int(input('Digite seus numeros: '))
    list_nums.append(digi_qtd)
    i+=1

# print(estatisticas(*list_nums))
print(f'A média {estatisticas(*list_nums)[0]}, o maior {estatisticas(*list_nums)[1]} e o menor {estatisticas(*list_nums)[2]}')