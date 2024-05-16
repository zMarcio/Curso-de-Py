numInteiroOrDecimal = input('Digite um numero')

if '.' not in numInteiroOrDecimal:
    print("inteiro")
elif '.0' in numInteiroOrDecimal:
    print('inteiro')
else:
    print('decimal')
