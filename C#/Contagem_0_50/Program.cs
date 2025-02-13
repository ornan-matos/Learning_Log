using System;

class contagem{
  static void Main(){

    int[] vetor = new int[51];

    for (int n = 0; n < vetor.Length; n++){
      vetor[n] = n;
      Console.WriteLine(vetor[n]);
    }
  }
}
