import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
# # pd.read_csv lê um arquivo, e nele se passa o url, ou onde tá o arquivos, coloca que atributo que quer que ele separe e por ai vai
# data = pd.read_csv(url,delimiter=';')
dados = pd.read_csv(url, sep=';')

df = dados

df.Tipo.unique()

df.drop('Tipo', axis=1,inplace=True)

selecao1 = df['Quartos'] == 1
print(df[selecao1])

selecao2 = df['Valor'] < 1200
print(df[selecao2])

selecao_final = (selecao1) & (selecao2)
print(df[selecao_final])

df_filtro1 = df[selecao_final]

# # Salvando o df_filtros em arquivos diferentes
df_filtro1.to_csv('dados_filtro_1.csv', index=False, sep=';')
