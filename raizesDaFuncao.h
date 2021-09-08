double funcao(int opcao, double x);

double derivadaF(int opcao, double x);

double funcaoFi(int opcao, double x);

int sgn(double x);

double metodoBissecao(int opcao, double a, double b, int maxIter, double epsilon1, double epsilon2);
    
double metodoFalsaPosicao(int opcao, double a, double b, int maxIter, double epsilon);
    
double metodoNewton(int opcao, double x_k, double epsilon1, double epsilon2, int *iteracoes);

double metodoSecante(int opcao, double x_1, double x_2, double epsilon1, double epsilon2, int *iteracoes);

double metodoPontoFixo(int opcao, double x_0, double raizD, double epsilon, int *iteracoes);

/*
def ordemConvergencia(x_k, x_n, x_nMais1, epsilon):
    raiz = metodoNewton(x_k, epsilon, epsilon)

    E = abs(raiz - x_n)

    p = log() / log()
*/