lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')], [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]], [9.0, 7.3, 5.8, 6.7, 8.5], ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

# [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]

listDici = ['Name','Notas','Médias','Situação']

# dicAllInfos = {x:y for x,y in zip(listDici,lista_completa)}
dicAllInfos2 = {listDici[i]:lista_completa[i] for i in range(len(listDici))}


dicAllInfos2['Estudantes'] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]


# print(dicAllInfos)
print('-'*40)
print(dicAllInfos2)