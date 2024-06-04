import pandas as pd
import numpy as np

locacao_url = '/content/drive/MyDrive/Ciência de Dados/Data Science Alura/dados_locacao_imoveis.json'
data_locacao = pd.read_json(locacao_url)
data_locacao = pd.json_normalize(data_locacao['dados_locacao'])
data_locacao.head()

columns = list(data_locacao.columns)
data_locacao = data_locacao.explode(columns[1:])
data_locacao

data_locacao.reset_index(drop=True,inplace=True)

data_locacao['valor_aluguel'] = data_locacao['valor_aluguel'].apply(lambda x : x.replace('$','').replace(',','.').replace('reais',''))
data_locacao['valor_aluguel'] = data_locacao['valor_aluguel'].astype(np.float64)
data_locacao.head()