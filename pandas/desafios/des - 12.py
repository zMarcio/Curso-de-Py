import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
# # pd.read_csv lê um arquivo, e nele se passa o url, ou onde tá o arquivos, coloca que atributo que quer que ele separe e por ai vai
# data = pd.read_csv(url,delimiter=';')
dados = pd.read_csv(url, sep=';')


df = dados

df.Tipo.unique()

df.drop('Tipo', axis=1,inplace=True)

selecao_filtro2 = (df['Quartos'] >= 2) & (df['Valor'] < 3000) & (df['Area'] > 70)
df_filtro2 = df[selecao_filtro2]

print(df_filtro2.head())


df_filtro2.to_csv('dados_filtro_2.csv', index=False, sep=';')
