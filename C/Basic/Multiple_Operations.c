#include <stdio.h>
#include <stdlib.h>

/**
O programa executa quatro operações básicas: soma, subtração, multiplicação e divisão,
com dois números inteiros que o usuário deve fornecer. Ele faz o seguinte:
1. Solicita ao usuário que insira dois números inteiros.
2. Calcula a soma, subtração, multiplicação e divisão desses números.
3. Exibe os resultados das operações.
 */

int main(){
    printf("Operações básicas com dois números.\n");
    printf("\n");
    int n1, n2;
    printf("Por favor, digite o primeiro número:\n");
    scanf("%d", &n1);
    printf("Por favor, digite o segundo numero:\n");
    scanf("%d", &n2);
    int soma = n1 + n2;
    int sub = n1 - n2;
    int mult = n1 * n2;
    int div = n1 / n2;
    printf("\n");
    printf("O resultado da parcela %d", n1);
    printf(" com a parcela %d \n", n2);
    printf("É igual a %d \n", soma);
    printf("\n");
    printf("O resultado do minuendo %d", n1);
    printf(" com o subtraendo %d \n", n2);
    printf("É igual a %d \n", sub);
    printf("\n");
    printf("O resultado do multiplicando %d", n1);
    printf(" com o multiplicador %d \n", n2);
    printf("É igual a %d \n", mult);
    printf("\n");
    printf("O resultado do dividendo %d", n1);
    printf(" com o divisor %d \n", n2);
    printf("É igual a %d \n", div);
    return 0;

}
