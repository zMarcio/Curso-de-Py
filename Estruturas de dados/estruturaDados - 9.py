# 9. Corrigindo Provas com Python
# Desenvolva um programa que corrige uma prova de 10 questões. 
# O programa deve solicitar a resposta do aluno para cada questão e verificar se a resposta está correta, 
# comparando com o gabarito fornecido.
# Calcule a nota do aluno, considerando que cada questão vale um ponto.
# Gabarito da Prova
# 01 - D
# 02 - A
# 03 - C
# 04 - B
# 05 - A
# 06 - D
# 07 - C
# 08 - C
# 09 - A
# 10 - B

dic = {
    1 : 'D',
    2 : 'A',
    3 : 'C',
    4 : 'B',
    5 : 'A',
    6 : 'D',
    7 : 'C',
    8 : 'C',
    9 : 'A',
    10 : 'B',
}

i = 1
nota = 0
while i != 11:
    resposta = input(f'Diga a alternativa que você escolheu na {i}: ').upper()
    if resposta in dic[i]:
        nota += 1
    i += 1

print(nota)