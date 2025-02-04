using System;

class litros{
  static void Main(){
    Console.WriteLine("Forneça o tempo médio da viagem:");
    float tempo = Convert.ToSingle(Console.ReadLine());

    Console.WriteLine("Forneça a velocida média:");
    int velocida = Convert.ToInt32(Console.ReadLine());

    int distancia = Convert.ToInt32(tempo) * velocida;

    int litros = distancia / 12;

    Console.WriteLine(String.Format("\nA "));


  }
}
