using System;

class entrada{
  static void Main(){
    Console.WriteLine("Digite seu nome:");
    string res = Console.ReadLine();
    Console.WriteLine($"Obrigado, {res}!");
    Console.WriteLine("Tudo Ok,"+res);

    //double > float > long > int > char
    //Conversão Implicita -> do menor para o maior
    int num1 = 10;
    float num2 = num1;
    Console.WriteLine(num2);

    //Conversão Explicita -> do maior para o menor
    num2 = 10.5f;
    int num3 = (int)num2; //TypeCast
    Console.WriteLine(num3);

  }
}
