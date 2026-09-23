// Ex 9 — Média + aprovação
// Lê duas notas, calcula a média e exibe se o aluno foi aprovado (média >= 6) ou
// reprovado. Teste de mesa: 7 e 5

#include <stdio.h>

int main(void) {
    float n1, n2, media;
    printf("Entre n1: \n");
    scanf("%f", &n1);
    printf("Entre n2: \n");
    scanf("%f", &n2);
    media = (n1 + n2) / 2;
    if (media >= 6) {
        printf("Aluno aprovado com média: %.2f", media);
    } else {
        printf("Aluno reprovado com media: %.2f", media);
    }
    return 0;
}
