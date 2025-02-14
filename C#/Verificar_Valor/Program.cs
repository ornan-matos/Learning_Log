using System;

class verificar{

  static void Main(){

    Console.Write("Insira o valor: ");
    int num = Convert.ToInt32(Console.ReadLine());

    if (num >= 0 && num <= 9){

      Console.WriteLine("\nValor valido!");

    }

    else {

      Console.WriteLine("\nValor invalido!");

    }
  }
}
