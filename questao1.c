#include <stdio.h>

void teste_precisao_float(int VAL)
{
    float A = 1, s = A + VAL;
    while (s > VAL)
    {
        A = A / 2;
        s = VAL + A;
    }

    float Prec = 2 * A;
    printf("Float = %e\n", Prec);
}

void teste_precisao_double(int VAL)
{
    double A = 1, s = A + VAL;
    while (s > VAL)
    {
        A = A / 2;
        s = VAL + A;
    }

    double Prec = 2 * A;
    printf("Double = %e\n", Prec);
}

void teste_precisao(int VAL)
{
    printf("VAL = %d\n", VAL);
    teste_precisao_float(VAL);
    teste_precisao_double(VAL);
    printf("\n");
}

int main(int argc, char const *argv[])
{
    // VAL = 1
    teste_precisao(1);

    // VAL = 10
    teste_precisao(10);

    // VAL = 17
    teste_precisao(17);

    // VAL = 100
    teste_precisao(100);

    // VAL = 184
    teste_precisao(184);

    // VAL = 1000
    teste_precisao(1000);

    // VAL = 1575
    teste_precisao(1575);

    // VAL = 10000
    teste_precisao(10000);

    // VAL = 17893
    teste_precisao(17893);

    return 0;
}
