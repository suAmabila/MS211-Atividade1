#include <stdio.h>
#include <math.h>
#include "raizesDaFuncao.h"

/*
def defFuncDeri(f, d):
    global functionF
    global derivada

    functionF = f
    derivada = d
*/

double funcao(double x){
    return 1.0;
    //return functionF(x);
    //return x ** 3 - 9 * x + 3
}

double derivadaF(double x){
    return 1.0;
    //return derivada(x);
    //return 3 * x ** 2 - 9
}

int sgn(double x){
    if(x > 0){
        return 1;
    }else if(x < 0){
        return -1;
    } else if(x == 0){
        return 0;
    }
}

// certo
double metodoBissecao(double a, double b, int maxIter, double epsilon1, double epsilon2){
    int i = 0;
    double raiz = 0;
    while(i < maxIter){
        double x = (a + b) / 2;
        if(funcao(x) == 0){
            printf("%.32e é a raiz da função\n", x);
            raiz = x;
            return raiz;
        } else{ 
            if ((sgn(funcao(a)) * sgn(funcao(x))) < 0){
                b = x;
            } else if ((sgn(funcao(x)) * sgn(funcao(b))) < 0){
                a = x;
            }
        }

        if (fabs(b - a) < epsilon1 || fabs(funcao(x)) < epsilon2){
            raiz = x;
            break;
        }
        
        raiz = x;
        i += 1;
    }
    return raiz;
}

// certo
double metodoFalsaPosicao(double a, double b, int maxIter, double epsilon){
    int i = 0;
    double raiz = 0;

    while(i < maxIter){
        double x = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a));
        
        if(fabs(x - a) < epsilon || fabs(b - x) < epsilon){
            raiz = x;
            break;
        }
        if(funcao(x) == 0){
            raiz = x;
            return raiz;
        } else{
            if((sgn(funcao(a)) * sgn(funcao(x))) < 0){
                b = x;
            } else if((sgn(funcao(x)) * sgn(funcao(b))) < 0){
                a = x;
            }
        }

        raiz = x;
        i += 1;
    }
    return raiz;
}

// certo
double metodoNewton(double x_k, double epsilon1, double epsilon2){
    double raiz = x_k;

    while(1){
        x_k = raiz;
        double x = x_k - (funcao(x_k))/(derivadaF(x_k));
        
        if(fabs(x - x_k) < epsilon1 || fabs(funcao(x)) < epsilon2){
            raiz = x;
            return raiz;
        }
        raiz = x;
    }
}

// certo
double metodoSecante(double x_1, double x_2, double epsilon1, double epsilon2){
    //k = x_2
    //k - 1 = x_1
    //k + 1 = x

    double raiz = 0;
    double x = 0;

    while(1){ 
        double x = (x_1 * funcao(x_2) - x_2 * funcao(x_1)) / (funcao(x_2) - funcao(x_1));
        if(fabs(x - x_2) < epsilon1 || fabs(funcao(x)) < epsilon2){
            raiz = x;
            return raiz;
        }
        raiz = x;
        x_1 = x_2;
        x_2 = x;
    }
}

double metodoPontoFixo(double x_0, double epsilon){
    printf("\n");
}

/*
def ordemConvergencia(x_k, x_n, x_nMais1, epsilon):
    raiz = metodoNewton(x_k, epsilon, epsilon)

    E = abs(raiz - x_n)

    p = log() / log()
*/