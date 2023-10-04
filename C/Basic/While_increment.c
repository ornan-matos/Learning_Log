#include <stdlib.h>
#include <stdio.h>

/*
O programa irá solicitar uma palavra qualquer ao usuário e também um número que representara a quantidade de vezes que a palavra será repedida. Como o resultado o output será a palavra do usuário repetida pelo número de vezes que foi predefinida.
*/

int main(){

    char name[20];
    int incremento;
    int decremento = 0;

    printf("\nInsira a palavra que sera repetida: ");
    scanf("%s", &name);
    printf("\nQuantas vezes a palavras será repetida: ");
    scanf("%d", &incremento);
    printf("\n\n");
    
    while(decremento < incremento)
    {
        printf("%s\n\n", name);
        incremento--;
    }

    return 0;
}