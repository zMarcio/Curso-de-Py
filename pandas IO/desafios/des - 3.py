import requests
import json
import pandas as pd

# # da um request no dado da api, trazendo  assim em formato json
dados_frutas = requests.get('https://fruityvice.com/api/fruit/all')

resultado = json.loads(dados_frutas.text)

pd.DataFrame(resultado)
# # Aqui ele tenta Normaliza o objeto json que vem para ele, se tiver aninhado ele trás o nome da aniação chave e pós isso coloca o nome da chave
test = pd.json_normalize(resultado)
print(test)
