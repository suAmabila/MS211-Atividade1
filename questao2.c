#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "raizesDaFuncao.h"

void printResultado(int opcao, double raiz, char metodo[30], int iteracoes){
    printf("A raiz, pelo Método %s, é %e\n", metodo, raiz);
    printf("f(x) = %e\n", funcao(opcao, raiz));
    printf("Número de iterações: %d\n", iteracoes);
    printf("\n");
}

int main(){
    // Teste usando Método da Bisseção

    double epsilon1 = 0;
    double raiz = 0;
    int *iteracoes;

    iteracoes = malloc(sizeof(int));

    *iteracoes = 0;

    epsilon1 = pow(10.0, (-1 * 6));
    raiz = metodoBissecao(2, 1, 2, 20, epsilon1, epsilon1);
    printResultado(2, raiz, "da Bisseção", 20);

    // Teste usando Método da Falsa Posição

    raiz = metodoFalsaPosicao(2, 1, 2, 17, epsilon1);
    printResultado(2, raiz, "da Falsa Posição", 17);

    double raiz2 = metodoPontoFixo(2, 1, raiz, epsilon1, iteracoes);
    printResultado(2, raiz2, "do Ponto Fixo", *iteracoes);

    // Teste usando Método de Newton

    raiz = metodoNewton(2, 0, epsilon1, epsilon1, iteracoes);
    printResultado(2, raiz, "de Newton", *iteracoes);

    // Teste usando Método da Secante

    raiz = metodoSecante(2, 0, 0.5, epsilon1, epsilon1, iteracoes);
    printResultado(2, raiz, "da Secante", *iteracoes);

    free(iteracoes);
    
    printf("\n");
    return 0;
}