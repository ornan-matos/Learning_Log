#include <stdio.h>
#include <stdlib.h>

int main(){
    float meters;
    printf("Conversor de Metros em Milimetros\n");
    printf("\n");
    printf("Insira os valor em metros:");
    scanf("%f", &meters);
    float mili = meters * 1000;
    printf("\n");
    printf("Valor convertido: ");
    printf("%.2f", mili);
    printf(" mm\n");
    return 0;
}
