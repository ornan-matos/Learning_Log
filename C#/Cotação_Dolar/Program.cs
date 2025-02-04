using System;

class cota{
  static void Main(){
    Console.WriteLine("\nConversor U$ -> R$\n");

    Console.WriteLine("\nCotação Dolar: R$ ");
    float cotacao = Convert.ToSingle(Console.ReadLine());

    Console.WriteLine("\nValor para Converter: U$ ");
    float valor = Convert.ToSingle(Console.ReadLine());

    float dolar = cotacao * valor;

    Console.WriteLine(String.Format("\nCotação R$ {0:F2} \nValor U$ {1:F2}\nU$ {2:F2}", cotacao, valor, dolar));
  }
}
