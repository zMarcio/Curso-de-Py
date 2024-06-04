import pandas as pd

url = '/content/drive/MyDrive/Ciência de Dados/Data Science Alura/1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx'

data = pd.read_excel(url, sheet_name='GEE Estados',)
colunas_info = list(data.loc[:,'Nível 1 - Setor':'Produto'].columns)

colunas_emissao = list(data.loc[:,1970:2021].columns)

emissao = data.melt(id_vars = colunas_info, value_vars = colunas_emissao, var_name = 'Ano', value_name = 'Emissão')

setores = emissao.pivot_table(values = 'Emissão', index = 'Ano', columns = 'Nível 1 - Setor', aggfunc = 'mean')
setores

testing = emissao.groupby(['Estado', 'Nível 1 - Setor'])[['Emissão']].sum()
testing

testing.xs('Energia', level=1)

testing.xs('MG',level=0).idxmax()

testing = emissao.groupby(['Estado', 'Nível 1 - Setor'])[['Emissão']].sum()
testing.groupby(level=0).idxmax()

testing = emissao.groupby(['Estado', 'Nível 1 - Setor'])[['Emissão']].sum()
testing.groupby(level=1).idxmax()