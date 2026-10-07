// Ex 22 — Menu de conta bancária (enquanto)
// Faça um algoritmo que mostre um menu de conta bancária com as seguintes
// opções: 1 – Verificar Saldo / 2 – Depositar / 3 – Sacar / 0 – Sair.
// O algoritmo deverá iniciar já com um valor fixo de R$ 2.000,00 na conta e
// deverá através das interações com o usuário aumentar (depositar) ou diminuir
// (sacar) o valor do saldo da conta, a interação com o usuário deve ser
// finalizada somente se ele digitar o número "0".

#include <stdio.h>

int main(void) {
    float saldo = 2000, dep, saq;
    int opt, rodando = 1;
    while (rodando) {
        printf("Selecione a opção Desejada: \n");
        printf("1 - Depósito \n");
        printf("2 - Saque \n");
        printf("0 - Sair \n");
        scanf("%i", &opt);
        switch (opt) {
        case 1:
            printf("Saldo disponível: %.2f\n", saldo);
            printf("Qual valor quer depositar: \n");
            scanf("%f", &dep);
            saldo += dep;
            printf("Saldo após depósito: %.2f\n", saldo);
            break;
        case 2:
            printf("Saldo disponível: %.2f\n", saldo);
            printf("Qual valor quer sacar: \n");
            scanf("%f", &saq);
            saldo -= saq;
            printf("Saldo após saque: %.2f\n", saldo);
            break;
        case 0:
            printf("Até logo\n");
            rodando = 0;
            break;
        }
    }
}