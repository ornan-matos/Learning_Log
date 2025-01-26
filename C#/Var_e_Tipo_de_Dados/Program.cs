using System;

class variavel{
  static void Main(){
    //Estrutura: tipo nome = valor
    //
    //String -> Texto, Aspas Duplas
    string texto1 = "Hello, world!";
    Console.WriteLine(texto1);

    //Char -> Caractere, Aspas Simples
    char letra = 'b';
    Console.WriteLine(letra);

    //Tipos de dados Númericos Inteiros
    
    //-128 a 127
    sbyte num1 = 127;
    //0 a 255
    byte num2 = 255;
    //-32.768 a 32.767
    short num3 = 1000;
    //0 a 65.535
    ushort num4 = 65534;
    //-2.147.483.648 a 2.147.483.647
    int num5 = 2147483647;
    //0 a 4.294.967.295
    uint num6 = 4294967295;
    //-9.223.372.036.854.775.808 a 9.223.372.036.854.775.807
    long num7 = 9223372036854775807;
    //0 a 18.446.744.073.709.551.615
    ulong num8 = 18446744073709551615;

    //Interpolação de Strings
    Console.WriteLine($"{num1}\n {num2}\n {num3}\n {num4}\n {num5}\n {num6}\n {num7}\n {num8}");

  }
}
