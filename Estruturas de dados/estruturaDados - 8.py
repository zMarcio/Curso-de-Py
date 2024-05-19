# 8. Classificando Doces e Amargos
# Imagine uma seleção de produtos alimentícios, 
# onde cada produto possui um ID. Produtos com IDs pares são doces, 
# e os com IDs ímpares são amargos. Crie um código que colete 10 IDs de produtos, 
# calcule e exiba a quantidade de produtos doces e amargos.

i = 0
list_doce = 0
list_amargo = 0
while i != 10:
    dig_idDoce = int(input('digite o id do doce: '))
    if dig_idDoce % 2 == 0:
        list_doce += 1
    else:
        list_amargo += 1
    i += 1

print(f'Total de doces {i}, doces amargos {list_amargo} e doce {list_doce}')