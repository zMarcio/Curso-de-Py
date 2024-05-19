# 12. A Busca pelo Design Perfeito
# Uma pesquisa de mercado foi realizada para determinar qual design de marca infantil é o mais popular. Os votos computados são os seguintes:
# - Design 1 - 1334 votos
# - Design 2 - 982 votos
# - Design 3 - 1751 votos
# - Design 4 - 210 votos
# - Design 5 - 1811 votos

# Adapte esses dados para um dicionário e, a partir dele, informe o design vencedor e a porcentagem de votos que ele recebeu.

dic = {
    'Design_1': 1334,
    'Design_2': 982,
    'Design_3': 1751,
    'Design_4': 210,
    'Design_5': 1811,
}

p = 0
pp = ''
for d,v in dic.items():
    if v > p:
        pp = d
        p = v

print(f'O Designer: {pp} ganhou a votação com {p}')