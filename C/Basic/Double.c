#include <stdio.h>
#include <stdlib.h>

int main(){
    int num;
    printf("Insira um numero inteiro para descobrir o seu dobro:\n");
    scanf("%d", &num);
    int dou = num * 2;
    printf("\n");
    printf("O dobro de %d", num);
    printf(" é %d \n", dou);
    printf("\n");
    return 0;
}
