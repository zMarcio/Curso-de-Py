# Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as para apresentar seus nomes completos na forma Nome Sobrenome. 
# As listas são:

# nomes = ["joão", "MaRia", "JOSÉ"]
# sobrenomes = ["SILVA", "souza", "Tavares"]

# O texto exibido ao fim deve ser parecido com:

# "Nome completo: Ana Silva"

# Dica: utilize a função map para mapear os nomes e sobrenomes e as funções de string para tratar o texto.
# 

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

def concStrings(nome,sobrenome):
    listNames = []
    p = 0
    for i in range(0,len(nome)):
        nameLastName = nome[p].capitalize() + ' ' + sobrenome[p].capitalize()
        listNames.append(nameLastName)
        p+=1
    return listNames


joao,maria,josé = concStrings(nomes,sobrenomes)

print(f'Primeiro: {joao}, segundo: {maria} e terceiro: {josé}')

