notas = {'1º Trimestre': 8.5, '2º Trimestre': 7.5, '3º Trimestre': 9}

somatorio = sum(notas.values())
print(somatorio)

qtd_notas = len(notas)

print(round(somatorio/qtd_notas, 2))
  