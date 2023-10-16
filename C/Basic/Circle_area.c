#include <stdio.h>
#include <string.h>
#include <math.h>

/*
O programa irá calcular a área de vários círculos de raio r, até que o usuário digite “n”.
*/

int main(){
  
  char desc, med;
  float raio;
  float pi = 3.14;

  printf("\n---- Calcule a área de um circulo ----\n");
  

  while(1)
  {
    printf("\nA medida está em Centímetros(c) ou Metros(m)\n");
    med = getchar();
    
    if(med == 'c')
    {
      printf("\nInsira o valor do raio do circulo:");
    scanf("%f", &raio);
    
    float valor = (pow(raio, 2)) * pi;


    printf("\n\nÁrea do circulo = %2.f centímetros\n", valor);
    
    getchar();

    printf("\nNovo calculo? SIM(s) ou NÃO (n)\n");
    desc = getchar();

    getchar();

    if(desc == 'n')
    {
      printf("\nOK!\n");
      break;
    }
    }
    
    if (med == 'm')
    {
      printf("\nInsira o valor do raio do circulo:");
    scanf("%f", &raio);
    
    float valor = (pow(raio, 2)) * pi;


    printf("\n\nÁrea do circulo = %2.f metros\n", valor);
    
    getchar();

    printf("\nNovo calculo? SIM(s) ou NÃO(n)\n");
    desc = getchar();
    
    getchar();

    if(desc == 'n')
    {
      printf("\nOK!\n");
      break;
    }
    }
  
    
  }
  
  return 0;


}




