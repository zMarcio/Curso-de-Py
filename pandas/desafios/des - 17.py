# Ao conferir as notas dos alunos aprovados, notamos que algumas notas estavam incorretas. As alunas que tiraram nota 7.0, na verdade, tinham um ponto extra que não foi contabilizado. Sendo assim, substitua as notas 7.0 da base de dados por 8.0. Dica: pesquise pelo método replace.
import pandas as pd

uri = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

datas = pd.read_csv(uri,sep=',')

datas = pd.read_csv(uri,sep=',')

datas = datas.query('Notas == 7.0').replace(7.0,8.0)

print(datas)

# datas.to_csv('alunos_aprovados.csv',index=False,sep=',')