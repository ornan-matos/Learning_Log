using System;
 
class intervalo
{
    static void Main() {
 
        Console.Write("\nInsira o primeiro número: ");
        int num1 = Convert.ToInt32(Console.ReadLine());
 
        Console.Write("\nInsira o segundo número: ");
        int num2 = Convert.ToInt32(Console.ReadLine());
 
 
 
        for (int diferenca = num1 - num2; diferenca <= 0; diferenca--){
            if (num1 <= num2)
            {
                Console.WriteLine(num1);
                num1++;
            }
        }
    }
}
