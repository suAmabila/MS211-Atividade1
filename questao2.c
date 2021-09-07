#include <stdio.h>
#include <math.h>
#include "raizesDaFuncao.h"

void printResultado(long double raiz, char metodo[30]){
    printf("A raiz, pelo Método %s, é %Lf", metodo, raiz);
    printf("f(x) = %Lf", funcao(raiz));
    printf("\n");
}

int main(){
    // Teste usando Método da Bisseção
    // usei função x ** 3 - 9 * x + 3

    double epsilon1 = pow(10.0, -3.0);
    double raiz = metodoBissecao(0, 1, 10, epsilon1, epsilon1);
    printf("A raiz, pelo Método da Bisseção, é %32.e\n", raiz);
    printf("f(x) = %.32e\n", funcao(raiz));

    // Teste usando Método da Falsa Posição
    // usei função x ** 3 - 9 * x + 3

    epsilon1 = pow(5 * 10, -4);
    raiz = metodoFalsaPosicao(0, 1, 3, epsilon1);
    printf("A raiz, pelo Método da Falsa Posição, é %.32e\n", raiz);
    printf("f(x) = %.32e\n", funcao(raiz));


    // Teste usando Método de Newton
    // usei função x ** 3 - 9 * x + 3

    epsilon1 = pow(10, -4);
    raiz = metodoNewton(0.5, epsilon1, epsilon1);
    printf("A raiz, pelo Método de Newton, é %.32e\n", raiz);
    printf("f(x) = %.32e\n", funcao(raiz));


    // Teste usando Método da Secante
    // usei função x ** 3 - 9 * x + 3

    epsilon1 = pow(5 * 10, -4);
    raiz = metodoSecante(0, 1, epsilon1, epsilon1);
    printf("A raiz, pelo Método da Secante, é %.32e\n", raiz);
    printf("f(x) = %.32e\n", funcao(raiz));
    
    printf("\n");
    return 0;
}