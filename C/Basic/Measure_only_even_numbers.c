#include <stdio.h>

/*
O programa recebe números do usuário e calcula a media dos números digitados, somente números pares. A leitura irá ser encerrada se o usuário digitar zero.
*/

int main(){

    int num; // numero digitado pelo usuário
    int soma = 0; // soma dos número digitados pelo usuário

    printf("\n\nDigite números pares para obter a media (pressione 0 para sair)\n\n)"); // mensagem inicial

    do
    {
        printf("\n\nDigite um número:"); // mensagem para o usuário
        scanf("%d", &num);  // leitura do numero digitado pelo usuário

        soma = soma + num; // soma dos números digitados pelo usuário

    } while (num != 0); // condição de parada do loop
    
    
    if (soma %2 == 0) // condição para verificar se a soma é par ou impar
    {
        int media = soma / 2; // calculo da media
        printf("\n\nMedia: %d\n", media); // impressão da media
    }

    else
    {
        printf("\n\n Desculpe! A somas dos valores inseridos não é par.\n"); // mensagem de erro
    }
    
    return 0; 
    
}
