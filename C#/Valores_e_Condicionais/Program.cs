using System;

class valores{
  static void Main(){

    int maior = 0;
    int menor = 0;
inicio:
a:
    Console.Write("\nInsira o primeiro valor: ");
    int a = Convert.ToInt32(Console.ReadLine());

    if (a <= 0){
      Console.WriteLine("\nValor invalido, tente novamente.");
      goto a;
    }

b:
    Console.Write("\nInsira o segundo valor: ");
    int b = Convert.ToInt32(Console.ReadLine());

    if (a <= 0){
      Console.WriteLine("\nValor invalido, tente novamente.");
      goto b;
    }

c:
    Console.Write("\nInsira o terceiro valor: ");
    int c = Convert.ToInt32(Console.ReadLine());

    if (a <= 0){
      Console.WriteLine("\nValor invalido, tente novamente.");
      goto c;
    }

    if (a > b && a > c){

      maior = a;

      if (b > c){
        menor = c;
      }
      else {
        menor = b;
      }
    }

    else if (b > a && b > c){

      maior = b;

      if (a > c){
        menor = c;
      }
      else {
        menor = a;
      }
    }

    else if (c > b && c > a){

      maior = c;

      if (b > a){
        menor = a;
      }
      else {
        menor = b;
      }
    }

    else {
      Console.WriteLine("\nValores iguais ou invalidos. Tente novamente.");
      goto inicio;
    }

// Exibe o menor valor lido multiplicado pelo maior e o maior valor dividido pelo menor

    Console.Write("\nResultado: " );
    Console.WriteLine(menor * maior);

    Console.Write("\nResultado: " );
    Console.WriteLine(maior / menor);

  }
}
