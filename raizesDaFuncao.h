double funcao(double x);

double derivadaF(double x);

int sgn(double x);

double metodoBissecao(double a, double b, int maxIter, double epsilon1, double epsilon2);
    
double metodoFalsaPosicao(double a, double b, int maxIter, double epsilon);
    
double metodoNewton(double x_k, double epsilon1, double epsilon2);

double metodoSecante(double x_1, double x_2, double epsilon1, double epsilon2);

double metodoPontoFixo(double x_0, double epsilon);

/*
def ordemConvergencia(x_k, x_n, x_nMais1, epsilon):
    raiz = metodoNewton(x_k, epsilon, epsilon)

    E = abs(raiz - x_n)

    p = log() / log()
*/