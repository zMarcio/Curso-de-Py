# Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. 
# Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação de qual é o Estado a que pertence: 
# estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG'].

# A empresa sempre está abrindo novas filiais, 
# de modo que a tabela está constantemente recebendo novos registros e o gestor gostaria de possuir a informação atualizada da quantidade de filiais em cada Estado.

# A partir da coluna com a informação dos Estados, 
# crie um dicionário usando dict comprehension com a chave sendo o nome de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.
estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
unic_estados = list(set(estados))
lista_das_Listas = []
for i in estados:
    lista = [p for p in estados if i == p]
    lista_das_Listas.append(lista)

# print(lista_das_Listas)

testing = {unic_estados[i]:len(lista_das_Listas[i]) for i in range(len(unic_estados))}

print(testing)
