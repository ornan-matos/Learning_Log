#include <stdio.h>
#include <stdlib.h>

/*
O programa dirá qual é o maior valor de dois números distintos inseridos.
*/

int main(){
    int num1;
    int num2;
    printf("\n");
    printf("Insira o primeiro número: ");
    scanf("%d", &num1);
    printf("\n");
    printf("Insira o segundo número: ");
    scanf("%d", &num2);
    printf("\n");
    if(num1 > num2){
        printf("O primeiro número %d", num1);
        printf(" é maior que o segundo número %d\n", num2);
        printf("\n");   
    }
    else {
        printf("O segundo número %d", num2);
        printf(" é maior que o primeiro número %d\n", num1);
        printf("\n");
    }

    return 0;
}