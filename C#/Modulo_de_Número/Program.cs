using System;

class modulo{
  static void Main(){
    Console.WriteLine("\nModulo de um número");

    Console.Write("\nInsira o número inteiro: ");
    int num = Convert.ToInt32(Console.ReadLine());

    if (num >= 0){
      Console.WriteLine("\nModulo = " + num);
    }
    else {
      num = num * (-1);
      Console.WriteLine("\nModulo = " + num);
    }
  }
}
