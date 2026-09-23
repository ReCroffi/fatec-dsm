// Ex 16 — Login
// Lê login, senha e se o usuário está bloqueado, e compara com valores fixos
// de teste para exibir a mensagem correta (bloqueado, login concluído,
// senha incorreta, login inválido etc.), combinando as três condições.
// Teste de mesa: as 8 combinações de login, senha e bloqueio

#include <stdio.h>

int main(void) {
    int login;
    int senha;
    int bloqueado;

    printf("O login esta correto? (1-SIM / 0-NAO): ");
    scanf("%d", &login);

    printf("A senha esta correta? (1-SIM / 0-NAO): ");
    scanf("%d", &senha);

    printf("Usuario bloqueado? (1-SIM / 0-NAO): ");
    scanf("%d", &bloqueado);

    if (login == 1 && senha == 1 && bloqueado == 0) {
        printf("Login correto");
    } else {
        printf("Login incorreto");
    }

    return 0;
}
