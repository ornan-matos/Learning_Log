using System;

class realcionamento{
  static void Main(){
    Console.Write("\nInsira o primeiro número: ");
    int num1 = Convert.ToInt32(Console.ReadLine());
    
    Console.Write("\nInsira o segundo número: ");
    int num2 = Convert.ToInt32(Console.ReadLine());

    if (num1 == num2){
      Console.WriteLine("\nOs número são iguais.");
    } 

    else {
      Console.WriteLine("\nOs número são diferentes.");

      if (num1 > num2){
        Console.WriteLine(String.Format("\n{0} é maior que {1}", num1, num2));
      }
      else if (num1 < num2){
        Console.WriteLine(String.Format("\n{0} é menor que {1}", num1, num2));
      }
    } 

  }
}
