using System;

class volume{
  static void Main(){
  
    Console.WriteLine("\nCalulo de Volume");

    Console.Write("\nInsira raio (cm): ");
    float raio = Convert.ToSingle(Console.ReadLine());
    
    Console.Write("\nInsira altura (cm): ");
    float altura = Convert.ToSingle(Console.ReadLine());

    double volume = 3.14159 * raio * raio * altura;

    Console.WriteLine(String.Format("\nVolume = {0}cm³", volume));




  }
}
