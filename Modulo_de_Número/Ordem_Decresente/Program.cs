using System;

class decresente{
  static void Main(){

    int[] num = new int[3];

    for (int n = 0; n < num.Length; n++){

      Console.Write("\nInsira o primeiro número: ");
      num[n] = Convert.ToInt32(Console.ReadLine());

    }

    Array.Reverse(num);

    foreach (int n in num){
      Console.WriteLine("\n" + n);
    }
  }
}
