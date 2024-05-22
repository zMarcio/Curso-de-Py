# Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, 
# sendo elas: Salvador, Fortaleza, Natal e Aracaju.

# O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, 
# sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

# Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, 
# crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina)
# e a 3ª os gastos com passeio e alimentação (gasto_passeio).

# Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.

def gasto_hotel(dias) -> float:
    # diaria do hotel 150 reais
    return 150 * dias



def gasto_gasolina(cidade:str) -> float:
    distancia = [850, 800, 300, 550] 
    gasolina = 5
    kmLitro = 14
    cidade = cidade.capitalize()
    if cidade == 'Fortaleza':
        return (2 * distancia[1] * gasolina / kmLitro)
    if cidade == 'Salvador':
        return (2 * distancia[0] * gasolina / kmLitro)
    if cidade == 'Natal':
        return (2 * distancia[2] * gasolina / kmLitro)
    if cidade == 'Aracaju':
        return (2 * distancia[3] * gasolina / kmLitro)
    
    


def gasto_passeio(cidade, dias) -> float:
    custo = [200, 400, 250, 300]
    cidade = cidade.capitalize()
    if cidade == 'Fortaleza':
        return (custo[1] * dias)
    if cidade == 'Salvador':
        return (custo[0] * dias)
    if cidade == 'Natal':
        return (custo[2] * dias)
    if cidade == 'Aracaju':
        return (custo[3] * dias)

dias = int(input('Digite os dias que você ficara: '))
cidade = input('Digite para qual cidade você vai [Salvador, Fortaleza, Natal ou Aracaju]: ')



print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade.capitalize()} saindo de Recife custaria {gasto_gasolina(cidade) + gasto_hotel(dias) + gasto_passeio(cidade,dias):.2f} reais")
