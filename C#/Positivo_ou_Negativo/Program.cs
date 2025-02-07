using System;

class p_ou_v{
  static void Main(){
    Console.WriteLine("\nPositivo ou Negativo");

inicio:
    Console.Write("\nInsira um valor: ");
    int num = Convert.ToInt32(Console.ReadLine());

    if (num > 0){
      Console.WriteLine(String.Format("\n{0} é positivo.", num));
    } else if (num < 0){
      Console.WriteLine(String.Format("\n{0} é negativo.", num));
    } else {
      Console.WriteLine(String.Format("\n{0} é neutro. Tente novamente", num));
      goto inicio;
    }
  }
}
