# 4. Explore as colunas do DataFrame e analise os tipos dos dados presentes em cada coluna.

import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

data = pd.read_csv(url,sep=',')

# # Analisando os dados de cada linha, o que é o dados, esse é geralzão
print(data.info())
# # Específico
print(data['Nome']) # object ou str(String)
print(data['Idade']) # int64 ou int(Inteiro)
print(data['Notas']) # Float64 ou Float(Decimal)
print(data['Aprovado']) # Bool ou booleano(True or False)
