// Ex 7 — Área do trapézio
// Lê a base maior, a base menor e a altura de um trapézio e exibe sua área.
// Teste de mesa: 10, 6 e 4

#include <stdio.h>

int main(void) {
    int base_men, base_maior, h, area;
    printf("Entre com a base menor: ");
    scanf("%d", &base_men);
    printf("Entre com a base maior: ");
    scanf("%d", &base_maior);
    printf("Entre com a aultura: ");
    scanf("%d", &h);
    area = ((base_men + base_maior) * h) / 2;
    printf("A área do trapézio é: %i", area);
    return 0;
}
