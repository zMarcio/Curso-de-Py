import pandas as pd
url = '' # Fiz no google colab e o link é para meu drive

# test = pd.ExcelFile(url).sheet_names

# test

data = pd.read_excel(url,sheet_name='GEE Estados',)
data

# data['Nível 1 - Setor'].unique()
