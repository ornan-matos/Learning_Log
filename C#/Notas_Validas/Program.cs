using System;

class notas{
  static void Main(){

inicio:
    Console.Write("\nInsira nota (0 a 10): ");
    float nota = Convert.ToSingle(Console.ReadLine());

    if (nota >= 0 && nota <= 10){
      Console.WriteLine("\nValor valido!");
    } else {
      Console.WriteLine("\nValor invalido! Tente novamente!");
      goto inicio;
    } 
  }

}
