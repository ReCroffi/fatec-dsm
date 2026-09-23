// Ex 1 — Soma, Subtração, Multiplicação e Divisão
// Lê dois números e exibe a soma, a subtração, a multiplicação e a divisão entre eles.
// Teste de mesa: 20 e 4

#include <stdio.h>

int main(void) {
    int a, b;
    printf("Entre um valor: \n");
    scanf("%d", &a);
    printf("Entre o segundo valor: \n");
    scanf("%d", &b);
    printf("Soma: %i \n", a + b);
    printf("Subtração: %i \n", a - b);
    printf("Multiplicação: %i \n", a * b);
    printf("Divisão: %.2f", (float)a / b);
    return 0;
}
