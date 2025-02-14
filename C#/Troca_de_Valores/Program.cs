using System;

class troca{

  static void Main(){
    Console.Write("\nInsira o valor da variável A: ");
    int A = Convert.ToInt32(Console.ReadLine());

    Console.Write("\nInsira o valor da variável B: ");
    int B = Convert.ToInt32(Console.ReadLine());

    int C = B;

    B = A;

    A = C;

    Console.WriteLine(String.Format("\nVariável A: {0}\nVariável B: {1}", A, B));


  }
}
