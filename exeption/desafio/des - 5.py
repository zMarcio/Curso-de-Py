# Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste. 
# Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. 
# Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.

# Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, 
# você deve lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida". 
# O cálculo das 3 notas só será realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes. 
# Se não for lançada a exceção, será exibida uma lista com as notas em cada teste.

# Os dados para o teste do código são:

# Gabarito da prova:
# gabarito = ['D', 'A', 'B', 'C', 'A']

# Abaixo temos 2 listas de listas que você pode usar como teste

# Notas sem exceção:
# testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

# Notas com exceção:
# testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

def calcNota(lista):
    list_newNotas = []
    list_Alternativas = ['A', 'B', 'C', 'D']
    dic_Corretas = {
        0: 'D',
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'A'
    }
    
    try:
        for i in lista:
            x = 0
            nota_Usuário = 0
            for p in i:
                if p not in list_Alternativas:
                    raise Exception(f'A alternativa {p} não é uma opção de alternativa válida')
                elif p == dic_Corretas[x]:
                    nota_Usuário += 2
                x += 1
            list_newNotas.append((i, nota_Usuário))
    except Exception as e:
        print(e)
    else:
        return list_newNotas

# Exemplos de testes
testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

# Testando a função
print(calcNota(testes_sem_ex))  # Deve retornar a lista com notas sem exceções
print(calcNota(testes_com_ex))  # Deve imprimir a exceção e não retornar a lista de notas
