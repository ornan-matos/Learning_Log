using System;

class cota{
  static void Main(){
    Console.WriteLine("\nConversor U$ -> R$\n");

    Console.Write("\nCotação Dolar: U$ ");
    float cotacao = Convert.ToSingle(Console.Read());

    Console.Write("\nValor para Converter: U$ ");
    float valor = Convert.ToSingle(Console.Read());

    float dolar = cotacao * valor;

    Console.WriteLine()
  }
}
