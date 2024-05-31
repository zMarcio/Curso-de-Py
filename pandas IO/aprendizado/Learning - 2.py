import pandas as pd

# url = '/content/emissoes_CO2.xlsx'

url = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'

dados_co2 = pd.read_excel(url)

dados_co2.head()

pd.ExcelFile(url).sheet_names

emissoes = pd.read_excel(url,sheet_name='emissoes_C02',usecols='A:D')
emissoes_CO2 = pd.read_excel(url,sheet_name='emissoes_C02')
print(emissoes)

percapita = pd.read_excel(url ,sheet_name='emissoes_percapita')
print(percapita)


fontes = pd.read_excel(url,sheet_name='fontes')
print(fontes)

emissoes = pd.read_excel(url,sheet_name='emissoes_C02',usecols='A:D', nrows=10)

emissoes_CO2.to_excel('emissoes_CO2.xlsx',index=False)