# Aplique um filtro que selecione apenas os alunos que foram aprovados.
import pandas as pd

uri = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

datas = pd.read_csv(uri,sep=',')

datas = datas.query('Aprovado == True')

print(datas)


