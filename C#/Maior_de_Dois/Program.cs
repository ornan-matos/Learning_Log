using System;

class maior{
  static void Main(){
    Console.WriteLine("\nMaior de dois números");

    Console.Write("\nInsira o primeiro número: ");
    int num1 = Convert.ToInt32(Console.ReadLine());
    
    Console.Write("\nInsira o segundo número: ");
    int num2 = Convert.ToInt32(Console.ReadLine());

    if (num1 > num2){

      Console.WriteLine(String.Format("\nO número {0} é o maior.", num1));

    } else if (num1 < num2){

      Console.WriteLine(String.Format("\nO número {0} é o maior.", num2));

    } else {

      Console.WriteLine(String.Format("\nOs números {0}, {1} são iguais!", num1, num2));

    }

  }
}
