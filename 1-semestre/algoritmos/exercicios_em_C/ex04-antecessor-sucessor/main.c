// Ex 4 — Antecessor e Sucessor
// Lê um número e exibe seu antecessor e seu sucessor.
// Teste de mesa: 10

#include <stdio.h>

int main(void) {
    int n;
    printf("Entre um numero: \n");
    scanf("%i", &n);
    printf("O antecessor é: %i \n", n - 1);
    printf("O sucessor é: %i \n", n + 1);
    return 0;
}
