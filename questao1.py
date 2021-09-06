from decimal import Decimal

# Precisão Simples (float)
'''
A = 1
s = 2

while s > 1:
    A = A / 2
    s = 1 + A

Prec = 2 * A
print('Precisão: ', Prec)
'''

# Precisão Dupla (Decimal)
'''
A = Decimal(1)
s = Decimal(2)

while s > 1:
    A = A / 2
    s = 1 + A

Prec = Decimal(2 * A)
print('Precisão: ', Prec)
'''

# Item c
numIteracoes = 0
val = 1

# esse while é para testar os valores de c.1)
while val != 0:
    A = 1
    val = float(input('Digite um número: '))
    s = val + A

    while s > val:
        A = A / 2
        s = val + A
        numIteracoes += 1

    Prec = 2 * A
    print('Precisão: ', Prec, '\nNúmero de Iterações: ', numIteracoes, '\n')

