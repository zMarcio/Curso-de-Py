# Verifique se a base de dados possui dados nulos e, caso tenha, realize o tratamento desses dados nulos da forma que achar mais coerente com a situação.
import pandas as pd

uri = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

datas = pd.read_csv(uri, sep=',')

data = datas['Notas'].fillna(0)

print(data)
print(data.isnull().sum())
