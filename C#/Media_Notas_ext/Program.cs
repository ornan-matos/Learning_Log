using System;

class media{
  static void Main(){
    Console.WriteLine("\nVerificar Aprovação Escolar");

    Console.WriteLine("\nInsira o valor de cada disciplina");

    Console.Write("\nPortuguês: ");
    float port = Convert.ToSingle(Console.ReadLine());

    Console.Write("\nMatemática: ");
    float mat = Convert.ToSingle(Console.ReadLine());

    Console.Write("\nBiologia: ");
    float bio = Convert.ToSingle(Console.ReadLine());

    Console.Write("\nIngles: ");
    float ing = Convert.ToSingle(Console.ReadLine());
    
    Console.Write("\nGeografia: ");
    float geo = Convert.ToSingle(Console.ReadLine());

    float media = (port + mat + bio + ing + geo) / 5;

    if (media == 10){
      Console.WriteLine("\nAprovado por Distinção!");
    } else if (media >= 7){
      Console.WriteLine("\nAprovado!");
    } else {
      Console.WriteLine("\nReprovado!");
    }
  }
}
