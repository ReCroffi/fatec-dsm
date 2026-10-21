#include <stdio.h>

int main(void)
{
    int nota, count_cinco, count_um_dois, i, soma;
    float med;
    count_cinco = 0;
    count_um_dois = 0;
    soma = 0;
    for (i = 1; i < 11; i++)
    {
        printf("Participante %i\n", i);
        printf("Entre sua nota: \n");
        printf("1 - Muito Instisfeito\n");
        printf("2 - Instisfeito\n");
        printf("3 - Indiferente\n");
        printf("4 - Satisfeito\n");
        printf("5 - Muito Satisfeito\n");
        scanf("%i", &nota);
        while (nota < 1 || nota > 5)
        {
            printf("Entre uma nota valida!\n");
            scanf("%i", &nota);
        }
        if (nota == 5)
        {
            count_cinco++;
        }
        else if (nota == 1 || nota == 2)
        {
            count_um_dois++;
        }
        soma = soma + nota;
    }
    med = (float)soma / 10;
    printf("Média das notas: %.2f\n", med);
    printf("Quantidade de participantes que deram 5: %i\n", count_cinco);
    printf("Quantidade de participantes que deram 1 ou 2: %i\n", count_um_dois);

    return 0;
}
