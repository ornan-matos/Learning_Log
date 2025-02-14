using System;

class verificar{
  static void Main(){

    Console.WriteLine("\nVerifique se foi aprovado");

    Console.Write("Insira a nota de Português: ");
    float port = Convert.ToSingle(Console.ReadLine());

    Console.Write("Insira a nota de Matemática: ");
    float mat = Convert.ToSingle(Console.ReadLine());

    Console.Write("Insira a nota de Geografia: ");
    float geo = Convert.ToSingle(Console.ReadLine());

    Console.Write("Insira a nota de Biologia: ");
    float bio = Convert.ToSingle(Console.ReadLine());

    float media = (port + mat + geo + bio) / 4;

    if (media >= 7){

      Console.WriteLine("\nVocê foi aprovado, parabéns!");

    }

    else {

      Console.WriteLine("\nVocê foi reprovado!");

    }

    Console.WriteLine("------------------------------");

    Console.WriteLine(String.Format("Português: \t{0:F2}\nMatemática: \t{1:F2}\nGeografia: \t{2:F2}\nBiologia: \t{3:F2}",port, mat, geo, bio));

   Console.WriteLine("------------------------------");

   Console.WriteLine(String.Format("\nMedia Geral: \t{0:F2}", media));

 }
}
