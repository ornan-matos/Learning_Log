#include <stdio.h>

/*
O programa irá ler três números do teclado e os imprimir na tela na ordem inversa da entrada.
*/

main(){

    int num1, num2, num3;

    printf("\nInsira o primeiro número: \n");
    scanf("%d", &num1);

    printf("\nInsira o segundo número: \n");
    scanf("%d", &num2);

    printf("\nInsira o terceiro número: \n");
    scanf("%d", &num3);

    printf("\nO números na ordem inversa: %d %d %d\n", num3, num2, num1);

    return 0;

}