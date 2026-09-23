// Ex 15 — Desconto
// Lê o valor da compra e se o cliente é VIP, e exibe se o cliente
// tem direito a desconto (valor >= 100 ou é VIP).
// Teste de mesa: 150/S, 150/N, 50/S, 50/N

#include <stdio.h>

int main(void) {
    int VIP;
    float valor;
    printf("Entre o valor da compra: ");
    scanf("%f", &valor);
    printf("Cliente é VIP?\n1-SIM\n0-NÂO\n");
    scanf("%d", &VIP);
    if (valor >= 100 || VIP == 1) {
        printf("Cliente com direito a desconto");
    } else {
        printf("Cliente sem direito a desconto");
    }

    return 0;
}
