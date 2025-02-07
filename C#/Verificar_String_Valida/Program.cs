using System;

class valido{

  static void Main(){
    Console.WriteLine("\nSeleção de Sexo");

inicio:

    Console.WriteLine("\nM...\tMasculino");
    Console.WriteLine("F...\tFeminino\n");

    string sx = Console.ReadLine();

    if (sx == "M"){
      Console.WriteLine("\nVocê selecionou Masculino");
    } else if (sx == "F"){
      Console.WriteLine("\nVocê selecionou Feminino");
    } else{
      Console.WriteLine("\nSeleção Invalida! Tente novamente.");
      goto inicio;
    }
    
  }
}
