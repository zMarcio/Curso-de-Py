# Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

# [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

# Utilize o return na função e salve a nova lista na variável mult_3.

# Em lambda
list_nums = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

newList = list(map(lambda x: x * 3, list_nums))

print(newList)

# def, ou em função
def newLst(x:list) -> list:
    list_Return = []
    for i in x:
        list_Return.append(i*3)
    return list_Return

mult_3 = newLst(list_nums)

print(mult_3)