from raizesDaFuncao import defFuncDeri, funcao, metodoBissecao, metodoFalsaPosicao, metodoNewton, metodoSecante
from math import *

def printResultado(raiz, metodo):
    print('A raiz, pelo Método', metodo, 'é', raiz)
    print('f(x) = ', funcao(raiz))
    print()

epsilon1 = 10 ** -12
epsilon2 = 10 ** -15

epsilon18 = 10 ** -4
epsilon19 = 10 ** -6

f1 = lambda x: (e ** (-x ** 2)) - cos(x)
derivadaF1 = lambda x: ((- 2 * x) + (e ** (x ** 2)) * sin(x)) / (e ** (x ** 2))
fPontoFixo1 = lambda x: cos(x) - e ** (-x ** 2) + x

raiz = 0
defFuncDeri(f1, derivadaF1)
raiz = metodoBissecao(1, 2, 14, epsilon18, epsilon18)
printResultado(raiz, 'da Bisseção')

raiz = metodoFalsaPosicao(1, 2, 6, epsilon18)
printResultado(raiz, 'da Falsa Posição')

# Falta o Método do Ponto Fixo

raiz = metodoNewton(1.5, epsilon18, epsilon18)
printResultado(raiz, 'de Newton')

raiz = metodoSecante(1, 2, epsilon18, epsilon18)
printResultado(raiz, 'da Secante')

# EXEMPLO 19
print()

f2 = lambda x: x ** 3 - x - 1
derivadaF2 = lambda x: 3 * (x ** 2) - 1
fPontoFixo2 = lambda x: (x + 1) ** (1 / 3)

raiz = 0
defFuncDeri(f2, derivadaF2)
raiz = metodoBissecao(1, 2, 20, epsilon19, epsilon19)
printResultado(raiz, 'da Bisseção')

raiz = metodoFalsaPosicao(1, 2, 17, epsilon19)
printResultado(raiz, 'da Falsa Posição')

# Falta o Método do Ponto Fixo

raiz = metodoNewton(0, epsilon19, epsilon19)
printResultado(raiz, 'de Newton')

raiz = metodoSecante(0, 0.5, epsilon19, epsilon19)
printResultado(raiz, 'da Secante')
