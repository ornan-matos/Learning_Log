#include <stdio.h>

/*
O programa irá calcular a média dos números digitados pelo usuário, se eles forem
pares. O programa irá terminar a leitura se o usuário digitar zero.
*/

int main (){

    int numero, soma = 0, contador = 0;

    printf("\n-- Verificador de Media --\n\n");
    printf("Insira uma sequência números (0 para encerrar):\n\n");

    while (1)
    {
        scanf("%d", &numero);

         if(numero == 0)
        {
            break;
        }

        if (numero % 2 == 0)
        {
            soma += numero;
            contador++;
        }

        else
        {
            printf("\nNumero não par inserido, tente novamente.\n\n");
        }
    } 

    double media = (double)soma /contador;
    printf("A media dos números é: %.2f\n", media);

    return 0;
}