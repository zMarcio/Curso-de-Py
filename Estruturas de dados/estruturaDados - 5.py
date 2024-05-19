# 5. Desvendando os Números Primos
# Desenvolva um programa que, ao receber um número qualquer do usuário, 
# gere uma lista contendo todos os números primos entre 1 e o número digitado.

list_numPrimo = []
digNum = int(input('Digite um numero'))

def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2,int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True



for i in range(2,digNum+1):
    if eh_primo(i):
        list_numPrimo.append(i)

print(list_numPrimo)

