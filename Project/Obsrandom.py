# Disponibiliza uma função para gerar observações de uma variavel aleatoria
# com distribuicao exponencial
from random import random
from math import log

def exprandom(m):
    x=random()
    return -m*log(x)


