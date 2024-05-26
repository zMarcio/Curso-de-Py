import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
# # pd.read_csv lê um arquivo, e nele se passa o url, ou onde tá o arquivos, coloca que atributo que quer que ele separe e por ai vai
# data = pd.read_csv(url,delimiter=';')
dados = pd.read_csv(url, sep=';')

# # Organiza o modo de ver os dados que coletou
# dados = pd.DataFrame(dados)

# # ajusta dados para ver só as primeiras linhas, se você quiser mais dados só inserir dentro dos colchetes quantos você quer
print(dados.head(10))
# # faz o inverso da função a cima, em vez de pega os primeiros pega os ultimos
print(dados.tail(10))
# # Aqui você visualiza como é que tá a estrutura dos dados da pandas, no caso aqui está dizendo que é um pandas.core.frame.DataFrame, ou seja transformou a dados um DataFrame pandas.
print(type(dados))
# # Usado para ver quantidade de linhas e colunas vindo dessa forma (num de linhas e num de colunas)
print(dados.shape)
# # trás os nome das colunas do nosso dataframe
print(dados.columns)
# # trás o dados de cada coluna, o nome de cada coluna, quantidade de dados não nulos e o tipo de dados contido na coluna 
print(dados.info())
# # Por coluna específica
print(dados['Tipo'])
print('-'*30)
print(dados['Quartos'])
print('-'*30)
print(dados['IPTU'])

# # Selecionando duas colunas ao mesmo tempo
print(dados[['Quartos','Valor']])

# # Teste para ver se da para pegar só os 10 primeiros
print(dados[['Quartos','Valor']].head(10))
