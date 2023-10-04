#include <stdio.h>
#include <stdlib.h>

/*
O programa irá gerar números aleatórios em intervalos definidos pelo usuário.
*/

int main(){
    
    int prim, segun;
    srand(time(NULL)); //Inicializador de semente.

    printf("\n------- GERADOR DE NÚMEROS ALEATÓRIOS -------\n");
    
    do
    {
        printf("\nInsira o primeiro número do intervalo: ");
        scanf("%d", &prim); //Ler primeiro número.
        printf("\nInsira o ultimo número intervalo: ");
        scanf("%d", &segun); //Ler segundo número.
        
        if(prim > segun) //Estrutura de decisão simples que visa impedir que o primeiro número seja maior que o segundo.
        {
            
            printf("\nErro o primeiro não pode ser maior que o segundo.\n");
            printf("\nTente novamente.\n");

        }
        
    } while(prim > segun);

    int rest = segun - prim + 1; //Calculo de antemão para saber o resto entre dois números do usuário (intervalo entre eles).

    for ( int cont = 0 ; cont < rest; cont++)//O loop será repetido dependendo do resto entre 'segun' e 'prim' atribuído na variável 'rest'.
    {   
        int randonNum = rand() % rest + prim; //Gera números aleatórios entre 'prim' e 'segun'.
        printf("%d\n", randonNum);
    }

    return 0;

}