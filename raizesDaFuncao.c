#include <stdio.h>
#include <math.h>
#include "raizesDaFuncao.h"

double funcao(int opcao, double x){
    double num = 0;
    if(opcao == 1){
        double expo = pow((-1 * x), 2);
        num = exp(expo) - cos(x);
        return num;
    } else if(opcao == 2){
        num = (pow(x, 3)) - x - 1;
        return num;
    }
}

double derivada(int opcao, double x){
    if(opcao == 1){
        return ((-1 * 2) * x + exp(pow(x, 2)) * sin(x)) / (exp(pow(x, 2)));
    } else if(opcao == 2){
        return 3 * pow(x, 2) - 1;
    }
}

double funcaoFi(int opcao, double x){
    if(opcao == 1){
        return cos(x) - exp(pow((-1 * x), 2)) + x;
    } else if(opcao == 2){
        return pow((x + 1), (1 / 3));
    }
}

int sgn(double x){
    if(x > 0){
        return 1;
    } else if(x < 0){
        return -1;
    } else if(x == 0){
        return 0;
    }
}

// certo
double metodoBissecao(int opcao, double a, double b, int maxIter, double epsilon1, double epsilon2){
    int i = 0;
    double raiz = 0;
    while(i < maxIter){
        double x = (a + b) / 2;
        if(funcao(opcao, x) == 0){
            printf("%.32e é a raiz da função\n", x);
            raiz = x;
            return raiz;
        } else{ 
            if (sgn(funcao(opcao, a)) * sgn(funcao(opcao, x)) < 0){
                b = x;
            /*} else if ((sgn(funcao(opcao, x)) * sgn(funcao(opcao, b))) < 0){
                a = x;
            }*/
            } else {
                a = x;
            }
        }

        if (fabs(b - a) < epsilon1 || fabs(funcao(opcao, x)) < epsilon2){
            raiz = x;
            break;
        }
        
        raiz = x;
        i += 1;
    }
    return raiz;
}

// certo
double metodoFalsaPosicao(int opcao, double a, double b, int maxIter, double epsilon){
    int i = 0;
    double raiz = 0;

    while(i < maxIter){
        double x = (a * funcao(opcao, b) - b * funcao(opcao, a)) / (funcao(opcao, b) - funcao(opcao, a));
        
        if(fabs(x - a) < epsilon || fabs(b - x) < epsilon){
            raiz = x;
            break;
        }
        if(funcao(opcao, x) == 0){
            raiz = x;
            return raiz;
        } else{
            if((sgn(funcao(opcao, a)) * sgn(funcao(opcao, x))) < 0){
                b = x;
            } else if((sgn(funcao(opcao, x)) * sgn(funcao(opcao, b))) < 0){
                a = x;
            }
        }

        raiz = x;
        i += 1;
    }
    return raiz;
}

// certo
double metodoNewton(int opcao, double x_k, double epsilon1, double epsilon2, int *iteracoes){
    double raiz = x_k;
    int entrou = 0;
    *iteracoes = 0;

    while(entrou != 1){
        x_k = raiz;
        double x = x_k - (funcao(opcao, x_k))/(derivada(opcao, x_k));
        
        if(fabs(x - x_k) < epsilon1 || fabs(funcao(opcao, x)) < epsilon2){
            //raiz = x;
            // return raiz
            entrou = 1;
        }
        raiz = x;
        (*iteracoes)++;
    }
    return raiz;
}

// certo
double metodoSecante(int opcao, double x_1, double x_2, double epsilon1, double epsilon2, int *iteracoes){
    //k = x_2
    //k - 1 = x_1
    //k + 1 = x

    double raiz = 0;
    double x = 0;

    while(1){ 
        double x = (x_1 * funcao(opcao, x_2) - x_2 * funcao(opcao, x_1)) / (funcao(opcao, x_2) - funcao(opcao, x_1));
        if(fabs(x - x_2) < epsilon1 || fabs(funcao(opcao, x)) < epsilon2){
            raiz = x;
            return raiz;
        }
        raiz = x;
        x_1 = x_2;
        x_2 = x;
        (*iteracoes)++;
    }
}

double metodoPontoFixo(int opcao, double x_0, double raizD, double epsilon, int *iteracoes){
    double x_1 = 0;
    while(x_1 != raizD){
        x_1 = funcaoFi(opcao, x_0);

        if(fabs(x_1 - x_0) < epsilon || fabs(funcao(opcao, x_1)) < epsilon){
            return x_1;
        }

        x_0 = x_1;
        (*iteracoes)++;
    }
    return x_1;
}

/*
def ordemConvergencia(x_k, x_n, x_nMais1, epsilon):
    raiz = metodoNewton(x_k, epsilon, epsilon)

    E = abs(raiz - x_n)

    p = log() / log()
*/