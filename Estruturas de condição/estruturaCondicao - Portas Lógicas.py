# AND(Para ser verdadeira todos os elementos precisa ser verdadeiro, ou ser falso, ficando assim:"F F verdadeiro e V V verdadeiro", agora V F falso e F V falso.)
t1 = True
t2 = True
t3 = False
t4 = False
print('AND:')
if t1 and t2:
    print('True')
else:
    print('false')

if t3 and t1:
    print('True')
else:
    print('False')
print('-'*10)

# OR (O OR funciona da seguinte maneira, um dos operadores precisa ser verdadeiro)
print('OR:')
if t1 or t3:
    print('True')
else:
    print('false')

if t3 or t4:
    print('True')
else:
    print('false')
print('-'*10)

# NOT (NOT inverte o valor do operador, se for True passa a ser False, e se for False passa a ser True)
print('NOT:')
if not t3:
    print('True')
else:
    print('false')

if not t1:
    print('True')
else:
    print('false')
print('-'*10)

# IN (IN ele verifica se tal variavel está dentro de uma lista)
print('IN:')
string = "Cebolácio", 'castelo', 'pedra', 'papel' , 'tesoura'
if 'tesoura' in string:
    print('True')
else:
    print('False')

if 'cabelo' in string:
    print('True')
else:
    print('False')
