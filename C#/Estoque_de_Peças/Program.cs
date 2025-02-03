using System;

class media{
  static void Main(){
    Console.WriteLine("\nEstoque Médio de Parafusos\n");
    
    Console.WriteLine("\nIsira o número maxímo de Parafusos suportados pelo estoque:");
    int max = Convert.ToInt32(Console.ReadLine());
    
    Console.WriteLine("\nIsira o número minimo de Parafusos que o estoque deve conter:");
    int min = Convert.ToInt32(Console.ReadLine());

    int media = (min + max) / 2;

    Console.WriteLine("\nEstoque medio recomendado: " + media + "parafusos.");

  }
}
