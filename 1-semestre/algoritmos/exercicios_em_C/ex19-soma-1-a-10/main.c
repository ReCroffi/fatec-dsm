// Ex 19 — Soma de 1 até 10 (enquanto)
// Faça um algoritmo que, utilizando a estrutura de repetição While (enquanto),
// some os números de 1 até 10 e no final mostre o resultado.

#include <stdio.h>

int main(void) {
    int numero = 1, soma = 0;
    while (numero <= 10) {
        soma += numero;
        numero++;
    }
    printf("Soma dos números de 1 até 10: %d\n", soma);

    return 0;
}
