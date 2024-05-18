# 4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas.
#  A leitura deve ser encerrada ao ser enviado o valor -273°C.


temperatura = 0
list_temp = []
while temperatura != -273:
    temperatura = float(input('Digite uma temperatura'))
    if temperatura == -273:
        print('ixi bateu -273')
        break
    list_temp.append(temperatura)

temperatura = 0

for i in list_temp:
    temperatura += i
    print(temperatura)
temperatura /= len(list_temp)
print(temperatura)