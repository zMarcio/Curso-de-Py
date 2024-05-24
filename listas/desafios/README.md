### Desafios de Programação

1. **Soma dos Elementos das Listas**
   Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

   ```python
   lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
   ```

2. **Terceiro Elemento das Tuplas**
   Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:

   ```python
   lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
   ```

3. **Posição e Nome**
   A partir da lista:

   ```python
   lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
   ```

   Crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.

4. **Valores de Apartamentos**
   Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:

   ```python
   aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
   ```

5. **Dicionário de Despesas Mensais**
   Crie um dicionário usando o dict comprehension em que as chaves estão na lista:

   ```python
   meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
   ```

   e os valores estão em:

   ```python
   despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
   ```

### Aplicando a Projetos

6. **Filtragem de Vendas**
   Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores de venda:

   ```python
   vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
   ```

   Crie uma lista usando list comprehension para filtrar os valores de 2022 e que sejam maiores que 6000.

7. **Rotulagem de Glicose**
   Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da seguinte maneira:

   - Glicose igual ou inferior a 70: 'Hipoglicemia'
   - Glicose entre 70 a 99: 'Normal'
   - Glicose entre 100 e 125: 'Alterada'
   - Glicose superior a 125: 'Diabetes'

   A clínica disponibilizou parte dos valores:

   ```python
   glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
   ```

   Sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia em cada tupla.

8. **Tabela de Vendas**
   Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas:

   ```python
   id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
   preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]
   ```

   Crie uma lista de tuplas em que cada tupla tenha id, quantidade, preço e valor total (quantidade * preço), na qual a primeira tupla é o cabeçalho da tabela.

9. **Contagem de Filiais por Estado**
   Uma empresa possui filiais espalhadas nos Estados da região Sudeste do Brasil. Em uma das tabelas de cadastro das filiais há uma coluna contendo a informação de qual é o Estado a que pertence:

   ```python
   estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
   ```

   A partir da coluna com a informação dos Estados, crie um dicionário usando dict comprehension com a chave sendo o nome de um Estado e o valor sendo a contagem de vezes em que o Estado aparece na lista.

10. **Soma de Funcionários por Estado**
    Nessa mesma tabela de cadastro de filiais, há uma coluna com as informações da quantidade de pessoas colaboradoras:

    ```python
    funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
    ```

    Crie um dicionário usando dict comprehension para agrupar a soma dessas pessoas para cada estado.

---