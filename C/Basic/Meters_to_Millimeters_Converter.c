#include <stdio.h>
#include <stdlib.h>

/*

O programa converte um valor em metros para milímetros.
 
Funcionamento:
1. O programa solicita ao usuário que insira um valor em metros.
2. O valor inserido é lido e convertido de metros para milímetros.
3. O resultado da conversão é exibido na tela com duas casas decimais.

*/

int main(){
    float meters;
    printf("Conversor de Metros em Milimetros\n");
    printf("\n");
    printf("Insira os valor em metros:");
    scanf("%f", &meters);
    float mili = meters * 1000;
    printf("\n");
    printf("Valor convertido: ");
    printf("%.2f", mili);
    printf(" mm\n");
    return 0;
}
