using System;

class media{
  static void Main(){
    Console.WriteLine("Media Notas");
    
    Console.WriteLine("\nMatématica");
    float nota1 = Convert.ToSingle(Console.ReadLine());

    Console.WriteLine("\nPortuguês");
    float nota2 = Convert.ToSingle(Console.ReadLine());


    Console.WriteLine("\nBiologia");
    float nota3 = Convert.ToSingle(Console.ReadLine());

    Console.WriteLine("\nGeografia");
    float nota4 = Convert.ToSingle(Console.ReadLine());

    float media = (nota1 + nota2 + nota3 + nota4) / 4;

    Console.WriteLine("\nResultado Media: " + media);

  }
}
