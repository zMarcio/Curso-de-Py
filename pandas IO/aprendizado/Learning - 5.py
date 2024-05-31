import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/filmes_wikipedia.html'

# # Trás todas tabelas que encontra no html
data_html = pd.read_html(url)

# # como vem em lista da para fazer isso
top_filmes = data_html[1]

top_filmes.to_html('top_filmes.html')