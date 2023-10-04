#include <stdio.h>
#include <stdlib.h>

/*
Informe a categoria de um jogador de futebol, considerando sua
idade: infantil (até 13 anos), juvenil (até 17 anos) ou sênior (acima de 17 anos).
*/

int main(){
    int idade;
    printf("\n");
    printf("Insira a idade do jogador: ");
    scanf("%d", &idade);
    printf("\n");
    if (idade <= 13){
        printf("A categoria adequada é Infantil\n");
    }
    else {
        if (idade >= 14){
            if (idade <= 17){
                printf("A categoria adequada é Juvenil\n");
            }
            else {
                if(idade >= 18){
                    printf("A categoria adequada é Sênior\n");
                }   
            }
        
        }
    
    }
    printf("\n");
    return 0;
}