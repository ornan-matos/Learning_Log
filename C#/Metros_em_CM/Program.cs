using System;

class conversao{
  static void Main(){
    Console.WriteLine("\nConversão de Metros em Centímetros");
    Console.WriteLine("\nInsira a Quantidade de Metros");

    float metros = Convert.ToSingle(Console.ReadLine());

    float centimetros = metros * 100;
    float milimetros = metros * 1000;

    Console.WriteLine(String.Format("\n{0}M\n=\n{1}cm\n{2}mm", metros, centimetros, milimetros));
  }
}
