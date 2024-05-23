# Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:


# Dois jeitos de fazer a mesma situação, um com list Comprehension(segundo caso) e um com for(primeiro caso)


# 1
list_elemento = []
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
for i in range(0, len(lista_de_tuplas)):
    # print(lista_de_tuplas[i][2])
    list_elemento.append(lista_de_tuplas[i][2])


# 2
testing = [lista_de_tuplas[i][2] for i in range(0, len(lista_de_tuplas))]

# Print do primeiro
print(list_elemento)
# Print do segundo
print(testing)


