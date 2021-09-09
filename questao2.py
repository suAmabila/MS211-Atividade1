from raizesDaFuncao import *
from math import *

def printResultado(opcao, raiz, iteracoes, erro, p, metodo):
    f = funcao(opcao, raiz)

    if opcao == 1:
        print('A raiz, pelo Método', metodo, 'é', raiz)
        print('f(x) = ', f'{f:.4e}')
    elif opcao == 2:
        print('A raiz, pelo Método', metodo, 'é', f'{raiz:.8e}')
        print('f(x) = ', f'{f:.7e}')

    print('Erro na raiz: ', erro)
    print('Ordem de convergência: ', p)
    print('Número de iterações: ', iteracoes)
    print()


epsilon1 = 10 ** -12
epsilon2 = 10 ** -15

epsilon18 = 10 ** -4
epsilon19 = 10 ** -6


raiz = 0
iteracoes = 0
erro = 0
p = 0

raiz, iteracoes, erro, p = metodoBissecao(1, 1, 2, 14, epsilon18, epsilon18)
printResultado(1, round(raiz, 8), iteracoes, erro, p, 'da Bisseção')

raiz, iteracoes, erro, p = metodoFalsaPosicao(1, 1, 2, 6, epsilon18)
printResultado(1, round(raiz, 8), iteracoes, erro, p, 'da Falsa Posição')

raiz, iteracoes, erro, p = metodoPontoFixo(1, 1.5, metodoNewton(1, 1.5, epsilon18, epsilon18)[0], epsilon18)
printResultado(1, round(raiz, 8), iteracoes, erro, p, 'do Ponto Fixo')

raiz, iteracoes, erro, p = metodoNewton(1, 1.5, epsilon18, epsilon18)
printResultado(1, round(raiz, 8), iteracoes, erro, p, 'de Newton')

raiz, iteracoes, erro, p = metodoSecante(1, 1, 2, epsilon18, epsilon18)
printResultado(1, round(raiz, 8), iteracoes, erro, p, 'da Secante')

# EXEMPLO 19
print()

raiz = 0
raiz, iteracoes, erro, p = metodoBissecao(2, 1, 2, 20, epsilon19, epsilon19)
printResultado(2, raiz, iteracoes, erro, p, 'da Bisseção')

raiz, iteracoes, erro, p = metodoFalsaPosicao(2, 1, 2, 17, epsilon19)
printResultado(2, raiz, iteracoes, erro, p, 'da Falsa Posição')

raiz, iteracoes, erro, p = metodoPontoFixo(2, 1, metodoNewton(2, 0, epsilon19, epsilon19)[0], epsilon19)
printResultado(2, raiz, iteracoes, erro, p, 'do Ponto Fixo')

# o erro está muito errado para o método de Newton e da Secante no exemplo 19
raiz, iteracoes, erro, p = metodoNewton(2, 0, epsilon19, epsilon19)
printResultado(2, raiz, iteracoes, erro, p, 'de Newton')

raiz, iteracoes, erro, p = metodoSecante(2, 0, 0.5, epsilon19, epsilon19)
printResultado(2, raiz, iteracoes, erro, p, 'da Secante')
