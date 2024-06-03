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

emissoes_por_ano.groupby('Gás')

emissoes_por_ano.groupby('Gás').groups

emissoes_por_ano.groupby('Gás').get_group('CO2 (t)')

emissoes_por_ano.groupby('Gás')[['Emissão']].sum()

emissao_por_gas = emissoes_por_ano.groupby('Gás')[['Emissão']].sum().sort_values('Emissão', ascending=False)
emissao_por_gas

emissao_por_gas.plot(kind = 'barh', figsize = (10,6))

emissao_por_gas.iloc[0:9]

print(f'A emissão de CO2 corresponde {float((emissao_por_gas.iloc[0:9].sum()/emissao_por_gas.sum()).iloc[0])*100:.2f} % de emissão de total de gases estufa no Brasil de 1970 a 2021')

gas_por_setor = emissoes_por_ano.groupby(['Gás', 'Nível 1 - Setor'])[['Emissão']].sum()
gas_por_setor

gas_por_setor = emissoes_por_ano.groupby(['Gás', 'Nível 1 - Setor'])[['Emissão']].sum()
gas_por_setor

gas_por_setor.xs('CO2 (t)', level = 0).max()

gas_por_setor.xs('CO2 (t)', level = 0).idxmax()

gas_por_setor.groupby(level = 0).idxmax()

gas_por_setor.groupby(level = 0).max()

valores_max = gas_por_setor.groupby(level = 0).max().values

tabela_sumarizada = gas_por_setor.groupby(level = 0).idxmax()
tabela_sumarizada.insert(1,'Quantidade de emissão', valores_max)
tabela_sumarizada

gas_por_setor.swaplevel(0,1)

gas_por_setor.swaplevel(0,1).groupby(level=0).idxmax()