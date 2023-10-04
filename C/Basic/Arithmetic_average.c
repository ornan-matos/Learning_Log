#include <stdio.h>
#include <stdio.h>

/*
O programa irá calcular a média aritmética de três números digitados pelo usuário.
*/

int main(){
    float num1;
    float num2;
    float num3;
    printf("\n\nInsira o primeiro numero: ");
    scanf("%f", &num1);
    printf("\n");
    printf("\n\nInsira o primeiro segundo: ");
    scanf("%f", &num2);
    printf("\n");
    printf("\n\nInsira o terceiro numero: ");
    scanf("%f", &num3);
    printf("\n\n");
    float media = num1 + num2 + num3;
    printf("Media Aritmética: %.2f\n\n", media / 3);
    return 0;
}