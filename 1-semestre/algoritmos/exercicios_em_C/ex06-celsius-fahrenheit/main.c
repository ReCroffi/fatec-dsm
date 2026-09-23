// Ex 6 — Celsius para Fahrenheit
// Lê uma temperatura em Celsius e exibe o valor convertido para Fahrenheit.
// Teste de mesa: 25 °C

#include <stdio.h>

int main(void) {
    float temp_f, temp_c;
    printf("Entre com o valor em Celsius: \n");
    scanf("%f", &temp_c);
    temp_f = (9.0 / 5 * temp_c) + 32;
    printf("A temperatura em Farenheit é: %.2f", temp_f);

    return 0;
}
