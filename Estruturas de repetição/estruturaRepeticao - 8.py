# # 8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de 
# uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.


entrada = int(input('Diga sua idade: '))

idade_0_25 = 0
idade_26_50 = 0
idade_51_75 = 0
idade_76_100 = 0

while entrada >=:
    if entrada > 0 and entrada < 25:
        idade_0_25 += 1 
    if entrada > 26 and entrada < 50:
        idade_26_50 += 1
    if entrada > 51 and entrada < 75:
        idade_51_75 += 1
    if entrada > 76 and entrada < 100:
        idade_76_100 += 1

print(f'pessoa entre [0,25]:  {idade_0_25}')
print(f'pessoa entre [26,50]:  {idade_26_50}')
print(f'pessoa entre [51,75]:  {idade_51_75}')
print(f'pessoa entre [76,100]:  {idade_76_100}')