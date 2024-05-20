# 8 - Para diversificar e atrair novos(as) clientes, 
# uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". 
# Neste item, 
# são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. 
# Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:

from random import randint
frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

fruit1,fruit2,fruit3 = 0,0,0
while fruit1 == fruit2 or fruit1 == fruit3 or fruit2 == fruit3:
    fruit1,fruit2,fruit3 = randint(0,11), randint(0,11), randint(0,11)


print(f'Você clicou na salada de frutas surpresa, então aqui está sua salada de fruta com {frutas[fruit1]}, {frutas[fruit2]} e {frutas[fruit3]}')
