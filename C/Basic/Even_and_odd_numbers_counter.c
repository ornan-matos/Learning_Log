#include <stdio.h>

/*
 O programa irá receber dez números inteiros do teclado e dirá quantos são pares e
quantos são ímpares.
*/

int main(){
  
  int num; // Número a ser inserido
  int imp = 0; // Números impares
  int par = 0; // Números pares
  int cont = 0; // Contador
  
  while(cont < 10) // Enquanto o contador for menor que 10
  {
    printf("\n\nInsira um número: ");
    scanf("%d", &num); // Recebe o número
    
    int total = num%2; // Verifica se o número é par ou impar
    
    if(total == 0) // Se o resto da divisão for 0, o número é par
    {
      imp++; // Incrementa o número de impares
    }
    
    else  // Se o resto da divisão for diferente de 0, o número é impar
    {
      par++; // Incrementa o número de pares
    }

    cont++; // Incrementa o contador
  }
  
  printf("\n\nQuantidade de numeros pares: %d\n", par); // Exibe a quantidade de números pares e impares
  printf("\nQuantidade de numeros impares: %d\n", imp); // Exibe a quantidade de números pares e impares
  
  return 0;
  
}
