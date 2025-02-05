using System;

class multipla{
  static void Main(){

    Console.Write("\nTemperatura atual (Celcius):");
    Int16 temperatura = Convert.ToInt16(Console.ReadLine());

    if (temperatura > 25 && temperatura < 29){
      Console.WriteLine("\nTemperatura agradavel!");
    }
    else if (temperatura == 25){
      Console.WriteLine("\nTemperatura ambiente!");
    }
    else if (temperatura < 25 && temperatura > 15){
      Console.WriteLine("\nTempo Frio!");
    }
    else if (temperatura >= 29){
      Console.WriteLine("\nTempo Quente!");
    }
    else{
      Console.WriteLine("\nTempo Muito Frio!");
    }

  }
}
