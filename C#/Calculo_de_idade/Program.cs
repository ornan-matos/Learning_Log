using System;

class idade{
  static void Main(){

    Console.WriteLine("\nInsira a quantidade de anos, meses e dias que você possui.");
    
    Console.Write("\nAnos: ");
    int anos = Convert.ToInt32(Console.ReadLine());

    Console.Write("\nMeses: ");
    int meses = Convert.ToInt32(Console.ReadLine());
    
    Console.Write("\nDias: ");
    int dias = Convert.ToInt32(Console.ReadLine());
    
    int idade = ((anos * 365) + (meses * 30)) + dias; 

    Console.WriteLine(String.Format("\nTotal de dias de vida: {0} dias", idade));    

  }
}
