using System;

class tempo{
  static void Main(){
    Console.WriteLine("\nTempo de Download --> \n");
  
    Console.WriteLine("Tamanho do arquivo em MB");
    float arquivo = Convert.ToSingle(Console.ReadLine());

    Console.WriteLine("Velocidad da Internet em Mbps");
    float internet = Convert.ToSingle(Console.ReadLine());

    float tempo = ((arquivo / internet) * 8) / 60 ; 

    Console.WriteLine(String.Format("\nVelocidade da Rede: {0}Mbps\nTamanho do Arquivo: {1}MB\nTempo para concluir o Download: {2:F2} minutos", internet, arquivo, tempo));

  }
}
