using System;

class pos_neg{
  static void Main(){

    Console.WriteLine("\nDigite 0 a qualquer momento para sair.");
      
    while(true){

      Console.Write("\nInsira o número: ");
      int num = Convert.ToInt32(Console.ReadLine());

      if (num > 0){
        Console.WriteLine("\nO número é positivo!");
      }
      else if (num == 0){
        Console.WriteLine("\nPrograma finalizado.");
        break;
      }
      else {
        Console.WriteLine("\nO número é negativo");
      }

    }

  }
}
