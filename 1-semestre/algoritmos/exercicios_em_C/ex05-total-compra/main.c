// Ex 5 — Total da Compra
// Lê a quantidade de itens e o valor de cada item, e exibe o total da compra.
// Teste de mesa: 4 e 25

#include <stdio.h>

int main(void) {
    int qtd;
    float valor;
    printf("Entre a quantidade de itens: \n");
    scanf("%i", &qtd);
    printf("Entre com o valor de cada item: \n");
    scanf("%f", &valor);
    printf("O valor da compra é: R$%.2f", qtd * valor);

    return 0;
}
