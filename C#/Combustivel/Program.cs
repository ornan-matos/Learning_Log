using System;

class combustivel{

  static void Main(){
    Console.WriteLine("\nCalculo de Combustível");

    Console.Write("\nInsira o tempo gasto na viagem (em hora(s)): ");
    float tempo = Convert.ToSingle(Console.ReadLine());

    Console.Write("\nInsira a velocidade média (em KM/h): ");
    float velocidade = Convert.ToSingle(Console.ReadLine());

    float distancia = tempo * velocidade;

    float litros = distancia / 12;

    Console.WriteLine("\nRESULTADO DA ANALISE");
    Console.WriteLine("-----------------------");
    Console.WriteLine(String.Format("Velocidade média: \t{0}km/h\nTempo:             \t{1} hora(s)\nDistância Percorrida:\t{2} KM\nQuantidade de Litros\t{3:F2}L", velocidade, tempo, distancia, litros));

    
  }

}
