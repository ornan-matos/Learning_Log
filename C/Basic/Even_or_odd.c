#include <stdio.h>
#include <stdlib.h>
/*
O programa informara se o número inserido é par ou ímpar.
*/
int main(){
    int num;
    printf("\nInsira um número: ");
    scanf("%d", &num);
    printf("\n\n");
    int resul = num % 2;
    if (resul == 0)
    {
        printf("O número é par.\n\n");
    }
    else {
        printf("O número é ímpar.\n\n");
    }
    return 0;

    }