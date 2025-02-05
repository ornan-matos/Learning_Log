using System;

class condicional{
  static void Main(){
    Console.Write("\nInsira sua idade: ");
    Int16 idade = Convert.ToInt16(Console.ReadLine());
    
    if (idade >= 18){
      Console.WriteLine("\nVenda autorizada!");
    }
    else{
      Console.WriteLine("\nVenda proibida!"); }
  }
}
