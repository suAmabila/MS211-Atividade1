main: main.o raizesDaFuncao.o
	gcc -g -lm main.o raizesDaFuncao.o -o main
main.o: questao2.c raizesDaFuncao.h
	gcc -g -lm -c questao2.c -o main.o
raizesDaFuncao.o: raizesDaFuncao.c raizesDaFuncao.h
	gcc -g -lm -c raizesDaFuncao.c
clean:
	rm -rf *.o
mrproper: clean
	rm -rf main