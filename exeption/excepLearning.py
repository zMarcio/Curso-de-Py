notas = [5.0, 2.0, 6.0, 8.0]

def fun(nota):

    if len(nota) > 3:
        raise ValueError('Tem mais do que três notas')

    for i,nt in enumerate(nota):
        print(f'esse é o i {i} e esse é o nt {nt}')

try:
    allNotas = fun(notas)
except  Exception as e:
    print(e)
else:
    print(allNotas)
finally:
    print('Request finalizada')

