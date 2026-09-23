// Ex 12 — Maior de idade
// Lê a idade de uma pessoa e exibe se ela é maior ou menor de idade (limite: 18 anos).
// Teste de mesa: 17, 18 e 19

#include <stdio.h>

int main(void) {
    int idade;
    printf("Entre a idade: \n");
    scanf("%i", &idade);
    if (idade >= 18) {
        printf("Maior de idade");
    } else {
        printf("Menor de idade");
    }

    return 0;
}
