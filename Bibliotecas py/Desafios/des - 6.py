# 6 - Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. 
# A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. 
# Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.
from random import choice as ch
num_Participantes = int(input('Digite número de participantes: '))

list_Participantes = []

for i in range(1,num_Participantes):
    list_Participantes.append(i)

print(f'O número sorteado foi: {ch(list_Participantes)}')