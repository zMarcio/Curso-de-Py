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