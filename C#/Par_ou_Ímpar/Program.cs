using System;

class par_impar{
  static void Main(){

    Console.Write("\nInsira um número: ");
    int num = Convert.ToInt32(Console.ReadLine());

    if (num % 2 == 0){
      Console.WriteLine("\nO número é par!");
    } else {
      Console.WriteLine("\nO número é impar!");
    }
  }
}
