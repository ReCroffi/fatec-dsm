// Ex 17 — Soma e contagem até digitar 0 (enquanto)
// Faça um algoritmo que leia números até o momento em que o usuário digite o
// número "0", o algoritmo deve somar os números informados pelo usuário e ao
// mesmo tempo contar quantos foram somados, ao final o algoritmo deve mostrar
// o resultado final da soma e também quantos números foram digitados.

#include <stdio.h>

int main(void) {
    int numero, soma = 0, contador = 0;
    while (1) {
        printf("Digite um número ou 0 para sair: ");
        scanf("%d", &numero);
        if (numero == 0) {
            break;
        }
        soma += numero;
        contador++;
    }

    printf("Soma: %d\n", soma);
    printf("Quantidade de números digitados: %d\n", contador);

    return 0;
}
