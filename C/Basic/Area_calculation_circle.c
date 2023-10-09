#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*
O programa irá calcular a área de um círculo de raio r, testando ao final se o valor da area é menor que zero.
*/

int main() 
{
    float diametro; // variavel para receber o valor do diametro
    printf("\nInsira o diâmetro do circulo: "); // solicita o valor do diametro
    scanf("%f", &diametro); // recebe o valor do diametro
    printf("\n\n");
    float raio = diametro / 2;
    float area = pow(raio, 2) * 3.1415926535898; // calcula a area
    printf("Area: %.2f²\n\n", area); // imprime a area
    
    if(area < 0){
        printf("O valor é menor que zero!\n\n");
    } // testa se a area é menor que zero
    else{
        printf("O valor é maior que zero!\n\n");
    }

    return 0;
}