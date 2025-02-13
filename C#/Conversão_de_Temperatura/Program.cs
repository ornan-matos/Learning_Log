using System;

class conversao{
  static void Main(){

    Console.WriteLine("\nConverção de Celsius para Fahrenheit");

    Console.Write("\nInsira a temperatura em Celsius: ");
    float celsius = Convert.ToSingle(Console.ReadLine());

    float fahrenheit = (9 * celsius + 160) / 5;

    Console.WriteLine(String.Format("{0} ºC\n{1} ºF", celsius, fahrenheit));

    Console.WriteLine("--------------------------");

    Console.WriteLine("\nConverção de Fahrenheit para Celsius");
    
    Console.Write("\nInsira a temperatura em Fahrenheit: ");
    float fahrenheit2 = Convert.ToSingle(Console.ReadLine());

    float celsius2 = (fahrenheit2 - 32) * 5 / 9;

    Console.WriteLine(String.Format("{0} ºF\n{1} ºC", fahrenheit2, celsius2));

  }
}
