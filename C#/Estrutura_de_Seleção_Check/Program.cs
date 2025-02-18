using System;

class check{
  static void Main(){
    Console.Write("\nInsira o primeiro número: ");
    int num1 = Convert.ToInt32(Console.ReadLine());
    
    Console.Write("\nInsira o segundo número: ");
    int num2 = Convert.ToInt32(Console.ReadLine());

inicio:

    Console.WriteLine("\n--------------------------------------------------------------------");
    Console.WriteLine("\n1...\tVerificar se um dos números lidos é ou não múltiplo do outro.");
    Console.WriteLine("\n2...\tVerificar se os dois números lidos são pares.");
    Console.WriteLine("\n3...\tVerificar se a média dos dois números é maior ou igual a 7.");
    Console.WriteLine("\n4...\tSair.\n");

    string op = Console.ReadLine();

    switch (op){
      case "1":
        if (num1 % num2 == 0 || num2 % num1 == 0 ){
          if (num1 % num2 == 0){
            Console.WriteLine(String.Format("\n{0} é multiplo de {1}", num1, num2));
          }
          else if (num2 % num1 == 0){
            Console.WriteLine(String.Format("\n{0} é multiplo de {1}", num2, num1));
          }
        }
        else {
          Console.WriteLine(String.Format("\nNem um dos dois número é multiplo um do outro."));
        }
        break;

      case "2":
        if (num1 % 2 == 0 && num2 % 2 == 0){
          Console.WriteLine(String.Format("\nOs dois número são pares."));
        }
        else{
          Console.WriteLine(String.Format("\nAmbos (ou algum dos números) não são pares."));
        }
        break;

      case "3":
        if ((num1 + num2) / 2 >= 7){
          Console.WriteLine("\nA media dos dois número é maior ou igual a 7.");
        }
        else {
          Console.WriteLine("\nA media dos dois número é menor que 7.");
        }
        break;

      case "4":
        Console.WriteLine("\nFechando o Programa.");
        break;

      default:
        Console.WriteLine("\nA opção escolhida não foi reconhecida. Tente novamente!");
        goto inicio;
        break;

    }

  }
}
