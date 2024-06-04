import pandas as pd

url = '/content/drive/MyDrive/Ciência de Dados/Data Science Alura/1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx'

data = pd.read_excel(url, sheet_name='GEE Estados',)
colunas_info = list(data.loc[:,'Nível 1 - Setor':'Produto'].columns)

colunas_emissao = list(data.loc[:,1970:2021].columns)

emissoes_por_ano = data.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano', value_name = 'Emissão')

emissoes_por_ano.groupby('Nível 1 - Setor').groups


emissoes_por_ano.groupby('Nível 1 - Setor').get_group('Agropecuária')