using System;

class comissao{
  static void Main(){

    Console.WriteLine("\nNome do Vendedor:");
    string nome = Console.ReadLine();

    Console.WriteLine("\nCódigo:");
    int codigo = Convert.ToInt32(Console.ReadLine());

    Console.WriteLine("\nPreço: R$ ");
    float preco = Convert.ToSingle(Console.ReadLine());

    Console.WriteLine("\nQuantidade: ");
    int quantidade = Convert.ToInt32(Console.ReadLine());

    float total = (preco * quantidade) * 0.05f;

    Console.WriteLine(String.Format("\n{0} você vendeu {1} peça(s)\nComissão: R${2:F2}", nome, quantidade, total));
  }
}
