import pandas as pd
import numpy as np
import json

url = '/content/drive/MyDrive/Ciência de Dados/Data Science Alura/dataset-telecon.json'

# data = pd.read_json(url)

# data = pd.json_normalize(data[['cliente','telefone','internet','conta']])

# cliente = pd.json_normalize(data['cliente'])
# telefone = pd.json_normalize(data['telefone'])
# internet = pd.json_normalize(data['internet'])
# conta = pd.json_normalize(data['conta'])

# data.head()

with open(url) as f:
  leitura = json.load(f)

leitura

data = pd.json_normalize(leitura)

data.head()


data.info()

data[data['conta.cobranca.Total'] == ' '][
    ['cliente.tempo_servico', 'conta.contrato','conta.cobranca.mensal','conta.cobranca.Total']
]

index = data[data['conta.cobranca.Total'] == ' '].index

data.loc[index, 'conta.cobranca.Total'] = data.loc[index, 'conta.cobranca.mensal'] * 24
data.loc[index, 'conta.cobranca.Total']

data.loc[index, 'cliente.tempo_servico'] = 24
data.loc[index, 'cliente.tempo_servico']

data.loc[index][
    ['cliente.tempo_servico', 'conta.contrato','conta.cobranca.mensal','conta.cobranca.Total']
]

data['conta.cobranca.Total'] = data['conta.cobranca.Total'].astype(np.float64)

data.info()

for col in data.columns:
  print(f'Coluna: {col}')
  print(data[col].unique())
  print('-'*30)

  data.query("Churn == ''")

data_dif = data[data['Churn'] != ''].copy()

data_dif.info()

data_dif.reset_index(drop=True,inplace=True)

data_dif

data_dif.duplicated()

data_dif.duplicated().sum()

fil_duplicated = data_dif.duplicated()
fil_duplicated

data_dif[fil_duplicated]

data_dif.drop_duplicates(inplace=True)
data_dif.duplicated().sum()

data_dif.isna()

data_dif.isna().sum()

data_dif.isna().sum().sum()

data_dif[data_dif.isna().any(axis=1)]

filtro = data_dif['cliente.tempo_servico'].isna()

data_dif[filtro][['cliente.tempo_servico', 'conta.cobranca.mensal','conta.cobranca.Total']]

data_dif['cliente.tempo_servico'].fillna(
    np.ceil(
        data_dif['conta.cobranca.Total'] / data_dif['conta.cobranca.mensal']
    ), inplace=True
)

data_dif[filtro][['cliente.tempo_servico', 'conta.cobranca.mensal','conta.cobranca.Total']]

data_dif.isna().sum()

data_dif['conta.contrato'].value_counts()

colunas_dropar = ['conta.contrato', 'conta.faturamente_eletronico', 'conta.metodo_pagamento']

data_dif[colunas_dropar].isna().any(axis=1).sum()

df_sem_nulo = data_dif.dropna(subset=colunas_dropar).copy()
df_sem_nulo.head()

df_sem_nulo.reset_index(drop=True,inplace=True)
df_sem_nulo.isna().sum()