# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5


newNotas = map(lambda x : x + qualitativo, notas)

newNotas = list(newNotas)

print(newNotas)


temp_celsius = [0, 25, 37, 78, 100]
temp_fahrenheit = list(map(lambda x: (x * 9/5) + 32, temp_celsius))
print(temp_fahrenheit)