using System;

class verificar{
  static void Main(){
    Console.Write("\nInsira um número: ");
    int num = Convert.ToInt32(Console.ReadLine());

    if (num.GetType() == typeof(Int32)){
      Console.WriteLine("\nÉ um número inteiro! (" + num.GetType() +")");
    } else{
      Console.WriteLine("\nNão é do mesmo formato!");
    }
  }
}
