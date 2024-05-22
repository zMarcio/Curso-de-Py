#  Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP).
#  Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho maior ou igual a 5,
# exibindo-as em uma lista. Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.

digiteAlgo = 'Aprender Python aqui na Alura é muito bom'
digiteAlgo = digiteAlgo.replace(',', ' ').replace('.',' ').replace('!', ' ').replace('?', ' ').split()


tamanho = list(filter(lambda x: len(x) >= 5,digiteAlgo))

print(tamanho)

