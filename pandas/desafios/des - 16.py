# Salve o DataFrame que possui apenas os alunos aprovados em um arquivo csv chamado "alunos_aprovados.csv".
import pandas as pd

uri = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

datas = pd.read_csv(uri,sep=',')

datas = pd.read_csv(uri,sep=',')

datas = datas.query('Aprovado == True')

datas.to_csv('alunos_aprovados.csv',index=False,sep=',')