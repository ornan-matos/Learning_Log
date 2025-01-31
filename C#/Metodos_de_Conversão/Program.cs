using System;

class metodos{
  static void Main(){
    //Metodos para Conversão

    //Convesão de string para int
    string op_1 = "2";

    int num = Convert.ToInt32(op_1);

    Console.WriteLine(num);

    //Converter uma entrada
    Console.WriteLine("Insira o primeiro número:");

    int num2 = Convert.ToInt32(Console.ReadLine());

    Console.WriteLine("Insira o segundo número:");

    int num3 = Convert.ToInt32(Console.ReadLine());

    //Constante
    const int num4 = 10;

    int resul = num2 + num3 - 10;

    Console.WriteLine("Resultado da soma de " + num2 + " + " + num3 + " - " + num4 + " = " + resul);
    
  }
}
