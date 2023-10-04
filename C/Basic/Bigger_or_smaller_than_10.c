#include <stdio.h>
#include <stdlib.h>

/*
O programa que receberá um número e mostrará uma mensagem caso este seja maior, menor ou igual a 10.
*/

int main(){

    int num;

    printf("\n\nInsira um numero: ");
    scanf("%d", &num);
    printf("\n\n");
    
    if (num == 10) {
            printf("O numero %d", num);
            printf(" é igual ao próprio 10.\n\n");
        }

    else {

        if (num > 10) {
            printf("O numero %d", num);
            printf(" é maior que 10.\n\n");
        }
        
        else{
            printf("O numero %d", num);
            printf(" é menor que 10.\n\n");
        }
    }
    
    return 0;

}