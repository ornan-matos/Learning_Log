using System;

class Array_{
  static void Main(){

    int[] Vetor1 = new int[4]{10,20,30,50};

    Vetor1[3] = 40;

    for (int i = 0; i < Vetor1.Length; i++){
      Console.WriteLine(Vetor1[i]);
    }
  }
}
