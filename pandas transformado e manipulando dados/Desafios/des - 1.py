import pandas as pd
import numpy as np

vendas_url = '/content/drive/MyDrive/Ciência de Dados/Data Science Alura/dados_vendas_clientes.json'

data_vendas = pd.read_json(vendas_url)
data_vendas = pd.json_normalize(data_vendas['dados_vendas'])
data_vendas.head()

coluns = list(data_vendas.columns)
data_vendas = data_vendas.explode(coluns[1:])
data_vendas.head()

data_vendas.info()
data_vendas.reset_index(drop=True,inplace=True)

data_vendas['Valor da compra'] = data_vendas['Valor da compra'].apply(lambda x : x.replace('R$', '').replace(',','.'))
data_vendas['Valor da compra'] = data_vendas['Valor da compra'].astype(np.float64)
data_vendas.head()