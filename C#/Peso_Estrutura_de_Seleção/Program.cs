using System;

class peso{
  static void Main(){
    Console.WriteLine("\nEscolha uma das alaternativas");
    Console.WriteLine("--------------------------------");
inicio:
    Console.WriteLine("\n1...\tHomen\n2...\tMulher");
    string op = Console.ReadLine();

    Console.Write("\nInsira a sua altura: ");
    float altura = Convert.ToSingle(Console.ReadLine());

    switch (op){

      case "1":
        double h = (72.7 * altura) - 58;
        Console.WriteLine(String.Format("\nPeso Ideal: {0:F2} kg", h));
        break;
      case "2":
        double m = (62.1 * altura) - 44.7;
        Console.WriteLine(String.Format("\nPeso Ideal: {0:F2} kg", m));
        break;
      default:
        Console.WriteLine("\nOpção invalida! Tente novamente.");
        goto inicio;
        break;

    }
  }
}
