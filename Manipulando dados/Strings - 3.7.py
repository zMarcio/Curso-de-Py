# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
frase =  input('Digite uma frase: ')
print(frase)
print('Abaixo a frase sem espaços:')
print(frase.strip().lower())