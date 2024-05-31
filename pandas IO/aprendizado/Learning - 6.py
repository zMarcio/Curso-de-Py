import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/imdb_top_1000.xml'

data_imdb = pd.read_xml(url)

data_imdb.head()