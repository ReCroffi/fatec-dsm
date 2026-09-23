// Ex 11 — Maior ou menor
// Lê dois números e exibe se são iguais, ou qual deles é o maior e qual é o menor.
// Teste de mesa: 8 e 3, 3 e 8, 4 e 4

#include <stdio.h>

int main(void) {
    int n1, n2;
    printf("Entre n1: \n");
    scanf("%d", &n1);
    printf("Entre n2: \n");
    scanf("%d", &n2);
    if (n1 > n2) {
        printf("%i é maior que %i", n1, n2);
    } else if (n1 < n2) {
        printf("%i é menor que %i", n1, n2);
    } else {
        printf("%i é igual %i", n1, n2);
    }

    return 0;
}
