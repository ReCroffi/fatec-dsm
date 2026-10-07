// Ex 21 — Contar positivos, negativos e zeros entre 6 números (enquanto)
// Faça um algoritmo que receba a entrada de 6 números digitados pelo usuário,
// o algoritmo deverá verificar se cada número inserido é positivo, negativo ou
// zero, deverá também registrar em contadores as quantidades de positivos,
// negativos e zeros inseridos para no fim informar o usuário dessas contagens.

#include <stdio.h>

int main(void) {
    int num, cont, cont_pos, cont_zero, cont_neg;
    while (cont < 6) {
        printf("Entre um numero: \n");
        scanf("%i", &num);
        if (num < 0) {
            cont_neg++;
        } else if (num > 0) {
            cont_pos++;
        } else {
            cont_zero++;
        }
        cont++;
    }
    printf("Foram inseridos %d positivos, %d negativos e %d zeros", cont_pos, cont_neg,
           cont_zero);

    return 0;
}
