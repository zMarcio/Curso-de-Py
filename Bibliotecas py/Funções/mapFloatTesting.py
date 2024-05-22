# primeiro transforma em list, depois trás com map para variavel, dizendo qual tipo de type os elementos irão ter, após isso faz o input e por fim separa cada 'elemento'
num = list(map(str, input("Oi digite varios numeros: ").split()))

# numeros = list(map(float, input("Digite uma sequência de números separados por espaços: ").split()))

for i in num : print(type(i))