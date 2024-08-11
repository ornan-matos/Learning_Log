#include <math.h>
#include <stdio.h>
#include <stdlib.h>

/*
Este programa calcula e exibe a potência de um número fornecido pelo usuário.
O usuário é solicitado a inserir um número, e o programa calcula e mostra:
- O quadrado do número
- O cubo do número
- A quarta potência do número
O cálculo das potências é realizado usando a função pow() da biblioteca math.h.
 */

int main(){
    float num;
    printf("Digite um numero para descobrir a sua potencia:\n");
    scanf("%f", &num);
    float dou = pow(num, 2);
    float tri = pow(num, 3);
    float qua = pow(num, 4);
    printf("\n");
    printf("%.2f ", num);
    printf("Elevado ao quadrado é %.2f", dou);
    printf("\n");
    printf("%.2f ", num);
    printf("Elevado ao cubo é %.2f", tri);
    printf("\n");
    printf("%.2f ", num);
    printf("Elevado a quarta potencia é %.2f \n", qua);
    return 0;
}
