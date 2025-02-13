using System;

class inverso{
  static void Main(){

    int[] vetor = new int[10];

    for (int n = 0; n < vetor.Length; n++){
      Console.Write("\nInsira um número: ");
      vetor[n] = Convert.ToInt32(Console.ReadLine());
    }

    Array.Reverse(vetor);
    foreach (int n in vetor){
      Console.WriteLine("\n" + n);
    }
  }
}
