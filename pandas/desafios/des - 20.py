# Crie mais uma coluna, chamada "Notas_finais" que possua as notas de cada aluno somada com os pontos extras
import pandas as pd

uri = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

datas = pd.read_csv(uri,sep=',')

datas['Notas'] = datas['Notas'].fillna(0)

datas['Pontos_extras'] = datas['Notas'] * 0.4

datas['Notas_finais'] = datas['Notas'] + datas['Pontos_extras']

print(datas.head())