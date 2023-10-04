#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*
O programa irá calcular a velocidade de queda de um corpo em função do tempo, partindo da velocidade zero.

- Equação de Torricelli = v² = v0² + 2.a.ΔS
- Gravidade da Terra g = 9.8 m/s2
*/

int main(){
    float grav = 9.8;
    float qued;
    printf("\nInsira o valor da queda em metros: ");
    scanf("%f", &qued);
    printf("\n\n");
    float vel = 2 * qued * grav;
    printf("Velocidade Final: %.2f", sqrt(vel));
    printf(" m/s\n\n");
    return 0;
    }