#include <stdio.h>
#include <stdlib.h>

/*
Solicita ao usuário que insira um número inteiro, 
lê o número da entrada padrão e, em seguida, exibe o número inserido 
na tela. O programa utiliza as funções `printf` e `scanf` da biblioteca 
padrão `stdio.h` para realizar a entrada e saída de dados.
*/

int main(){
    int number;
    printf("Insira um numero:\n");
    scanf("%d", &number);
    printf("O numero inserido é %d \n", number);
    return 0;

}
