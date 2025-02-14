using System;

class codigo{

  static void Main(){

    Console.WriteLine("\nQual o código?");
    string codigo = Console.ReadLine();

    switch (codigo){

      case "1":
        Console.WriteLine("\nCódigo 1. \tValido");
        break;

      case "2":
        Console.WriteLine("\nCódigo 2. \tValido");
        break;

      case "3":
        Console.WriteLine("\nCódigo 3. \tValido");
        break;

      default:
        Console.WriteLine("\nCódigo Invalido!");
        break;

    }
  }
}
