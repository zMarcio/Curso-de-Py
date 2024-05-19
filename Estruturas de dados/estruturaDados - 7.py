# 7. A Explosão Bacteriana: Medindo o Crescimento
# Para um estudo sobre o crescimento de uma colônia de bactérias, você possui o número de bactérias por dia. 
# Crie um código que gere uma lista contendo o percentual de crescimento de bactérias a cada dia, comparando o número de bactérias de 
# um dia com o do dia anterior.
# Utilize a fórmula: `percentual_crescimento = 100 * (amostra_atual - amostra_passada) / amostra_passada
bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

list_Comparation = []
for i in range(1, len(bacterias)):
    percentual_crescimento = 100 * (bacterias[i] - bacterias[i-1]) / bacterias[i-1]
    list_Comparation.append(int(percentual_crescimento))


print(list_Comparation)


# # Lista de crescimento das bactérias
# bacterias_colonia = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
# # Lista que irá armazenar as porcentagens de crescimento
# porcentagem_crescimento = []
# # Vamos percorrer os índices de 1 a 9 para compararmos o valor atual com o passado
# for i in range(1, len(bacterias_colonia)):
#   # seguimos o cálculo 100 * (amostra_atual - amostra_passada) / (amostra_passada)
#   porcentagem = 100 * (bacterias_colonia[i] - bacterias_colonia[i-1]) / (bacterias_colonia[i-1])
#   # adicionamos o resultado na lista porcentagem_crescimento
#   porcentagem_crescimento.append(porcentagem)
# # Resultado
# print(f'Porcentagens de crescimento:\n{porcentagem_crescimento}')
