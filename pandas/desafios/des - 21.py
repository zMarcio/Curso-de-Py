# Como houve uma pontuação extra, alguns alunos que não tinham sido aprovados antes podem ter sido aprovados agora. Com base nisso, crie uma coluna chamada "Aprovado_final" com os seguintes valores:

# True: caso o aluno esteja aprovado (nota final deve ser maior ou igual a 6);
# False: caso o aluno esteja reprovado (nota final deve ser menor que 6).
import pandas as pd

uri = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

datas = pd.read_csv(uri,sep=',')


datas['Notas'] = datas['Notas'].fillna(0)

print(datas.loc[datas['Aprovado'] == False].head())

datas['Pontos_extras'] = datas['Notas'] * 0.4

datas['Notas_finais'] = datas['Notas'] + datas['Pontos_extras']

condicao = datas['Notas_finais'] >=  6.0 

datas.loc[datas['Notas_finais'] >=  6.0, 'Aprovado'] = True

print(datas.head())