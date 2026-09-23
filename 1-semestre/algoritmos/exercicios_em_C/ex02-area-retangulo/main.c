// Ex 2 — Área do retângulo
// Lê a base e a altura de um retângulo e exibe sua área.
// Teste de mesa: 8 e 5

#include <stdio.h>

int main(void) {
    int base, altura;
    printf("Entre a base: \n");
    scanf("%d", &base);
    printf("Entre com a altura: \n");
    scanf("%d", &altura);
    printf("A área do retangulo é %i", base * altura);
    return 0;
}
