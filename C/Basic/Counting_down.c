#include <stdlib.h>
#include <stdio.h>

/*
O programa que apresentará uma contagem regressiva a partir de um número inteiro inserido pelo o usuário.
*/

int main(){

    int num;
    
    printf("\nInsira um numero inteiro: ");
    scanf("%d", &num);

    while (num > 0){
            printf("\n%d", num);
            num--;
    } 
    
    printf("\n\nFim da contagem regressiva.\n\n");

    return 0;

}