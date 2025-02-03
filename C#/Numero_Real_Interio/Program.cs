using System;

class real_int{
  static void Main(){

    Console.WriteLine("\nInsira o primeiro número inteiro:");
    int num_1 = Convert.ToInt16(Console.ReadLine());

    Console.WriteLine("\nInsira o segundo número inteiro:");
    int num_2 = Convert.ToInt16(Console.ReadLine());

    Console.WriteLine("\nInsira o número real:");
    double real = Convert.ToDouble(Console.ReadLine());

    double produto = ((Math.Pow(num_1, 2)) + (num_2 / 2));
    double produto_2 = ((num_1 * 3) + (real * 3));
    double produto_3 = Math.Pow(real, 3);

    Console.WriteLine("\nProduto do dobro do primeiro com metade do segundo: " + produto);
    Console.WriteLine("\nSoma do triplo do primeiro com o terceiro: " + produto_2);
    Console.WriteLine("\nTerceiro elevado ao cubo: " + produto_3);

  }
}
