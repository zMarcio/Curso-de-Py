import pandas as pd
import requests
import numpy as np

url_hospedagem = 'C:\\Users\\Marcio\\Desktop\\python_Alura\\pandas transformado e manipulando dados\\Objetos Json\\dados_hospedagem.json'
url_moveis = 'C:\\Users\\Marcio\\Desktop\\python_Alura\\pandas transformado e manipulando dados\\Objetos Json\\moveis_disponiveis.json'
dados = pd.read_json(url_hospedagem)
dados.head()

dados = pd.json_normalize(dados['info_moveis'])
dados.head()

colunas = list(dados.columns)
colunas
dados = dados.explode(colunas[3:])
dados

dados.reset_index(inplace=True,drop=True)
dados.head()

dados.info()

dados['max_hospedes'] = dados['max_hospedes'].astype(np.int64)
dados.info()

col_numericas = ['quantidade_banheiros', 'quantidade_quartos','quantidade_camas']
dados[col_numericas] = dados[col_numericas].astype(np.int64)
dados['avaliacao_geral'] = dados['avaliacao_geral'].astype(np.float64)
dados.info()

dados['preco'] = dados['preco'].apply(lambda x : x.replace('$', '').replace(',','').strip())
dados['preco'] = dados['preco'].astype(np.float64)

dados['taxa_limpeza'] = dados['taxa_limpeza'].apply(lambda x : x.replace('$', '').replace(',','').strip())
dados['taxa_limpeza'] = dados['taxa_limpeza'].astype(np.float64)

dados['taxa_deposito'] = dados['taxa_deposito'].apply(lambda x : x.replace('$', '').replace(',','').strip())
dados['taxa_deposito'] = dados['taxa_deposito'].astype(np.float64)

dados.head()

dados