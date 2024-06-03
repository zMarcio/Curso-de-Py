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

emissoes_por_ano

emissoes_por_ano.groupby('Ano')[['Emissão']].mean().plot(figsize=(10,6));

emissoes_por_ano.groupby('Ano')[['Emissão']].mean().idxmax()

emissoes_por_ano.groupby(['Ano', 'Gás'])[['Emissão']].mean()

media_emissao_anual = emissoes_por_ano.groupby(['Ano', 'Gás'])[['Emissão']].mean().reset_index()
media_emissao_anual

media_emissao_anual = media_emissao_anual.pivot_table(index = 'Ano', columns = 'Gás', values = 'Emissão')
media_emissao_anual

media_emissao_anual.plot(subplots = True, figsize=(10,40));


gov_url = '/content/drive/MyDrive/Ciência de Dados/Data Science Alura/POP2022_Municipios.xls'

testing = pd.read_excel(gov_url,header = 1, skipfooter = 34)

testing

testing.groupby('UF').sum(numeric_only=True)

testing['POPULAÇÃO'].astype(int)

testing[testing['POPULAÇÃO'].str.contains('\(', na=False)]

testing = testing.assign(semparenteses = testing['POPULAÇÃO'].replace('\(\d{1,2}\)', '', regex=True), pop = lambda x : x.loc[:, 'semparenteses'].replace('\.','',regex=True))

testing[testing['POPULAÇÃO'].str.contains('\(', na=False)]

testing = testing.astype({'pop':'int64'})

testing = testing.groupby('UF')[['pop']].sum(numeric_only=True).reset_index()
testing

emissao_estados = emissoes_por_ano[emissoes_por_ano['Ano'] == 2021].groupby('Estado')[['Emissão']].sum().reset_index()
emissao_estados