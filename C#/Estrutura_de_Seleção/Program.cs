using System;

class seleção{
  static void Main(){
    Console.WriteLine("\nMenu");
inicio:
    Console.WriteLine("\n[1]...Entrar");
    Console.WriteLine("[2]...Opções");
    Console.WriteLine("[3]...Sair\n");

    string res = Console.ReadLine();

    switch(res){

      case "1":
        Console.WriteLine("\nEntrou no Programa com sucesso!");
        break;

      case "2":
        Console.WriteLine("\nAqui estão as opções ->");
        break;

      case "3":
        Console.WriteLine("\nSaindo do Programa.");
        break;

      default:
        Console.WriteLine("\nOpção não reconhecida, tente novamente.\n");
        goto inicio;

    }
  }
}
