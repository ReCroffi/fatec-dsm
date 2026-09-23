// Ex 10 — Positivo, negativo ou zero
// Lê um número e exibe se ele é positivo, negativo ou igual a zero.
// Teste de mesa: 5, -3 e 0

#include <stdio.h>

int main(void) {
    int n;
    printf("Entre um número: \n");
    scanf("%d", &n);
    if (n > 0) {
        printf("Esse número é positivo");
    } else if (n < 0) {
        printf("Esse número é negativo");
    } else {
        printf("Esse numero é zero");
    }
    return 0;
}
    