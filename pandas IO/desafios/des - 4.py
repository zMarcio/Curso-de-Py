import pandas as pd

data_html = pd.read_html("https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o")
data_html[0]