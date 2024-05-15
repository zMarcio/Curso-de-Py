def objAluno(nomeAluno,note1,note2,result,aprovadoOrRecuperacao):
    infoAluno = {
        'nome': nomeAluno,
        'nota 1': note1,
        'nota 2': note2,
        'media': result,
        'resultado': aprovadoOrRecuperacao
    }
    return infoAluno

listTotalNotasAlunos = []
aprovados = []
recuperacao = []

while len(listTotalNotasAlunos) != 1:
    nomeAluno = input('Digite o nome do aluno ')
    note1 = float(input('Digite a primeira nota: '))
    note2 = float(input('Digite a segunda nota: '))
    aprovaOrN = True
    result = (note1+note2)/2
    if result < 6:
        aprovaOrN = False
        recuperacao.append(objAluno(nomeAluno,note1,note2,result,aprovaOrN))
        listTotalNotasAlunos.append(objAluno(nomeAluno,note1,note2,result,aprovaOrN))
    else:
        aprovados.append(objAluno(nomeAluno,note1,note2,result,aprovaOrN))
        listTotalNotasAlunos.append(objAluno(nomeAluno,note1,note2,result,aprovaOrN))

if len(aprovados) != 0:
    print('Aprovados:')
    for i in range(len(aprovados)):
    
        print(aprovados[i]['nome'])
    
print('-'*15)
if len(recuperacao) != 0:
    print('Recuperação:')
    for i in range(len(recuperacao)):
        print(recuperacao[i]['nome'])
else:
    print('Não há reprovados!')

print('-'*15)
print(f'Alunos: \n {listTotalNotasAlunos}')

