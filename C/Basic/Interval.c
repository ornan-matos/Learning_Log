#include <stdio.h>
#include <stdlib.h>

/*
O programa irá receber um número e dizer se ele está no intervalo entre 100 e 200.
*/

int main(){
    
    int num;

    printf("\n\nInsira um numero inteiro: ");
    scanf("%d", &num);
    printf("\n\n");

    if(num >= 100){
        if(num <= 200){
            printf("O numero %d", num);
            printf(" esta no intervalo entre 100 e 200.\n\n");
        }
        else {
        printf("O numero %d", num);
        printf(" esta fora do intervalo entre 100 e 200.\n\n");
        }
    }
    else{
        printf("O numero %d", num);
        printf(" esta fora do intervalo entre 100 e 200.\n\n");
    }
}