// Ex 3 — Média
// Lê três notas e exibe a média aritmética entre elas.
// Teste de mesa: 7, 5 e 8

#include <stdio.h>

int main(void) {
    float n1, n2, n3;
    printf("Entre com a nota 1: \n");
    scanf("%f", &n1);
    printf("Entre com a nota 2: \n");
    scanf("%f", &n2);
    printf("Entre com a nota 3: \n");
    scanf("%f", &n3);
    printf("A média é: %.2f", (n1 + n2 + n3) / 3);
    return 0;
}
