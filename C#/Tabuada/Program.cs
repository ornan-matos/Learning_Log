using System;

class tabuada{
  static void Main(){

    Console.WriteLine("\nOperação Matemática");

inicio:

    Console.WriteLine("\n[1]\tAdição\n[2]\tSubtração\n[3]\tMultiplicação\n[4]\tDivisão");
    string op = Console.ReadLine();

    Console.Write("\nNúmero para aplicar operação: ");
    int num = Convert.ToInt32(Console.ReadLine());

    switch(op){

      case "1":
        Console.WriteLine("\nOperações Tabuada de Adição");
        for(int n = 1; n <= 10; n++){
          int result = num + n;
          Console.WriteLine(String.Format("{0} + {1} = {2}", n, num, result));
        }
        break;

      case "2":
        Console.WriteLine("\nOperações Tabuada de Subtração");
        for(int n = 1; n <= 10; n++){
          int result = num - n;
          Console.WriteLine(String.Format("{0} - {1} = {2}", n, num, result));
        }
        break;

      case "3":
        Console.WriteLine("\nOperações Tabuada de Multiplicação");
        for(int n = 1; n <= 10; n++){
          int result = num * n;
          Console.WriteLine(String.Format("{0} x {1} = {2}", n, num, result));
        }
        break;

      case "4":
        Console.WriteLine("\nOperações Tabuada de Divisão");
        for(int n = 1; n <= 10; n++){
          int result = num / n;
          Console.WriteLine(String.Format("{0} / {1} = {2}", n, num, result));
        }
        break;

      default:
        Console.WriteLine("\nOperação invalida, tente novamente!");
        goto inicio;
    }
  }
}
