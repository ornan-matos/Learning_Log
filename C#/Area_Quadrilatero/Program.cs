using System;

class area{
  static void Main(){

    Console.WriteLine("\nCalcule a Área de um Quadrilátero(Retângular)");

    Console.WriteLine("\nInsira a Altura do Retângulo:");
    float altura = Convert.ToSingle(Console.ReadLine());

    Console.WriteLine("\nInsira a Base do Retângulo:");
    float base_ = Convert.ToSingle(Console.ReadLine());

    float area = base_ * altura;

    Console.WriteLine("\nA área do Quadrilátero = " + area);

  }
}
