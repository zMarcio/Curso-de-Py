# Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:
lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

# Dois jeitos de fazer a mesma situação, um com list Comprehension(segundo caso) e um com for(primeiro caso)

sumLists = 0
for i in range(0,len(lista_de_listas)):
    sumLists += sum(lista_de_listas[i])


# sumLists = [sum(lista_de_listas[i]) for i in range(0,len(lista_de_listas))]
# sumLists = sum(sumLists)

print(sumLists)