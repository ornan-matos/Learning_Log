#include <stdlib.h>
#include <stdio.h>

/*
O programa irá ler cinco valores e contar quantos desses valores são negativos, mostrando essa informação no final.
*/

int main(){
    int num;
    int contNeg = 0;
    
    printf("\n---- Contagem de Números Negativos ----\n");

    for (int i = 0; i < 5; i++)
    {
        printf("\nNumero: \n");
        scanf("%d", &num);
        
        if(num < 0){
            contNeg++;
        }
    } 
    printf("\nQuantidade de Valores Negativos: %d\n", contNeg);

    return 0;
}