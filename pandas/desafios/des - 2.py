import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

data = pd.read_csv(url,sep=',')

print(data)

# # 7 primeiros
print(data.head(7))
# # 5 últimas
print(data.head(5))