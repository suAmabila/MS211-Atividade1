from math import *

global functionF
global derivada

def defFuncDeri(f, d):
    global functionF
    global derivada

    functionF = f
    derivada = d

def funcao(x):
    return functionF(x)
    #return x ** 3 - 9 * x + 3

def derivadaF(x):
    return derivada(x)
    #return 3 * x ** 2 - 9

def sgn(x):
    if x > 0:
        return 1;
    elif x < 0:
        return -1;
    elif x == 0:
        return 0

# certo
def metodoBissecao(a, b, maxIter, epsilon1, epsilon2):
    i = 0
    raiz = 0
    while i < maxIter:
        x = (a + b) / 2
        if funcao(x) == 0:
            print(x, 'é a raiz da função')
            raiz = x
            return raiz
        else: 
            if (sgn(funcao(a)) * sgn(funcao(x))) < 0:
                a, b = a, x
            elif (sgn(funcao(x)) * sgn(funcao(b))) < 0:
                a, b = x, b

        if abs(b - a) < epsilon1 or abs(funcao(x)) < epsilon2:
            raiz = x
            break
        
        raiz = x
        i += 1
    
    return raiz

# certo
def metodoFalsaPosicao(a, b, maxIter, epsilon):
    i = 0
    raiz = 0
    while i < maxIter:
        x = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))
        
        if abs(x - a) < epsilon or abs(b - x) < epsilon:
            raiz = x;
            break;

        if funcao(x) == 0:
            raiz = x
            return raiz
        else:
            if (sgn(funcao(a)) * sgn(funcao(x))) < 0:
                a,b = a, x 
            elif (sgn(funcao(x)) * sgn(funcao(b))) < 0:
                a, b = x, b

        raiz = x
        i += 1
    
    return raiz

# certo
def metodoNewton(x_k, epsilon1, epsilon2):
    raiz = x_k

    while True:
        x_k = raiz
        x = x_k - (funcao(x_k))/(derivadaF(x_k))
        
        if abs(x - x_k) < epsilon1 or abs(funcao(x)) < epsilon2:
            raiz = x
            return raiz

        raiz = x

# certo
def metodoSecante(x_1, x_2, epsilon1, epsilon2):
    # k = x_2
    # k - 1 = x_1
    # k + 1 = x

    raiz = 0
    x = 0

    while True: 
        x = (x_1 * funcao(x_2) - x_2 * funcao(x_1)) / (funcao(x_2) - funcao(x_1))
        if abs(x - x_2) < epsilon1 or abs(funcao(x)) < epsilon2:
            raiz = x
            return raiz
        raiz = x
        x_1 = x_2
        x_2 = x

def metodoPontoFixo(funcao, x_0, epsilon):
    print()

def ordemConvergencia(x_k, x_n, x_nMais1, epsilon):
    raiz = metodoNewton(x_k, epsilon, epsilon)

    E = abs(raiz - x_n)

    p = log() / log()

# Teste usando Método da Bisseção
# usei função x ** 3 - 9 * x + 3
'''
epsilon1 = 10 ** -3
raiz = metodoBissecao(0, 1, 10, epsilon1, epsilon1)
print('A raiz, pelo Método da Bisseção, é', raiz)
print('f(x) = ', funcao(raiz))
'''

# Teste usando Método da Falsa Posição
# usei função x ** 3 - 9 * x + 3
'''
epsilon1 = 5 * 10 ** -4
raiz = metodoFalsaPosicao(0, 1, 3, epsilon1)
print('A raiz, pelo Método da Falsa Posição, é', raiz)
print('f(x) = ', funcao(raiz))
'''

# Teste usando Método de Newton
# usei função x ** 3 - 9 * x + 3
'''
epsilon1 = 1 * 10 ** -4
raiz = metodoNewton(0.5, epsilon1, epsilon1)
print('A raiz, pelo Método de Newton, é', raiz)
print('f(x) = ', funcao(raiz))
'''

# Teste usando Método da Secante
# usei função x ** 3 - 9 * x + 3

'''
epsilon1 = 5 * 10 ** -4
raiz = metodoSecante(0, 1, epsilon1, epsilon1)
print('A raiz, pelo Método da Secante, é', raiz)
print('f(x) = ', funcao(raiz))
'''
