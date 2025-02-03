using System;

class area{
  static void Main(){
    Console.WriteLine("\nCálculo de Área de Circulo em Centímetros\n");

    Console.WriteLine("\nInsira o raiodo do cirulo (em cm)");

    double raio = Convert.ToDouble(Console.ReadLine());

    double area = 3.14 * (Math.Pow(raio,2));

    Console.WriteLine(String.Format("\nArea Corespondente: {0}cm", area));

  }
}
