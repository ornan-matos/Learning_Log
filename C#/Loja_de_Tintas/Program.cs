/*
O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total
 */
using System;

class loja{
  static void Main(){
    Console.WriteLine("\n-- Loja de Tintas --\n");

    Console.WriteLine("\nInsira o tamano em Metros Quadrados:");
    float tamanho = Convert.ToSingle(Console.ReadLine());

    int litros = Convert.ToInt32(tamanho) * 3;

    int latas = litros / 18;

    int valor = latas * 80;

    Console.WriteLine(String.Format("\nResultado -->\n"));
    Console.WriteLine(String.Format("{0} m2\n{1} latas de tinta\nR${2}.00",tamanho, latas, valor));


    



  }
}
