# Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. 
# A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. 
# Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.



listFloat = [1.1,1.2,1.3,1.4,1.5] # [1.1,1.2,1.3,1.4,1.5,'a']
listInt = []

try:
    for i in listFloat:
        listInt.append(int(i))

except Exception as e:
    print(f'Erro: {e.__class__.__name__}')

else:
    print(listInt)

finally:
    print('Fim da execução da função')