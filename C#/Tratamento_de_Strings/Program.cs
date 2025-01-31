using System;

class tratamento{
  static void Main(){
    //Tratamento de Strings

    //Formatação de String
    Console.WriteLine("Insira um texto para converte-lo:");
    string frase = Console.ReadLine();

    Console.WriteLine("\nCaixa Alta:");
    Console.WriteLine(frase.ToUpper());

    Console.WriteLine("\nCaixa Baixa:");
    Console.WriteLine(frase.ToLower());

    Console.WriteLine("\nInsira seu nome:");
    string nome = Console.ReadLine();
    Console.WriteLine(String.Format("\nOlá {0}, bem vindo!", nome));
  }
}
