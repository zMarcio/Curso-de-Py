# Faça uma seleção e verifique quais alunos não tinham sido aprovados anteriormente, mas foram aprovados após a soma dos pontos extras.
import pandas as pd

uri = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

datas = pd.read_csv(uri,sep=',')


datas['Notas'] = datas['Notas'].fillna(0)

# print(datas.loc[datas['Aprovado'] == False].head())

datas['Pontos_extras'] = datas['Notas'] * 0.4

datas['Notas_finais'] = datas['Notas'] + datas['Pontos_extras']

datas['Aprovado_finais'] = False

datas['Aprovado_finais'] = datas['Notas_finais'].apply(lambda x: True if x >= 6.0 else False)

print(datas.query('Aprovado_Finais == True & Aprovado == false').head())
