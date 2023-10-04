#include <stdio.h>
#include <stdlib.h>
/*
Problema fictício:
Uma cópia “xerox” custa R$ 0,25 por folha, mas acima de 100 folhas esse valor cai para R$ 0,20 por unidade. Dado o total de cópias,
o programa informara o valor a ser pago.
*/
int main(){
    int quant;
    printf("\n");
    printf("Insira a quantidade de copias desejada: ");
    scanf("%d", &quant);
    printf("\n");
    if (quant >= 100){
        float desco = quant * 0.20;
        printf("Valor total: %.2f \n", desco);
        printf("\n");
    }
    else{
        float semDesco = quant * 0.25;
        printf("Valor total: %.2f \n", semDesco);
        printf("\n");
    }
    return 0;

}
