using System;

class ler{
  static void Main(){

    int[] vetor = new int[5];

    for (int n = 0; n < vetor.Length; n++){

      Console.Write("\nInsira um número: ");
      vetor[n] = Convert.ToInt32(Console.ReadLine());

    }

    foreach (int elemento in vetor){

      Console.WriteLine("\n" + elemento);

    }

  }
}
