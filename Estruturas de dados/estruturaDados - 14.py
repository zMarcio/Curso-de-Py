# 14. Explorando a Diversidade Biológica
# Uma equipe de cientistas está estudando a diversidade biológica em uma floresta. 
# Os dados coletados sobre o número de espécies de plantas e animais em cada área da floresta estão armazenados em um dicionário. 
# Crie um código que calcule a média de espécies por área e identifique a área com a maior diversidade biológica.
# Dica: Utilize as funções `sum()` e `len()`.
# python
especies = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

sumMedia = {}

for i,v in especies.items():
    sumMedia[i] = (v[0] + v[1])/2

p = 0
pp = ''

for i,ii in sumMedia.items():
    print(f'Aqui está cada área e a média delas, Área: {i}, Média respectiva: {ii}')

for a,b in sumMedia.items():
    if b > p:
        p = b
        pp = a


print(f'Maior média {p} e a área {pp}')