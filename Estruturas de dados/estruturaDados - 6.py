# # 6. Validando Datas com Precisão
# # Escreva um programa que peça ao usuário o dia,
# # mês e ano de uma data e determine se a data é válida.


dataNumbers = input('digite uma data: ')

dataNumbers.strip()



if dataNumbers.isalpha() == False:
    if '/' in dataNumbers:
        print(dataNumbers.replace('/', ' '))
    elif '.' in dataNumbers:
        print(dataNumbers.replace('.', ' ')) 
    elif '/' or '.' in dataNumbers:
        print('Por favor coloque formatado a data, com "/" ou "."')