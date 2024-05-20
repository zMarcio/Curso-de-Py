# 10 - Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e o preço do metro quadrado da grama é de R$ 25,00.
# Peça à pessoa usuária o raio da área circular e devolva o valor em reais do quanto precisará pagar.

from math import pow as pw,pi

r = float(input('Digite seu raio: '))

formular = (pi * pw(r,2))

print(f'Aqui o preço da peça R$ {formular * 25:.2f}')