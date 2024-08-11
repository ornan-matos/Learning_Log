#include <stdio.h>
#include <stdlib.h>

/*
O programa solicita ao usuário que escolha seu time de futebol preferido
entre três opções disponíveis: Liverpool, Real Madrid e Ajax.
O usuário deve inserir um número correspondente à sua escolha.
O programa, então, exibe o número do time escolhido pelo usuário.
*/

int main() {
    int numero;
    printf("Escolha seu time de futebol preferido: \n");
    printf("1.Liverpool \n");
    printf("2.Real Madrid \n");
    printf("3.Ajax \n");
    scanf("%d", &numero);
    printf("O time escolhido foi o numero %d \n", numero);
    return 0;

}
