# 7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele 
# que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.



digaNum = int(input('Diga seu número: '))

listNums = [1,2,3,4,5,6,7,8,9,10,digaNum]
listNumsDiv = []
for i in listNums:
    if digaNum % i == 0 :
        listNumsDiv.append(i)

    

print(len(listNumsDiv))

if len(listNumsDiv) > 2:
    print('Número não é primo')
else:
    print('É primo')
    

# listNumsDiv.append(12)
# print(len(listNumsDiv))
