# Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade de pessoas colaboradoras 
# e o(a) gestor(a) gostaria de ter um agrupamento da soma dessas pessoas para cada estado. As informações contidas na tabela são:

# funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

# A partir da lista de tuplas, crie um dicionário em que as chaves são os nomes dos Estados únicos e os valores são as listas com o número de colaboradores(as) referentes ao Estado.
# Crie também um dicionário em que as chaves são os nomes dos Estados e os valores são a soma de colaboradores(as) por Estado.



# funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), 
#                 ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), 
#                 ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8),
#                 ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), 
#                 ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), 
#                 ('ES', 14), ('SP', 10), ('MG', 12)]

# dic_Fun = {}

# x = 0
# y = 0
# p = 0
# k = 0

# for i in range(0,len(funcionarios)):
#     if funcionarios[i][0] == 'SP':
#         x += funcionarios[i][1]
#         dic_Fun[funcionarios[i][0]] = x
#     if funcionarios[i][0] == 'MG':
#         y += funcionarios[i][1]
#         dic_Fun[funcionarios[i][0]] = y
#     if funcionarios[i][0] == 'ES':
#         p += funcionarios[i][1]
#         dic_Fun[funcionarios[i][0]] = p
#     if funcionarios[i][0] == 'RJ':
#         k += funcionarios[i][1]
        # dic_Fun[funcionarios[i][0]] = k


# print(dic_Fun)

funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), 
                ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), 
                ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8),
                ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), 
                ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), 
                ('ES', 14), ('SP', 10), ('MG', 12)]


# Separa os estados, colocando em um array, somente UM estado, já que ele se repete.
estados = list(set([i[0] for i in funcionarios]))
# Cria o dicionario para armazenar informações dos funcionarios e o estado
exp = {}

for i in estados:
    # forma um array para cada estado, dos funcionarios que trabalham no estado
    testing = [p[1] for p in funcionarios if p[0] == i]
    # armazena chave e valor necessaria, chave o estado, valor os funcionários
    exp[i] = sum(testing)
    
print(exp)











