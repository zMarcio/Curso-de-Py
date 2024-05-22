def escreve_mensagem(**mensagem):
    mensagemReturn = ''
    for value in mensagem.values():
        mensagemReturn += value
    return mensagemReturn

mensagem = {'mensagem': 'Bem-vindo, ', 'nome': 'Yuri'}
escreve_mensagem(**mensagem)
print(escreve_mensagem(**mensagem))