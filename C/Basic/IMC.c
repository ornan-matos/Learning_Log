#include <stdio.h>
#include <stdlib.h>

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
