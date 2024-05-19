# 3. Colecionando Números Inteiros
# Crie um código que colete 5 números inteiros do usuário
# e os armazene em uma lista. Exiba a lista no final da coleta. numeros = [1, 4, 7, 2, 4]


listNum = []

while len(listNum) != 5:
    num = int(input('Digite seu numero: '))
    listNum.append(num)
print(f'numeros = {listNum}')