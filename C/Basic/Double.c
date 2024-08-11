#include <stdio.h>
#include <stdlib.h>

/*
O programa calcula o dobro de um número inteiro.

Este programa realiza as seguintes etapas:
1. Solicita ao usuário que insira um número inteiro.
2. Lê o número inteiro fornecido pelo usuário.
3. Calcula o dobro do número inserido.
4. Exibe o número original e o seu dobro na tela.
*/

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
