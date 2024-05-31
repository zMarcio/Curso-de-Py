import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1pvBoLyX8kP0TjtUbadVMGdTl4yzm6bHMThhPiqCVtpw/gviz/tq?tqx=out:csv&sheet'

data = pd.read_csv(url)

print(data)

data.to_csv('dados_emissoes_co2.csv', index=False)