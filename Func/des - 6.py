# Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, 
# você precisa criar uma função que receba uma lista de 4 notas e retorne:

# maior nota
# menor nota
# média
# situação (Aprovado(a) ou Reprovado(a))

# Para testar o comportamento da função, os dados podem ser exibidos em um texto:

# "O(a) estudante obteve uma média de [media], com a sua maior nota de [maior] pontos e a menor nota de [menor] pontos e foi [situacao]"


def calcMediaEstudante(notas:list):
    maxi = max(notas)
    mini = min(notas)
    media = sum(notas)/len(notas)
    status = ''
    if media >= 6:
        status = 'Aprovado'
    elif media >= 5 and media < 6:
        status = 'Recuperação'
    else:
        status = 'Reprovado'
    return maxi,mini,media,status



notas = float(input('Digite as notas: '))

# para caso de teste, coloquei esses numeros no vetor (3,4,5,6), (4,5,6,7) e (7,8,9,10), para se testar todas as verficações, e comentei notas e o while todo.
todasNotas = []

while len(todasNotas) != 4:
    todasNotas.append(notas)
    notas = float(input('Digite as notas: '))

maxi,mini,media,status = calcMediaEstudante(todasNotas)

print(f"O(a) estudante obteve uma média de {media}, com a sua maior nota de {maxi} pontos e a menor nota de {mini} pontos e foi {status}")
