import matplotlib  # Importa toda a biblioteca, situacional, pois gasta muito da memória colocando todos os metodos/funções da biblioteca.
import matplotlib.pyplot as plt # Importa um metodo com um nome diferente, metplotlib fica nomeado com plt por conta do as, mais utilizavel, pois gasta menos da memória e facilita o entendimento do código
from random import choice # Importa um metodo específico, de uma biblioteca, facilitando entendimento e ajuda economizando memória
from random import randrange, sample # Importa alguns metodos da biblioteca, assim seria se necessitasse de mais de um metodo
from random import * # Importa todos os metodos, cai na mesma intenção do primeiro tópico, gasta memória
from math import sqrt as test # Importa um metodo específico colocando um nome diferente do metodo, situacional, ajuda bastante, pois você pode entra em conflito com imports de outras biblioteca