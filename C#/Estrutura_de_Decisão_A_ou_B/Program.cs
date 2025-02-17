using System;

class a_b{
  static void Main(){

    // Se positivo armazene-o em A, se for negativo, em B. No final mostrar o resultado.

    Console.Write("\nInsira um número: ");
    int num = Convert.ToInt32(Console.ReadLine());

    int a;
    int b;

    if (num >= 0){
      a = num;
      Console.WriteLine(String.Format("\nArmazenado em A: {0}", a));
    }
    else {
      b = num;
      Console.WriteLine(String.Format("\nArmazenado em B: {0}", b));

    }
  }
}
