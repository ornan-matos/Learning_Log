using System;

class triangulo{
  static void Main(){
    Console.Write("\nInsira o lado A: ");
    int a = Convert.ToInt32(Console.ReadLine());
    
    Console.Write("\nInsira o lado B: ");
    int b = Convert.ToInt32(Console.ReadLine());
    
    Console.Write("\nInsira o lado C: ");
    int c = Convert.ToInt32(Console.ReadLine());

    if (a < b + c && b < a + c && c < a + b){
      if (a == b && b == c){
        Console.WriteLine("\nTriângulo Equilátero");
      }
      else if (a == b || a == c || b == c){
        Console.WriteLine("\nTriângulo Isóceles");
      }
      else {
        Console.WriteLine("\nTriângulo Escaleno");
      }
    }
    else {
        Console.WriteLine("\nNão é um Triângulo!");
    }
  }
}
