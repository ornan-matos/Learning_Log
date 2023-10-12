#include <stdio.h>

/*
O programa irá solicitar ao usuário três números inteiros a, b e c, em que a seja maior
que 1. O programa deve somar todos os inteiros entre b e c que sejam divisíveis por a.
*/

int main(){

    int num1, num2, num3; //num1 = a, num2 = b, num3 = c
    int soma = 0; //soma dos números divisíveis por a
    
    printf("\n\nInsira o primeiro numero inteiro: ");
    scanf("%d", &num1);

    if(num1 <= 1)
    {
        printf("\n\nO numero deve ser maior que 1!\n\n");
        return 1;
    }

    printf("\nInsira o segundo numero inteiro: ");
    scanf("%d", &num2);

    printf("\nInsira o terceiro numero inteiro: ");
    scanf("%d", &num3);
    
    printf("\n\n");

    if(num2 > num3) //caso o segundo numero seja maior que o terceiro, troca os valores
    {
        int temp = num2;
        num2 = num3;
        num3 = temp;
    }

    for(int i = num2; i <= num3; i++) //soma os números divisíveis por a
    {
        if(i % num1 == 0) //se o resto da divisão for 0, o numero é divisível por a  
        {
            soma += i; //soma o numero
        }
    }

    printf("A soma dos números %d e %d divisíveis por %d é: %d\n", num2, num3, num1, soma); //imprime a soma dos números divisíveis por a


    return 0;
}