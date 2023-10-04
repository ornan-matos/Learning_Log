#include <stdlib.h>
#include <stdio.h>

/*
O programa irá conceder um aumento de 10% ao salário dos funcionários de uma
empresa, os quais recebem até R$ 1.000,00.
*/

int main()
{

    float salario;

    printf("\nPara saber se você irá receber o amento siga as instruções.");
    printf("\n\nInsira o seu salário: ");
    scanf("%f", &salario);
    printf("\n\n");

    if (salario <= 1000)
    {
        float aumento = (salario / 10) + salario;
        printf("Parabéns! Você está elegível para receber o aumento.\n");
        printf("Seu novo salário será: R$%2.f\n\n", aumento);
    }
    else
    {
        printf("Desculpe. Você não está elegível para receber aumento.\n\n");
    }

    return 0;
}