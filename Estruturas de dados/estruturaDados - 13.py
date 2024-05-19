# 13. Calculando o Abono Salarial
# Os colaboradores de um setor da empresa receberão um abono de 10% do salário. 
# O abono mínimo não pode ser inferior a 200 reais. 
# Crie um código que transforme os salários em chaves de um dicionário e o abono correspondente em seus valores. 
# Calcule e exiba o total de gastos com o abono, o número de colaboradores que receberam o abono mínimo e o valor do maior abono concedido.

# ### Dados
# ```python
# salarios = [117,2, 164,4, 261,7, 513,0, 553,2, 634,1, 665,0, 723,8, 768,5, 778,2, 790,3]
# ```

salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
dic = {}
for i in salarios:
    if i / 10 > 200:
        dic[i] = 200
    else:
        dic[i] = i / 10


for v,ab in dic.items():
    print(f'Salário: {v}, Abono: {ab}')