# Os alunos "Alice" e "Carlos", não fazem mais parte da turma. Sendo assim, remova-os da base de dados.
import pandas as pd

uri = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

datas = pd.read_csv(uri,sep=',')

print(datas)



data = datas.query('Nome == "Carlos" or Nome == "Alice"').index


print(datas.drop(data,axis=0))


