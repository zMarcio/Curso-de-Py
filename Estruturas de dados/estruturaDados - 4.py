# 4. Invertendo a Ordem dos Números
# Agora, colete mais 5 números inteiros e imprima a lista em ordem inversa, 
# mostrando os números na ordem contrária àquela em que foram digitados.


listNum = [1, 2, 3, 4, 5]

# while len(listNum) != 5:
#     num = int(input('Digite seu numero: '))
#     listNum.append(num)
listNum.reverse()
print(f'numeros = {listNum}')