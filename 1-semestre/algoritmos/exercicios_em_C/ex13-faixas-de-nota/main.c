// Ex 13 — Faixas de nota
// Lê uma nota e exibe se ela é igual, abaixo ou acima da média (média = 6).
// Teste de mesa: 4, 6 e 8 — uma por faixa

#include <stdio.h>

int main(void) {
    int nota;
    printf("Leia a nota: \n");
    scanf("%d", &nota);
    if (nota > 6) {
        printf("Acima da média");
    } else if (nota < 6) {
        printf("Abaixo da media");
    } else {
        printf("Na media");
    }

    return 0;
}
