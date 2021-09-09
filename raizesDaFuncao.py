from math import *

def funcao(opcao, x):
    if opcao == 1:
        return (e ** (-x ** 2)) - cos(x)
    elif opcao == 2:
        return (x ** 3) - x - 1

def derivada(opcao, x):
    if opcao == 1:
        return ((- 2 * x) + (e ** (x ** 2)) * sin(x)) / (e ** (x ** 2))
    elif opcao == 2:
        return 3 * (x ** 2) - 1

def funcaoFi(opcao, x):
    if opcao == 1:
        return cos(x) - e ** (-x ** 2) + x
    elif opcao == 2:
        return (x + 1) ** (1 / 3)

def sgn(x):
    if x > 0:
        return 1;
    elif x < 0:
        return -1;
    elif x == 0:
        return 0

# certo
def metodoBissecao(opcao, a, b, maxIter, epsilon1, epsilon2):
    i = 0
    raiz = 0
    iteracoes = 0
    p = 0

    x_0 = 0
    x_1 = 0
    x_2 = 0

    while i < maxIter:
        iteracoes += 1
        x_0 = x_1
        x_1 = x_2
        x_2 = (a + b) / 2

        if (abs(b - a) < epsilon1 or abs(funcao(opcao, x_2)) < epsilon2) and i == maxIter:
            raiz = x_2
            break
        
        if (sgn(funcao(opcao, a)) * sgn(funcao(opcao, x_2))) < 0:
            a, b = a, x_2
        elif (sgn(funcao(opcao, x_2)) * sgn(funcao(opcao, b))) < 0:
            a, b = x_2, b
        
        raiz = x_2
        i += 1
    
    erro = abs(b - a)
    p = ordemConvergencia(opcao, x_0, x_1, x_2)
    
    return raiz, iteracoes, erro, p

# certo
def metodoFalsaPosicao(opcao, a, b, maxIter, epsilon):
    i = 0
    raiz = 0
    iteracoes = 0
    p = 0

    x_0 = 0
    x_1 = 0
    x_2 = 0

    while i < maxIter:
        iteracoes += 1
        x_0 = x_1
        x_1 = x_2
        x_2 = (a * funcao(opcao, b) - b * funcao(opcao, a)) / (funcao(opcao, b) - funcao(opcao, a))

        #if x_0 != 0 and x_1 != 0 and x_2 != 0:
            #p = ordemConvergencia(opcao, x_0, x_1, x_2)
        
        if abs(x_2 - a) < epsilon or abs(b - x_2) < epsilon:
            raiz = x_2;
            break;

        if funcao(opcao, x_2) == 0:
            raiz = x_2
            return raiz
        else:
            if (sgn(funcao(opcao, a)) * sgn(funcao(opcao, x_2))) < 0:
                a,b = a, x_2 
            elif (sgn(funcao(opcao, x_2)) * sgn(funcao(opcao, b))) < 0:
                a, b = x_2, b

        raiz = x_2
        i += 1
    
    erro = abs(b-a)
    p = ordemConvergencia(opcao, x_0, x_1, x_2)
    return raiz, iteracoes, erro, p

def metodoPontoFixo(opcao, x_0, raizD, epsilon):
    x_1 = 0
    x_2 = 0
    iteracoes = 0
    erro = 0
    p = 0

    while x_2 != raizD:
        iteracoes += 1
        x_0 = x_1
        x_2 = funcaoFi(opcao, x_1)

        if abs(x_2 - x_1) < epsilon or abs(funcao(opcao, x_2)) < epsilon:
            return x_2, iteracoes

        erro = abs(x_2 - x_1)

        #if x_0 != 0 and x_1 != 0 and x_2 != 0:
            #p = ordemConvergencia(opcao, x_0, x_1, x_2)

        x_1 = x_2

    p = ordemConvergencia(opcao, x_0, x_1, x_2)
    return x_2, iteracoes, erro, p

def metodoNewton(opcao, x_k, epsilon1, epsilon2):
    raiz = x_k
    iteracoes = 0
    erro = 0
    p = 0

    x_0 = 0
    x_1 = 0
    x_2 = 0

    while True:
        iteracoes += 1
        
        x_0 = x_1
        x_1 = x_2

        x_k = raiz
        x_2 = x_k - (funcao(opcao, x_k))/(derivada(opcao, x_k))

        erro = abs(x_2 - x_k)
        #if x_0 != 0 and x_1 != 0 and x_2 != 0:
            #p = ordemConvergencia(opcao, x_0, x_1, x_2)
        
        if abs(x_2 - x_k) < epsilon1 or abs(funcao(opcao, x_2)) < epsilon2:
            raiz = x_2
            p = ordemConvergencia(opcao, x_0, x_1, x_2)
            return raiz, iteracoes, erro, p

        raiz = x_2

def metodoSecante(opcao, x_1, x_2, epsilon1, epsilon2):
    # k = x_2
    # k - 1 = x_1
    # k + 1 = x

    raiz = 0
    iteracoes = 0
    erro = 0
    p = 0

    x_0 = 0
    x_11 = 0
    x_22 = 0

    while True:
        iteracoes += 1
        x_0 = x_11
        x_11 = x_22 
        x_22 = (x_1 * funcao(opcao, x_2) - x_2 * funcao(opcao, x_1)) / (funcao(opcao, x_2) - funcao(opcao, x_1))

        erro = abs(x_22 - x_2)
        #if x_0 != 0 and x_11 != 0 and x_22 != 0:
            #p = ordemConvergencia(opcao, x_0, x_1, x_2)

        if abs(x_22 - x_2) < epsilon1 or abs(funcao(opcao, x_22)) < epsilon2:
            raiz = x_22
            p = ordemConvergencia(opcao, x_0, x_11, x_22)
            return raiz, iteracoes, erro, p
        raiz = x_2
        x_1 = x_2
        x_2 = x_2

def ordemConvergencia(opcao, x_0, x_1, x_2):
    # x_0 = x_n-1
    # x_1 = x_n
    # x_2 = x_n+1
    epsilon = 10 ** -15
    alfa = metodoNewton(opcao, x_2, epsilon, epsilon)[0]
    print('Alfa', alfa)

    e_0 = abs(alfa - x_0)
    e_1 = abs(alfa - x_1)
    e_2 = abs(alfa - x_2)

    p = log(e_2 / e_1) / log(e_1 / e_0)

    return p

