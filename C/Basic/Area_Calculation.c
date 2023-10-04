#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    float larg;
    printf("Para calcular a area. Insira as seguintes informações.\n");
    printf("\n");
    float com;
    printf("Largura:");
    printf("\n");
    scanf("%f", &larg);
    printf("Comprimento:");
    printf("\n");
    scanf("%f", &com);
    float area = larg * com;
    printf(" \n");
    printf("Area: ");
    printf("%.2f", area);
    printf("²\n");
    return 0;
}
