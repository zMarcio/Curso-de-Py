
# # 9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que 
# calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:
# Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
# Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
# Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. 
# Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.





cad1 = 0
cad2 = 0
cad3 = 0
cad4 = 0
nulo = 0
branco = 0

for i in range(0, 5):
    entradaVote = input('Diga quem você vai votar (1,2,3,4,5(NULO) e 6(BRANCO)): ')
    if entradaVote == '1':
        cad1 += 1
    if entradaVote == '2':
        cad2 += 1
    if entradaVote == '3':
        cad3 += 1
    if entradaVote == '4':
        cad4 += 1
    if entradaVote == '5':
        nulo += 1
    if entradaVote == '6':
        branco += 1


print(f'Candidato 1: {cad1}, Candidato 2: {cad2}, Candidato 3: {cad3}, Candidato 4: {cad4}, Votos nulo: {nulo}, Votos branco: {branco}, ')
maior = max(cad1,cad2,cad3,cad4)
if cad1 == cad2 == cad3 == cad4:
    print('DEU EMPATE!')
else:
    if maior == cad1:
        print(f'Candidato 1 venceu, com {maior} votos!')
    if maior == cad2:
        print(f'Candidato 2 venceu, com {maior} votos!')
    if maior == cad3:
        print(f'Candidato 3 venceu, com {maior} votos!')
    if maior == cad4:
        print(f'Candidato 4 venceu, com {maior} votos!')



