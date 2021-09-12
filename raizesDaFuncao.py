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
    erro = 0
    p = 0

    x_0 = 0
    x_00 = 0
    x = 0

    while i < maxIter:
        if abs(b - a) < epsilon1:
            raiz = (b + a) / 2
            break
        else:
            iteracoes += 1
            x_0 = x_00
            x_00 = x
            x = (a + b) / 2

            if funcao(opcao, a) * funcao(opcao, x) > 0:
                a = x
            else:
                b = x
            
            i += 1
    
    if raiz == 0:
        raiz = x
    
    erro = abs(b - a)
    
    if x_0 != 0 and x_00 != 0 and x != 0:
       p = ordemConvergencia(opcao, x_0, x_00, x)
    
    return raiz, iteracoes, erro, abs(p)

# certo
def metodoFalsaPosicao(opcao, a, b, maxIter, epsilon):
    i = 0
    raiz = 0
    iteracoes = 0
    erro = 0
    p = 0

    x_0 = 0
    x_00 = 0
    x = 0

    while i < maxIter:
        
        if abs(b - a) < epsilon:
            raiz = (b + a) / 2
            break
        
        if abs(funcao(opcao, a)) < epsilon:
            raiz = a
            break
        elif abs(funcao(opcao, b)) < epsilon:
            raiz = b
            break
        else:
            iteracoes += 1
            x_0 = x_00
            x_00 = x
            x = (a * funcao(opcao, b) - b * funcao(opcao, a)) / (funcao(opcao, b) - funcao(opcao, a))

            if funcao(opcao, a) * funcao(opcao, x) > 0:
                a = x
            else:
                b = x

        i += 1
    
    if raiz == 0:
        raiz = x

    erro = abs(b-a)
    if x_0 != 0 and x_00 != 0 and x != 0:
       p = ordemConvergencia(opcao, x_0, x_00, x)
    
    return raiz, iteracoes, erro, abs(p)

def metodoPontoFixo(opcao, x_0, epsilon):
    raiz = 0
    iteracoes = 0
    erro = 0
    p = 0

    x_00 = 0
    x_000 = 0
    x = 0

    while True:
        if abs(funcao(opcao, x_0)) < epsilon:
            raiz = x_0
            break
        else: 
            iteracoes += 1
            x_00 = x_000
            x_000 = x
            x = funcaoFi(opcao, x_0)

            if abs(x - x_0) < epsilon:
                raiz = x
                break
            
            x_0 = x
    
    if raiz == 0:
        raiz = x

    erro = abs(x - x_000)
    if x_00 != 0 and x_000 != 0 and x != 0:
       p = ordemConvergencia(opcao, x_00, x_000, x)
    
    return raiz, iteracoes, erro, abs(p)

def metodoNewton(opcao, x_k, epsilon1, epsilon2, paraP):
    raiz = 0
    iteracoes = 0
    erro = 0
    p = 0

    x_0 = 0
    x_00 = 0
    x = 0

    while True:
        if abs(funcao(opcao, x_k)) < epsilon1:
            raiz = x_k
            break
        else:
            iteracoes += 1
            x_0 = x_00
            x_00 = x
            x = x_k - (funcao(opcao, x_k))/(derivada(opcao, x_k))
            
            if abs(x - x_k) < epsilon2:
                raiz = x
                break
            else:
                x_k = x 
        
    if raiz == 0:
        raiz = x
    
    erro = abs(x - x_00)

    #if x_0 != 0 and x_00 != 0 and x != 0:
    if paraP == 0:
        p = ordemConvergencia(opcao, x_0, x_00, x)

    return raiz, iteracoes, erro, p

        

def metodoSecante(opcao, x_1, x_2, epsilon1, epsilon2):
    raiz = 0
    iteracoes = 0
    erro = 0
    p = 0

    x_0 = 0
    x_00 = 0
    x = 0

    while True:
        if abs(funcao(opcao, x_2)) < epsilon1:
            raiz = x_2
            break
        else:
            iteracoes += 1
            x_0 = x_00
            x_00 = x
            x = (x_1 * funcao(opcao, x_2) - x_2 * funcao(opcao, x_1)) / (funcao(opcao, x_2) - funcao(opcao, x_1))

            if abs(x - x_2) < epsilon2:
                raiz = x
                break
            
            x_1 = x_2
            x_2 = x
    
    if raiz == 0:
        raiz = x
    
    erro = abs(x - x_00)

    if x_0 != 0 and x_00 != 0 and x != 0:
        p = ordemConvergencia(opcao, x_0, x_00, x)

    return raiz, iteracoes, erro, p

def ordemConvergencia(opcao, x_0, x_00, x):
    # x_0 = x_n-1
    # x_00 = x_n
    # x = x_n+1
    epsilon = 10 ** -15
    alfa = metodoNewton(opcao, 1.5, epsilon, epsilon, 1)[0]
    #print('Alfa', alfa)

    e_0 = abs(alfa - x_0)
    e_00 = abs(alfa - x_00)
    e = abs(alfa - x)

    p = log(e / e_00) / log(e_00 / e_0)

    return p


