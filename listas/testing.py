notas_turma = ['João', 8.0, 9.0, 10.0, 'Maria', 9.0, 7.0, 6.0, 'José', 3.4, 7.0, 7.0, 'Cláudia', 5.5, 6.6, 8.0, 'Ana', 6.0, 10.0, 9.5]

# alunos = []
# notas = []
# for i in notas_turma:
#     if type(i) == str:
#         alunos.append(i)
#     else:
#         notas.append(i)


# print(f'Alunos: {alunos}')
# print(f'Notas: {notas}')
listCreation = []
# print([(type(item) == str) == true listCreation.append(item)  for item in notas_turma])
[listCreation.append(item) for item in notas_turma if type(item) == str]

# print(listCreation)


nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

nome = [i[0] for i in nomes]

nome = list(zip(nome,medias))
print(nome)

# nome = [i[0] for i in nome if i[1] >= 8]
nome = ['Aprovado(a)' if i[1] >= 6 else 'Reprovado(a)' for i in nome]
print(nome)

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]


allInfos = [x for x in [nomes,notas,medias,nome]]
print(allInfos)
