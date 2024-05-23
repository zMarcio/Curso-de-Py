# A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], 
# crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
list_tupla = []


for i in range(0,len(lista)):
    list_tupla.append((i, lista[i]))


print(list_tupla)



