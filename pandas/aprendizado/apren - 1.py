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

# # Calculando todos os valores da coluna valor
dados['Valor'].mean()

# # Fazendo agrupamento de colunas, no caso vai pegar pela coluna tipo, e fazer a media para outras colunas
dados.groupby('Tipo').mean(numeric_only=True)

# # Pega por tipo e faz a média, só que aqui coloca somente a coluna Valor
dados.groupby('Tipo')['Valor'].mean()

# # Organiza do menor para maior a partir da coluna pedida, no caso 'Valor'
dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')

# # Passando dados a uma variavel, depois plota ela, criando assim um gráfico.
df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
df_preco_tipo.plot(kind='barh', figsize= (14, 10), color='purple')

# # Iremos usar o metodo unique para verificar os tipos unicos de imoveis dentro da nossa base de dados
dados.Tipo.unique()

# # Vamos colocar aqui todos os tipos que são comerciais
imoveis_Comerciais = ['Conjunto Comercial/Sala', 
                      'Prédio Inteiro', 'Loja/Salão', 
                      'Galpão/Depósito/Armazém', 
                      'Casa Comercial', 'Terreno Padrão',
                      'Loja Shopping/ Ct Comercial',
                      'Box/Garagem', 'Chácara',
                      'Loteamento/Condomínio', 'Sítio',
                      'Pousada/Chalé', 'Hotel', 'Indústria']


# # Pedimos aqui só os dados da tabela tipo que estão em imoveis_Comerciais
dados.query('@imoveis_Comerciais in Tipo')

# # Pedimos aqui todos os dados menos o de imoveis_Comerciais
dados.query('@imoveis_Comerciais not in Tipo')


# # Aqui colocamos esse dataframe dentro da variavel df
df = dados.query('@imoveis_Comerciais not in Tipo')
df.head()
# # Verifica as propriedades que estão em tipo df
df.Tipo.unique()



# # Está passando a uma variavel os valores conseguidos devido ao filtragem realizado a cima
df_preco_tipo = df.groupby('Tipo')[['Valor']].mean().sort_values('Valor')
# # A baixo está fazendo o plot, para visualizar as informações em gráficos
df_preco_tipo.plot(kind = 'barh', figsize = (14, 10), color = 'purple')

df.Tipo.unique()

# # Está contando quantos vezes aparece em nossa base dados os imoveis da coluna Tipo
df.Tipo.value_counts()

# # Trás em formato de percentual
df.Tipo.value_counts(normalize=True)

# # Irá converter o valor a baixo em um dataframe
df.Tipo.value_counts(normalize=True).to_frame().sort_values('proportion')

# # Criando um Gráfico que mostra a quantidade de vezes que um dado da coluna Tipo aparece, só que em forma de percentual
df_percentual_tipo = df.Tipo.value_counts(normalize=True).to_frame().sort_values('proportion')
df_percentual_tipo.plot(kind = 'bar', figsize = (14,10), color = 'green', xlabel = 'Tipos', ylabel = 'Percentual')

# # Selecionando apenas os apartamentos
# apt = ['Apartamento']
# df.query('@apt in Tipo')
# # Ou fazer assim
df.query('Tipo == "Apartamento"')

# # Atribui-se a query a variavel df e agora temos só os apartamentos
df = df.query('Tipo == "Apartamento"')
df.head()