# Você foi contratado(a) como cientista de dados de uma associação de skate. 
# Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. 
# Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

# Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. 
# Retorne a média para apresentar o texto:

# "Nota da manobra: [media]"


def calcMediaSkate(notas:list):
    maxi = max(notas)
    mini = min(notas)
    p = 0
    for i in notas:
        if i == maxi or i == mini:
            notas.pop(p)
        p += 1
    notas = sum(notas)/len(notas)
    return notas



notas = float(input('Digite as notas: '))

# para caso de teste, coloquei esses numeros no vetor 6,7,8,9,10 e comentei notas e o while todo.
todasNotas = []

while len(todasNotas) != 5:
    todasNotas.append(notas)
    notas = float(input('Digite as notas: '))


print(f'Nota da manobra: {calcMediaSkate(todasNotas)}')