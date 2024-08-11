#include <stdio.h>
#include <stdlib.h>

/*
O programa solicita ao usuário que informe seu peso e altura. 
A partir dessas informações, calcula o IMC utilizando a fórmula:
IMC = peso / (altura * altura)
*/

int main(){
    float peso, altura, imc;
    printf("Digite o sue peso: \n");
    printf("Ex.: 75.50 \n");
    scanf("%f", &peso);
    printf("Digite a sua altura \n");
    printf("Ex.: 1.75 \n");
    scanf("%f", &altura);
    imc = peso / (altura * altura);
    printf("O IMC é: %f \n", imc);
    return 0;
}
