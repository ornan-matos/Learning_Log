using System;

class maior_três{
  static void Main(){
    Console.WriteLine("\nMaior de Três números");

    Console.Write("\nInsira o primeiro número: ");
    int num1 = Convert.ToInt32(Console.ReadLine());

    Console.Write("\nInsira o segundo número: ");
    int num2 = Convert.ToInt32(Console.ReadLine());

    Console.Write("\nInsira o terceiro número: ");
    int num3 = Convert.ToInt32(Console.ReadLine());

    if (num1 > num2 && num1 > num3){

      Console.WriteLine(String.Format("\n{0} é o maior número.", num1));

    } else if (num2 > num1 && num2 > num3){

      Console.WriteLine(String.Format("\n{0} é o maior número.", num2));

    } else if (num3 > num1 && num3 > num2) {

      Console.WriteLine(String.Format("\n{0} é o maior número.", num3));

    }  
  }
}
