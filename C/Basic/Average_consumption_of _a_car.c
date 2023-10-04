#include <stdio.h>
#include <stdlib.h>

/*
O programa irá calcular o consumo médio de um automóvel; são fornecidos a
distância total percorrida e o total de combustível gasto.
*/

int main(){

    float dist, litros, consumo;
    
    printf("\n\nCalcule o consumo médio do seu veículo.\n\n");
    printf("Insira a distância percorrida: ");
    scanf("%f", &dist);
    printf("\n");
    printf("Insira a quantidade de combustível: ");
    scanf("%f", &litros);
    printf("\n\n");
    consumo = dist / litros;
    printf("O consumo médio é %.2f", consumo);
    printf("km/l\n\n");

    return 0;

}