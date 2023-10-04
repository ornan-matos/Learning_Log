#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/*
O programa irá gerar um numero aleatório 1 a 10. O usuário tentara adivinha-lo.
*/

int main(){

    int randPC, randUser; /*Uma variável para o número aleatório do PC 'randPC' e outra variável para número escolhido pelo usuário'randUser'.*/

    srand (time(NULL));/*Garante que o gerador de números aleatórios seja inicializado com uma semente diferente a cada vez que o programa é executado.*/

    randPC = rand() % 10 + 1; /*Será extraído o resto da divisão do número aleatório gerado pela semente 'time(NULL)' dividido por dez. Na sequência será somado ao número um.*/

    printf("\n---------Escolha um numero entre 1 e 10.---------\n");

    do
    {
        printf("\nDigite o número: ");
        scanf("%d", &randUser); //Captura o número escolhido pelo usuário.
        if (randUser > randPC)
        {
            printf("\nO número é menor. Tente novamente!\n");
        }
        else if (randUser < randPC)
        {
            printf("\nO número é maior. Tente novamente!\n");
        }
        

    } while(randUser != randPC); //Fim da estrutura de repetição de teste final.

    printf("\nNumero Correto! Parabéns!\n");

    return 0;
}