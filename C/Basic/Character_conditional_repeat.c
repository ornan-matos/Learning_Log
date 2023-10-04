#include <stdlib.h>
#include <stdio.h>

/*
O programa irá imprimir "Tente novamente!" na tela enquanto o caractere “q” não for digitado pelo usuário (portanto, condição de saída com caractere). Também irá quantas repetições foram realizadas.
*/

int main(){

    int cont = 0;
    char let;
    
    //getchar() duplo para que o leitor de caractere ignore o '\n' (enter).    
    while(let = getchar(), getchar() != 'q'){
        
        printf("Tente novamente!\n");
        
        fflush;
        
        cont++;    
    }

    printf("\nSistema de repetição pausado.\n");
    printf("Numero total de tentativas: %d\n", cont);

    return 0;

}