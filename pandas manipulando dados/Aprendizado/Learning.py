import pandas as pd

url = '/content/drive/MyDrive/Ciência de Dados/Data Science Alura/1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx'

data = pd.read_excel(url, sheet_name='GEE Estados',)

data

data['Emissão / Remoção / Bunker'].unique()

((data['Emissão / Remoção / Bunker'] == 'Remoção NCI') | (data['Emissão / Remoção / Bunker'] == 'Remoção'))

data[data['Emissão / Remoção / Bunker'].isin(['Remoção NCI','Remoção'])]

data.loc[data['Emissão / Remoção / Bunker'].isin(['Remoção NCI','Remoção']), 1970:2021]

data.loc[data['Emissão / Remoção / Bunker'].isin(['Remoção NCI','Remoção']), 1970:2021].max()

data.loc[data['Emissão / Remoção / Bunker'] == 'Bunker', 'Estado'].unique()

data = data.loc[data['Emissão / Remoção / Bunker'] == 'Emissão']
data

data = data.drop(columns='Emissão / Remoção / Bunker')
data

data.loc[:,'Nível 1 - Setor':'Produto'].columns

colunas_info = list(data.loc[:,'Nível 1 - Setor':'Produto'].columns)
colunas_info

colunas_emissao = list(data.loc[:,1970:2021].columns)
colunas_emissao

data.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano', value_name = 'Emissão')

emissoes_por_ano = data.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano', value_name = 'Emissão')