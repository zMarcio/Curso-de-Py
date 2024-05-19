# 10. Mergulhando no Clima: Analisando Temperaturas
# Um instituto de meteorologia precisa analisar as temperaturas 
# médias de cada mês do ano. Crie um código que colete essas temperaturas, 
# armazene-as em uma lista, calcule a média anual e exiba todas as temperaturas acima da média anual, 
# juntamente com o nome do mês correspondente (Janeiro, Fevereiro, etc.).

temp_mes = {}
list_temps = []
list_highMedia = []
i = 0
temp_total = 0
while i != 12:
    name_mes = input('Digite o mes: ')
    name_temp = float(input('Digite a temperatura'))
    temp_total += name_temp

    list_temps.append([name_mes,name_temp])

    temp_mes[name_mes] = name_temp
    i += 1


for mes,temps in temp_mes.items():
    if (temp_total/12) < temps:
        list_highMedia.append([mes,temps])

print(f'Média anual: {(temp_total/12):.2f}, Temperaturas acima da média: {list_highMedia}')