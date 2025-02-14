using System;

class decresente{
  static void Main(){

    int[] num = new int[3];

    for (int n = 0; n < num.Length; n++){

      Console.Write("\nInsira um número: ");
      num[n] = Convert.ToInt32(Console.ReadLine());

    }
    

    if (num[0] >= num[1] && num[0] >= num[2]){
      Console.WriteLine("\n" + num[0]);
      if (num[1] >= num[2]){
        Console.WriteLine("\n" + num[1]);
        Console.WriteLine("\n" + num[2]);
      }
      else {
        Console.WriteLine("\n" + num[2]);
        Console.WriteLine("\n" + num[1]);
      }
    }
    else if (num[1] >= num[0] && num[1] >= num[2]){
      Console.WriteLine("\n" + num[1]);
      if (num[0] >= num[2]){
        Console.WriteLine("\n" + num[0]);
        Console.WriteLine("\n" + num[2]);
      }
      else {
        Console.WriteLine("\n" + num[2]);
        Console.WriteLine("\n" + num[0]);
      }
    }
    else {
      Console.WriteLine("\n" + num[2]);
      if (num[0] >= num[1]){
        Console.WriteLine("\n" + num[0]);
        Console.WriteLine("\n" + num[1]);
      }
      else {
        Console.WriteLine("\n" + num[1]);
        Console.WriteLine("\n" + num[0]);
      }
    }
  }
}
