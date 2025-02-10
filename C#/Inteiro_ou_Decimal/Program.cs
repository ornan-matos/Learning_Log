using System;

class int_ou_dec{
  static void Main(){
    Console.Write("\nInsira um número (inteiro ou decimal): ");
    float num = Convert.ToSingle(Console.ReadLine());

    if (num % 1 == 0){
      Console.WriteLine("\nO número é inteiro!");
    } else {
      Console.WriteLine("\nO número é decimal!");
    }
  }
}
