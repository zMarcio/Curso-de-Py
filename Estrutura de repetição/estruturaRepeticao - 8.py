# # 8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de 
# uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.


entrada = int(input('Diga sua idade: '))

if entrada > 0 and entrada < 25:
    print(f'Idade: {entrada} [0-25]')
if entrada > 26 and entrada < 50:
    print(f'Idade: {entrada} [26-50]')
if entrada > 51 and entrada < 75:
    print(f'Idade: {entrada} [51-75]')
if entrada > 76 and entrada < 100:
    print(f'Idade: {entrada} [76-100]')
else:
    print('Fora do escopo!')