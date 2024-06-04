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