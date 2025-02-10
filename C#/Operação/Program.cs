using System;

class operação{
  static void Main(){
    Console.WriteLine("\nOperação Matemática");

    Console.Write("\nInsira o primeiro número: ");
    float num1 = Convert.ToSingle(Console.ReadLine());

    Console.Write("\nInsira o segundo número: ");
    float num2 = Convert.ToSingle(Console.ReadLine());

inicio:
    Console.WriteLine("\nQual operação matemática deseja realizar?");
    Console.WriteLine("\n1...\tAdição\n2...\tSubtração\n3...\tMultiplicação\n4...\tDivisão\n");

    string op = Console.ReadLine();

    switch (op){
      case "1":
        float res = num1 + num2;
        Console.WriteLine(String.Format("\n{0} + {1} = {2}", num1, num2, res));
        break;

      case "2":
        float res2 = num1 - num2;
        Console.WriteLine(String.Format("\n{0} - {1} = {2}", num1, num2, res2));
        break;

      case "3":
        float res3 = num1 * num2;
        Console.WriteLine(String.Format("\n{0} x {1} = {2}", num1, num2, res3));
        break;

      case "4":
        float res4 = num1 - num2;
        Console.WriteLine(String.Format("\n{0} / {1} = {2}", num1, num2, res4));
        break;

      default:
        Console.WriteLine("\nOperação não reconhecida. Tente novamente!");
        goto inicio;

    }


 }
}
