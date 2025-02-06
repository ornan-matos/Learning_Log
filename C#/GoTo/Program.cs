using System;

class go_to{
  
  static void Main(){

    inicio:

    Console.Write("\nDigite um número: (0-10): ");
    int n1 = Convert.ToInt32(Console.ReadLine());

    if (n1 >= 0 && n1 <= 10){
      Console.WriteLine("\nValor entregue!");
    } else{
      Console.WriteLine("\nValor não reconhecido! Tente novamente...");  
      goto inicio;
    }

  }
}
