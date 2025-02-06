using System;
//Por TTech Inc - Curso Programação C#
class Principal{
    static void Main(){
        Console.WriteLine("Pense num número (0-9):");
        Console.ReadLine();

        Console.WriteLine("O número é maior que 5?(s/n)");
        string res = Console.ReadLine();

        if (res == "s"){
            Console.WriteLine("O número é par?(s/n)");
            string res2 = Console.ReadLine();
            if (res2 == "s"){
                Console.WriteLine("O número é 6? (s/n)");
                string res3 = Console.ReadLine();
                if (res3 == "s"){
                    Console.WriteLine("Acertei");
                }
                else{
                    Console.WriteLine("O número é 8!");
                }
            }else{
                Console.WriteLine("O número é 7? (s/n)");
                string res3 = Console.ReadLine();
                if (res3 == "s"){
                    Console.WriteLine("Acertei");
                }
                else{
                    Console.WriteLine("O número é 9!");
                }
            }
        }
        else if(res == "n"){
            Console.WriteLine("O número é par?(s/n)");
            string res4 = Console.ReadLine();
            if (res4 == "s"){
                Console.WriteLine("O número é maior que 0?(s/n)");
                string res5 = Console.ReadLine();
                if (res5=="s"){
                    Console.WriteLine("O número é 4? (s/n)");
                    string res6 = Console.ReadLine();
                    if (res6 == "s"){
                        Console.WriteLine("Acertei!");
                    }else{
                        Console.WriteLine("O número é 2!");
                    }
                }else{
                    Console.WriteLine("O número é 0!");
                }
                
            }else{
                Console.WriteLine("O número é maior que 3?(s/n)");
            string res7 = Console.ReadLine();
            if (res7=="s"){
                Console.WriteLine("O número é 5!");
            }else{
                Console.WriteLine("É igual a 3?(s/n)");
                string res8 = Console.ReadLine();
                if (res8=="s"){
                    Console.WriteLine("Acertei!");
                }else{
                    Console.WriteLine("O número é 1!");
                }
            }
            }
        }else{
            Console.WriteLine("Não conheço essa resposta,...");
        }
        
    }
}
