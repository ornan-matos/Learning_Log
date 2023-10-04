#include <stdio.h>
#include <stdlib.h>

/*
O programa exibirá uma restrição em caso de divisão por zero.
*/

int main(){
    
    int numerador, denominador;

    printf("\nDivisão de números inteiros.\n\n");

    printf("Numerador: \n");
    scanf("%d", &numerador);

    do{

        printf("Denominador: \n");
        scanf("%d", &denominador);

        if(denominador == 0) //Se o segundo número for o igual a zero, a mensagem será exibida e o loop retornará a o início.
        {
            printf("\n\nO denominador não pode ser zero!\nTente novamente!\n\n");
            continue; // Volta para o início do loop
        }
        
        else
        {
           int resultado = numerador / denominador;
           printf("\nResultado = %d\n", resultado);
           break; // Sai do loop quando a divisão é válida
        }
    

    } while(denominador == 0);

    return 0;

}
