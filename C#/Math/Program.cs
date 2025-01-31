using System;

class aritimetica{
  static void Main(){
    //Potencia
    double pot = Math.Pow(4,4);
    Console.WriteLine(pot + Math.Pow(2,3));
    //Raiz Quadrada
    Console.WriteLine(Math.Sqrt(27));
  
    //Arredonda ao mais próximo
    Console.WriteLine(Math.Round(3.5));
    //Arredonda para cima
    Console.WriteLine(Math.Ceiling(3.4));
    //Arredonda para baixo
    Console.WriteLine(Math.Floor(3.4));

    Console.WriteLine(Math.Max(3,7)); //Maior número
    Console.WriteLine(Math.Min(3,7)); //Menor número
  }
}
