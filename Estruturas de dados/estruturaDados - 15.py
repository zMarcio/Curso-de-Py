# 15. Analisando as Idades dos Colaboradores
# O RH da sua empresa precisa de sua ajuda para analisar as idades dos colaboradores em 4 setores. 
# Os dados das idades de cada setor foram fornecidos. 
# Crie um código que calcule a idade média de cada setor, a idade mínima e máxima de cada setor e a idade média geral dos colaboradores.

# ### Dados
# ```python
# idades = {
#     'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
#     'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
#     'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
#     'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
# }
# ```


idades = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

setAll = []

minp = 0
med = 0
maxp = 0
med_div = 0
for i,ii in idades.items():
    for a in ii:
        maxp = max(ii) 
        minp = min(ii)
        med += a
    med_div = len(ii)
    med = med/med_div
    setAll.append([i,maxp,minp,med])
    med = 0

for i in range(len(setAll)):
    print(f'Idade média do setor {setAll[i][0]}, a Média: {setAll[i][3]}, o mais velho tem essa idade {setAll[i][1]} e o mais jovem tem {setAll[i][2]}.')
