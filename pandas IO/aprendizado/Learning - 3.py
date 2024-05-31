import pandas as pd

# url = '/content/emissoes_CO2.xlsx'

sheet_id = '1ZllckIT4-HfMLHa4KOW97Jgj5e0LoxL_YQsv_nWYobY' 

url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet'

dados_co2 = pd.read_csv(url)

dados_co2.head()


sheet_id = '1ZllckIT4-HfMLHa4KOW97Jgj5e0LoxL_YQsv_nWYobY' 
sheet_name = 'emissoes_percapita'
url_percapita = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

percapita_sheets = pd.read_csv(url_percapita)
percapita_sheets.head()

sheet_id = '1ZllckIT4-HfMLHa4KOW97Jgj5e0LoxL_YQsv_nWYobY' 
sheet_name = 'fontes'
url_fontes = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'

fontes_sheets = pd.read_csv(url_fontes)
fontes_sheets.head()