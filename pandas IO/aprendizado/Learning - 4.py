import pandas as pd

url_1 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/pacientes.json'

url_2 = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/pacientes_2.json'

dados_pacientes = pd.read_json(url_1)

print(dados_pacientes.head())

dados_pacientes2 = pd.read_json(url_2)

print(dados_pacientes2.head())

df_normalizado = pd.json_normalize(dados_pacientes2['Pacientes'])
print(df_normalizado)