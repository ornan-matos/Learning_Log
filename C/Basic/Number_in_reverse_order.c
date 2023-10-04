#include <stdio.h>
#include <stdlib.h>

/*
Programa lê três números inteiros inseridos e irá imprimi-los na tela na ordem
inversa da entrada.
*/

int main(){
    int num1;
    int num2;
    int num3;
    printf("\nInsira o primeiro numero: ");
    scanf("%d", &num1);
    printf("\n\n");
    fflush;
    printf("\nInsira o segundo numero: ");
    scanf("%d", &num2);
    fflush;
    printf("\n\n");
    printf("\nInsira o terceiro numero: ");
    scanf("%d", &num3);
    fflush;
    printf("\n\n");
    printf("Ordem inserida: %d", num1);
    printf(" %d", num2); 
    printf(" %d", num3);
    printf("\n\n");
    printf("Ordem inversa: %d", num3);
    printf(" %d", num2); 
    printf(" %d", num1);
    printf("\n\n");

    return 0;
}