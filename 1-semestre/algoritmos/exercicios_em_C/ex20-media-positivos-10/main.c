// Ex 20 — Média dos positivos entre 10 números (enquanto)
// Faça um algoritmo que, utilizando o While (enquanto), leia 10 números que
// serão digitados pelo usuário, verifique em cada um se é um número positivo,
// sendo o número positivo deverá ser somado a uma variável para que no final o
// algoritmo faça a média dessa soma levando em consideração somente a
// quantidade de números positivos digitados.

#include <stdio.h>

int main(void) {
    int numero, soma, cont_num = 0, cont = 0;
    float media;
    while (cont < 10) {
        printf("Digite um número: \n");
        scanf("%d", &numero);
        if (numero > 0) {
            soma += numero;
            cont_num++;
        }

        cont++;
    }
    media = (float)soma / cont_num;
    printf("A média dos numeros positivos digitados é: %.1f\n", media);

    return 0;
}
