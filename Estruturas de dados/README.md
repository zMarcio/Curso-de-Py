**Examples**

1 - Uso do Split em string
2 - Uso do join em listas
3 - Controlando listas, com metodos do py


# Lista de Exercícios de Programação

## 1. Desvendando os Gastos da Empresa de Papel
Sua missão é criar um programa que calcule a média dos gastos de uma empresa de papel, utilizando a lista gastos fornecida.
Dica: Utilize as funções `sum()` e `len()` para simplificar seus cálculos.

```python
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
media_gastos = sum(gastos) / len(gastos)
print(f'Média de gastos: {media_gastos:.2f}')
```

## 2. Investigando Compras acima de 3000 Reais
Utilizando os mesmos dados da questão anterior, descubra quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem dessas compras em relação ao total de compras.

```python
compras_acima_3000 = [gasto for gasto in gastos if gasto > 3000]
quantidade_acima_3000 = len(compras_acima_3000)
percentual_acima_3000 = (quantidade_acima_3000 / len(gastos)) * 100
print(f'Compras acima de 3000: {quantidade_acima_3000}')
print(f'Porcentagem de compras acima de 3000: {percentual_acima_3000:.2f}%')
```

## 3. Colecionando Números Inteiros
Crie um código que colete 5 números inteiros do usuário e os armazene em uma lista. Exiba a lista no final da coleta.

```python
numeros = [int(input(f'Digite o {i+1}º número: ')) for i in range(5)]
print(numeros)
```

## 4. Invertendo a Ordem dos Números
Agora, colete mais 5 números inteiros e imprima a lista em ordem inversa, mostrando os números na ordem contrária àquela em que foram digitados.

```python
numeros = [int(input(f'Digite o {i+1}º número: ')) for i in range(5)]
print(numeros[::-1])
```

## 5. Desvendando os Números Primos
Desenvolva um programa que, ao receber um número qualquer do usuário, gere uma lista contendo todos os números primos entre 1 e o número digitado.

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input('Digite um número: '))
primos = [x for x in range(2, numero + 1) if is_prime(x)]
print(primos)
```

## 6. Validando Datas com Precisão
Escreva um programa que peça ao usuário o dia, mês e ano de uma data e determine se a data é válida.

```python
import datetime

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

try:
    data = datetime.date(ano, mes, dia)
    print('Data válida')
except ValueError:
    print('Data inválida')
```

## 7. A Explosão Bacteriana: Medindo o Crescimento
Para um estudo sobre o crescimento de uma colônia de bactérias, você possui o número de bactérias por dia. Crie um código que gere uma lista contendo o percentual de crescimento de bactérias a cada dia, comparando o número de bactérias de um dia com o do dia anterior.
Dica: Utilize a fórmula: `percentual_crescimento = 100 * (amostra_atual - amostra_passada) / amostra_passada`

```python
bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
percentual_crescimento = [100 * (bacterias[i] - bacterias[i-1]) / bacterias[i-1] for i in range(1, len(bacterias))]
print(percentual_crescimento)
```

## 8. Classificando Doces e Amargos
Imagine uma seleção de produtos alimentícios, onde cada produto possui um ID. Produtos com IDs pares são doces, e os com IDs ímpares são amargos. Crie um código que colete 10 IDs de produtos, calcule e exiba a quantidade de produtos doces e amargos.

```python
ids = [int(input(f'Digite o ID do {i+1}º produto: ')) for i in range(10)]
doces = [id for id in ids if id % 2 == 0]
amargos = [id for id in ids if id % 2 != 0]
print(f'Produtos doces: {len(doces)}')
print(f'Produtos amargos: {len(amargos)}')
```

## 9. Corrigindo Provas com Python
Desenvolva um programa que corrige uma prova de 10 questões. O programa deve solicitar a resposta do aluno para cada questão e verificar se a resposta está correta, comparando com o gabarito fornecido. Calcule a nota do aluno, considerando que cada questão vale um ponto.
- Gabarito da Prova:
  ```
  01 - D
  02 - A
  03 - C
  04 - B
  05 - A
  06 - D
  07 - C
  08 - C
  09 - A
  10 - B
  ```

```python
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
respostas = [input(f'Resposta da questão {i+1}: ').upper() for i in range(10)]
nota = sum(1 for i in range(10) if respostas[i] == gabarito[i])
print(f'Nota do aluno: {nota}')
```

## 10. Mergulhando no Clima: Analisando Temperaturas
Um instituto de meteorologia precisa analisar as temperaturas médias de cada mês do ano. Crie um código que colete essas temperaturas, armazene-as em uma lista, calcule a média anual e exiba todas as temperaturas acima da média anual, juntamente com o nome do mês correspondente (Janeiro, Fevereiro, etc.).

```python
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = [float(input(f'Temperatura média de {mes}: ')) for mes in meses]
media_anual = sum(temperaturas) / len(temperaturas)
acima_da_media = [(meses[i], temp) for i, temp in enumerate(temperaturas) if temp > media_anual]
print(f'Média anual: {media_anual:.2f}')
print('Temperaturas acima da média anual:')
for mes, temp in acima_da_media:
    print(f'{mes}: {temp:.2f}')
```

## 11. Analisando as Vendas do E-commerce
Uma empresa de e-commerce deseja analisar as vendas dos seus produtos. Os dados de vendas foram armazenados em um dicionário. Escreva um código que calcule o total de vendas e identifique o produto mais vendido.

```python
vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
total_vendas = sum(vendas.values())
produto_mais_vendido = max(vendas, key=vendas.get)
print(f'Total de vendas: {total_vendas}')
print(f'Produto mais vendido: {produto_mais_vendido}')
```

## 12. A Busca pelo Design Perfeito
Uma pesquisa de mercado foi realizada para determinar qual design de marca infantil é o mais popular. Os votos computados são os seguintes:
- Design 1 - 1334 votos
- Design 2 - 982 votos
- Design 3 - 1751 votos
- Design 4 - 210 votos
- Design 5 - 1811 votos

Adapte esses dados para um dicionário e, a partir dele, informe o design vencedor e a porcentagem de votos que ele recebeu.

```python
votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}
total_votos = sum(votos.values())
design_vencedor = max(votos, key=votos.get)
percentual_vencedor = (votos[design_vencedor] / total_votos) * 100
print(f'Design vencedor: {design_vencedor} com {percentual_vencedor:.2f}% dos votos')
```

## 13. Calculando o Abono Salarial
Os colaboradores de um

 setor da empresa receberão um abono de 10% do salário. O abono mínimo não pode ser inferior a 200 reais. Crie um código que transforme os salários em chaves de um dicionário e o abono correspondente em seus valores. Calcule e exiba o total de gastos com o abono, o número de colaboradores que receberam o abono mínimo e o valor do maior abono concedido.

```python
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = {salario: max(salario * 0.1, 200) for salario in salarios}
total_gastos = sum(abonos.values())
abono_minimo = sum(1 for abono in abonos.values() if abono == 200)
maior_abono = max(abonos.values())
print(f'Total de gastos com abono: {total_gastos:.2f}')
print(f'Colaboradores que receberam abono mínimo: {abono_minimo}')
print(f'Maior valor de abono: {maior_abono:.2f}')
```

## 14. Explorando a Diversidade Biológica
Uma equipe de cientistas está estudando a diversidade biológica em uma floresta. Os dados coletados sobre o número de espécies de plantas e animais em cada área da floresta estão armazenados em um dicionário. Crie um código que calcule a média de espécies por área e identifique a área com a maior diversidade biológica.
Dica: Utilize as funções `sum()` e `len()`.

```python
especies = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

media_especies = {area: sum(valores) / len(valores) for area, valores in especies.items()}
area_mais_diversa = max(media_especies, key=media_especies.get)
print(f'Média de espécies por área: {media_especies}')
print(f'Área com maior diversidade biológica: {area_mais_diversa}')
```

## 15. Analisando as Idades dos Colaboradores
O RH da sua empresa precisa de sua ajuda para analisar as idades dos colaboradores em 4 setores. Os dados das idades de cada setor foram fornecidos. Crie um código que calcule a idade média de cada setor, a idade mínima e máxima de cada setor e a idade média geral dos colaboradores.

```python
idades = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

for setor, lista_idades in idades.items():
    idade_media = sum(lista_idades) / len(lista_idades)
    idade_minima = min(lista_idades)
    idade_maxima = max(lista_idades)
    print(f'{setor}:')
    print(f'  Idade média: {idade_media:.2f}')
    print(f'  Idade mínima: {idade_minima}')
    print(f'  Idade máxima: {idade_maxima}')

idade_media_geral = sum(sum(lista_idades) for lista_idades in idades.values()) / sum(len(lista_idades) for lista_idades in idades.values())
print(f'Idade média geral dos colaboradores: {idade_media_geral:.2f}')
```