import pandas as pd

url = '/content/drive/MyDrive/Ciência de Dados/Data Science Alura/1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx'

data = pd.read_excel(url, sheet_name='GEE Estados',)

data