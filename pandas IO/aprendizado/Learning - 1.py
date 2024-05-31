import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/superstore_data.csv'

data = pd.read_csv(url, sep=',')

data.head()

data_5row = pd.read_csv(url,nrows=5)
print(data_5row)

data_selecao_col = pd.read_csv(url,usecols=['Id','Year_Birth','Income'])
print(data_selecao_col)

data_selecao_col_num = pd.read_csv(url,usecols=[0,1,4])
print(data_selecao_col_num)