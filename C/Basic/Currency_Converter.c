#include <stdlib.h>
#include <stdio.h>
#include <math.h>

/*
Este código em C realiza a conversão de um valor monetário de dólares para reais, considerando uma taxa de câmbio fixa de 4,85 reais por dólar.
*/

int main(){

    float dolar;
    printf("Converta Dolar em Reais hoje - 11/07/23\n");
    printf("\n");
    printf("Insira o valor em Dolar:");
    scanf("%f", &dolar);
    printf("\n");
    float conv = dolar * 4.85;
    printf("%.2f", dolar);
    printf(" dolares valem %.2f", conv);
    printf(" reais\n");
    printf("\n");
    printf("1 Dolar = 4,85 Reais\n");
    return 0;
}
