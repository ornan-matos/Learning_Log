#include <stdio.h>
#include <stdlib.h>

/*
O programa irá ler o nome de um aluno e as notas que ele obteve nas quatro unidades ano. No final, o programa deve informar o nome do aluno e a sua média (aritmética).

Média minima para ser aprovado = 7
*/

int main(){

    char nome[20];
    float num1, num2, num3,num4;
    printf("\n\n Resultado Escolar.\n\n");
    printf("Insira o seu nome: ");
    scanf("%s", &nome);
    printf("\n\n");
    printf("Insira a sua nota da 1° UNIDADE: ");
    scanf("%f", &num1);
    printf("\n");
    printf("Insira a sua nota da 2° UNIDADE: ");
    scanf("%f", &num2);
    printf("\n");
    printf("Insira a sua nota da 3° UNIDADE: ");
    scanf("%f", &num3);
    printf("\n");
    printf("Insira a sua nota da 4° UNIDADE: ");
    scanf("%f", &num4);
    printf("\n\n");

    float resultado = (num1 + num2 + num3 + num4) / 4;

    if(resultado >= 7) {
        printf("Parabéns, %s", nome);
        printf("! Você esta aprovado!\n\n");
        printf("Media: %.2f\n\n", resultado);
    } 
    else {
        printf("%s", nome);
        printf(", infelizmente você foi reprovado.\n\n");
        printf("Média: %.2f\n\n", resultado);
    }

    return 0;
    
}