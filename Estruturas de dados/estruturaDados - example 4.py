"""

Dicionários em python funciona assim:
índice = chave
chave = valor


chave é como se fosse um indice capaz de acessar um valor.
"""

# Criando um dicionário agora

# dic = { 'chave':'valor','chave2':'valor2','chave3':'valor3','chave4':'valor4'}

# print(dic.keys())

# if 'chave' in dic.keys():
#     print('Tem um chave aqui')


# for i in dic.items():
#     print(i)

chave = ""
valor = ""
dici = {'oi':'olá',
        'precos': [2000, 1500, 3500, 4000, 1500]
        }

print(dici)

# dici.pop('oi')

# print(dici)


print(dici.items())
print(dici.keys())
print(dici.values())

# def setDici(chave,valor):
#     dici[chave] = valor

# def popDici(chave,valor):
#     dici.pop(chave,valor)


# while len(dici) != 3:    
#     chave = input('chave interativa, digite algo: ')
#     valor = input('valor interativo, digite um valor: ')
#     popDici(chave,valor)

#     print(dici)


for i,p in dici.items():
    print(f'Chave: {i} e Value: {p}')
    for d in p:
        print(f'data for list {d}')

