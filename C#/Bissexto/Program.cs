using System;

class bissexto{
    static void Main(){
      Console.WriteLine("\nDescubra se o ano é Bissexto\n");

      Console.Write("Insira o ano: ");
      int ano = Convert.ToInt32(Console.ReadLine());

      if (ano % 4 == 0 && ano % 100 == 0 && ano % 400 == 0){
        Console.WriteLine(String.Format("\n{0} é bissexto!", ano));
      } else {
        Console.WriteLine(String.Format("\n{0} não é bissexto!", ano));
      }
    }
}
