// Ex 18 — Soma dos positivos entre 4 números (enquanto)
// Faça um algoritmo que receba a entrada de 4 números digitados pelo usuário,
// verifique em cada entrada se o número digitado é positivo (maior que 0),
// caso seja deverá realizar a soma desses números para que seja exibido o
// resultado no final da execução do algoritmo.

#include <stdio.h>

int main(void) {
    int numero, soma = 0, contador = 0;
    while (contador < 4) {
        printf("Digite um número: ");
        scanf("%d", &numero);
        if (numero > 0) {
            soma += numero;
        }
        contador++;
    }
    printf("Soma dos números positivos: %d\n", soma);
    return 0;
}   