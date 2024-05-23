Aqui estão os desafios reformulados para um repositório no GitHub, sem incluir as soluções:

---

### Desafios de Programação

1. **Divisão de Números Float**
   Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses números. O código deve conter um tratamento de erro, indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.

   Teste o programa com o segundo valor numérico do input igual a 0. Também teste utilizando caracteres textuais no input para checar os tipos de erro que ocorrem.

2. **Pesquisa em Dicionário**
   Faça um programa que solicite à pessoa usuária digitar um texto que será uma chave a ser pesquisada no seguinte dicionário:

   ```python
   idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}
   ```

   Armazene o resultado do valor em uma variável. O código deve conter um tratamento de erro KeyError, imprimindo a informação 'Nome não encontrado' caso ocorra o erro, e imprimir o valor caso não ocorra nenhum.

   Teste o programa com um nome presente em uma das chaves do dicionário e com um que não esteja no dicionário para verificar a mensagem de erro.

3. **Conversão de Lista para Float**
   Crie uma função que recebe uma lista como parâmetro e converta todos os valores da lista para float. A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar a lista caso não tenha ocorrido nenhum erro. Por fim, deve ter a cláusula finally para imprimir o texto: 'Fim da execução da função'.

4. **Agrupamento de Listas**
   Crie uma função que recebe duas listas como parâmetros e agrupe os elementos um a um das listas, formando uma lista de tuplas de 3 elementos, no qual o primeiro e segundo elemento da tupla são os valores na posição i das listas e o terceiro elemento é a soma dos valores na posição i das listas.

   A função deve conter um tratamento de erro indicando o tipo de erro gerado e retornar como resultado a lista de tuplas. Caso as listas enviadas como parâmetro tenham tamanhos diferentes, a função deve retornar um IndexError com a frase: 'A quantidade de elementos em cada lista é diferente.'

   **Dados para testar a função:**

   Valores sem erro:
   ```python
   lista1 = [4,6,7,9,10]
   lista2 = [-4,6,8,7,9]
   ```

   Listas com tamanhos diferentes:
   ```python
   lista1 = [4,6,7,9,10,4]
   lista2 = [-4,6,8,7,9]
   ```

   Listas com valores incoerentes:
   ```python
   lista1 = [4,6,7,9,'A']
   lista2 = [-4,'E',8,7,9]
   ```

### Aplicando a Projetos

5. **Pontuação de Estudantes**
   Desenvolva um código que contabiliza as pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste. O código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.

   Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, lance um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida". O cálculo das 3 notas só será realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes. Se não for lançada a exceção, será exibida uma lista com as notas em cada teste.

   **Dados para o teste do código:**

   Gabarito da prova:
   ```python
   gabarito = ['D', 'A', 'B', 'C', 'A']
   ```

   Notas sem exceção:
   ```python
   testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]
   ```

   Notas com exceção:
   ```python
   testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]
   ```

6. **Verificação de Pontuação em Texto**
   Crie uma função que recebe uma lista com as palavras separadas de uma frase gerada pelo ChatGPT. Avalie cada palavra desse texto e verifique se o tratamento para retirar os símbolos de pontuação (',' '.', '!' e '?') foi realizado. Caso contrário, lance uma exceção do tipo ValueError apontando o primeiro caso em que foi detectado o uso de uma pontuação por meio da frase "O texto apresenta pontuações na palavra '[palavra]'."

   **Dados para o teste do código:**

   Lista tratada:
   ```python
   lista_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa', 'versátil', 'e', 'fácil', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos', 'desde', 'análise', 'de', 'dados', 'até', 'inteligência', 'artificial']
   ```

   Lista não tratada:
   ```python
   lista_nao_tratada = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação', 'poderosa,', 'versátil', 'e', 'fácil,', 'de', 'aprender', 'utilizada', 'em', 'diversos', 'campos,', 'desde', 'análise', 'de', 'dados', 'até', 'inteligência', 'artificial!']
   ```

7. **Divisão de Dados de Experimento**
   Crie uma função `divide_colunas` que recebe os dados das colunas de pressão e temperatura (no formato de listas) e gera uma nova coluna com o resultado da divisão. Verifique se as listas têm o mesmo tamanho (ValueError) e se existe alguma divisão por zero (ZeroDivisionError).

   **Dados para testar a função:**

   Dados sem exceção:
   ```python
   pressoes = [100, 120, 140, 160, 180]
   temperaturas = [20, 25, 30, 35, 40]
   ```

   Dados com exceção:

   1) Exceção de ZeroDivisionError
   ```python
   pressoes = [60, 120, 140, 160, 180]
   temperaturas = [0, 25, 30, 35, 40]
   ```

   2) Exceção de ValueError
   ```python
   pressoes = [100, 120, 140, 160]
   temperaturas = [20, 25, 30, 35, 40]
   ```

---