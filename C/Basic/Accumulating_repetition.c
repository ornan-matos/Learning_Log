#include <stdio.h>
#include <stdlib.h>

/*
O programa com uma estrutura de repetição e irá assumir uma condição de saída com caractere e acumular somando os valores inseridos em cada iteração da repetição.
*/

int main(){
    
    int x; // variavel para receber o valor inserido
    int total = 0; // variavel para acumular os valores inseridos
    int cont = 0; // variavel para contar as repetições
    char let ; // variavel para receber o caractere de saída

    printf("\n\nInsira um numero para iniciar a soma.\n");
    printf("Para o obter o resultado insira a 'q' para sair.\n");

    while(let = getchar() != 'q')// condição de saída
    {
        
        printf("Insira mais um numero: \n");
        scanf("%d", &x);
        fflush(stdin);// limpa o buffer do teclado
        total = total + x;
        ++cont;
    }
    
    printf("\n------- Resultado --------\n\n");
    printf("Total = %d\n", total);// imprime o total
    printf("Repetições = %d\n\n", cont);// imprime o total de repetições

    return 0;
    
}