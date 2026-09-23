// Ex 14 — Aprovação
// Lê a nota e a frequência de um aluno e exibe se ele foi aprovado
// (nota >= 6 e frequência >= 75) ou reprovado.
// Teste de mesa: 7/80, 7/50, 5/80, 5/50

#include <stdio.h>

int main(void) {
    int freq;
    float nota;
    printf("Entre a nota: \n");
    scanf("%f", &nota);
    printf("Entre a frequencia: \n");
    scanf("%d", &freq);
    if (nota >= 6 && freq >= 75) {
        printf("Aprovado");
    } else {
        printf("Reprovado");
    }
    return 0;
}
