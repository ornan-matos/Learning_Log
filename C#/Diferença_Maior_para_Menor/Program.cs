using System;

class diferença{
  static void Main(){

    Console.Write("\nInsira o primeiro número: ");
    int num1 = Convert.ToInt32(Console.ReadLine());
    
    Console.Write("\nInsira o segundo número: ");
    int num2 = Convert.ToInt32(Console.ReadLine());
    
    if (num1 > num2){

      int dif = num1 - num2;
      Console.WriteLine("\nDiferença = " + dif);

    }

    else if (num2 > num1){

      int dif = num2 - num1;
      Console.WriteLine("\nDiferença = " + dif);
    }
    
    else{
      Console.WriteLine("\nOs número são iguais!");
    }

  }
}
