turno = input('Digite o horário que você estuda: ').strip().lower()

if 'manhã' in turno or 'manha' in turno:
    print('Bom dia!')
elif 'tarde' in turno:
    print('Boa tarde!')
elif 'noite' in turno:
    print('Boa noite!')