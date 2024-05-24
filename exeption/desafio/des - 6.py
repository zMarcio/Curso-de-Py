# Você está trabalhando com processamento de linguagem natural (NLP) e, dessa vez, sua líder requisitou que você criasse um trecho de código que recebe uma lista com as palavras separadas de uma frase gerada pelo ChatGPT.

# Você precisa criar uma função que avalia cada palavra desse texto e verificar se o tratamento para retirar os símbolos de pontuação (',' '.', '!' e '?') foi realizado. 
# Caso contrário, será lançada uma exceção do tipo ValueError apontando o 1º caso em que foi detectado o uso de uma pontuação por meio da 
# frase "O texto apresenta pontuações na palavra "[palavra]".". Essa demanda é voltada para a análise do padrão de frases geradas pela inteligência artificial.

# lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
#                   'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
#                   'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']



# lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
#                   'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
#                   'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']



lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil',
                  'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']

lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil',
                  'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde',
                  'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']



def tratamentoString(lista):
    try:
        for i in lista:
            for p in i:
                if '!' in p or '?' in p or ',' in p or '.' in p:
                    raise Exception(f'O texto apresenta pontuações na palavra "{p}".')
    except Exception as e:
        print(e)
    else:
        return 'Texto já tratado'

print(tratamentoString(lista_tratada))
print('-'*50)
print(tratamentoString(lista_nao_tratada))