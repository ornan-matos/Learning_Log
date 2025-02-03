using System;

class salario{

  static void Main(){

    Console.WriteLine("\nCalculo de Salário\n");

    Console.WriteLine("\nQuantas horas você trabalha por semana:");
    int horas_sem = Convert.ToInt16(Console.ReadLine());
    
    Console.WriteLine("\nQuanto você ganha por hora:");
    int valor_hora = Convert.ToInt16(Console.ReadLine());

    float salario = valor_hora * (horas_sem * 4); 

    Console.WriteLine(String.Format("\nGanhos mensais:\nR$ {0}",salario ));

  }
}
