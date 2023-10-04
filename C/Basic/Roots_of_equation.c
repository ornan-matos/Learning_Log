#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*
O programa irá calcular as raízes da equação do 2° grau (ax 2 + bx + c); os valores de a, b e c são fornecidos pelo usuário.
*/

int main()
{

    float a, b, c;

    printf("\n\nEquação de segundo grau \n\n");
    printf("Informe o valor de a: ");
    scanf("%f", &a);
    printf("\n");
    printf("Informe o valor de b: ");
    scanf("%f", &b);
    printf("\n");
    printf("Informe o valor de c: ");
    scanf("%f", &c);
    printf("\n");

    float delta = (pow(b, 2)) - 4 * a * c;

    if (delta < 0)
    {
        printf("Valor de Delta %.2f\n", delta);
        printf("Impossível calcular um valor negativo\n\n");
    }
    else
    {

        float x1 = ((-b) + sqrt(delta)) / (2 * a);
        float x2 = ((-b) - sqrt(delta)) / (2 * a);

        printf("A primeira raiz quadrada x1 é: %.2f\n\n", x1);
        printf("A segunda raiz quadrada x2 é: %.2f\n\n", x2);
    }

    return 0;
}