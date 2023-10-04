#include <stdio.h>
#include <stdlib.h>

/*
O programa com uma estrutura de repetição (com teste final) e irá assumir uma condição de saída com caractere e acumular somando os valores inseridos em cada iteração da repetição.
*/

int main() {
    
    int x;
    int total = 0;
    int cont = 0;
    char let;

    printf("\n\nInsira um numero para iniciar a soma.\n");
    printf(" - Na sequência insira qualquer caractere para continuar a soma.\n");
    printf(" - Caso queira para e obter o resultado insira a 'q' para sair.\n");

    do {
        printf("\nInsira um numero: ");
        scanf("%d", &x);
        fflush(stdin);
        total = total + x;
        cont++;
        printf("Digite uma letra: ");
    } while (let = getchar(), getchar() != 'q'); //getchar() duplo para que o leitor de caractere ignore o '\n' (enter).

    printf("\n------- Resultado --------\n\n");
    printf("Total = %d\n", total);
    printf("Repetições = %d\n\n", cont);

    return 0;

}