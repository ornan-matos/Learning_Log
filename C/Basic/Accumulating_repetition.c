#include <stdio.h>
#include <stdlib.h>

/*
O programa com uma estrutura de repetição e irá assumir uma condição de saída com caractere e acumular somando os valores inseridos em cada iteração da repetição.
*/

int main(){
    
    int x; 
    int total = 0; 
    int cont = 0;
    char let ;

    printf("\n\nInsira um numero para iniciar a soma.\n");
    printf("Para o obter o resultado insira a 'q' para sair.\n");

    while(let = getchar() != 'q'){
        
        printf("Insira mais um numero: \n");
        scanf("%d", &x);
        fflush(stdin);
        total = total + x;
        ++cont;
    }
    
    printf("\n------- Resultado --------\n\n");
    printf("Total = %d\n", total);
    printf("Repetições = %d\n\n", cont);

    return 0;
    
}