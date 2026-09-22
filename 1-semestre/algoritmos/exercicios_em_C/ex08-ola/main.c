// Ex 8 — Olá
// Lê o nome da pessoa e exibe uma saudação com esse nome.
// Teste de mesa: um nome qualquer

#include <stdio.h>

int main(void) {
    char nome[12];
    printf("Entre seu nome: \n");
    scanf("%s", nome);
    printf("Olá, %s", nome);

    return 0;
}
