using System;

class hora{
    static void Main(){
      
inicio:

      Console.Write("\nInsira o horario(Formato 24h / Não insira os minutos): ");

      int hora = Convert.ToInt32(Console.ReadLine());

      if (hora >= 1 && hora < 5){
        Console.WriteLine("\nBoa noite!");
      }
      else if (hora >= 5 && hora < 12){
        Console.WriteLine("\nBom dia!");
      } 
      else if (hora >= 12 && hora < 18){
        Console.WriteLine("\nBoa tarde!");
      }
      else if (hora >= 18 && hora <= 24){
        Console.WriteLine("\nBoa noite!");
      }
      else {
        Console.WriteLine("\nHora invalida, tente novamente.");
        goto inicio;
      }

    }
}
