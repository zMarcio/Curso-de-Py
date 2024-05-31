import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/dados_sus.csv'

# # Configurando o arquivo para que o pandas consiga ler sem da erro
data = pd.read_csv(url,sep=';',encoding='ISO-8859-1',skiprows=3,skipfooter=9,engine='python')
print(data)