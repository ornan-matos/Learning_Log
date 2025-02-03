using System;

class peso{
  static void Main(){
    Console.WriteLine("\nCálculo do Peso Recomendado\n");

    Console.WriteLine("\nQual o seu nome:");
    string nome = Console.ReadLine();

    Console.WriteLine("\nQual a sua altura? (em metros)");
    float altura = Convert.ToSingle(Console.ReadLine());

    float peso = (72.7f * altura) - 58;

    Console.WriteLine(String.Format("\nOlá {0}! O seu peso recomendado é {1:F2}kg", nome, peso));



  }
}
