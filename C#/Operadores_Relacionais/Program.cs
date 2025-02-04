using System;

class operadores{
  static void Main(){
    //Operadores Relacionais
    int n1 = 10;
    int n2 = 20;
    int n3 = 10;

    bool v1 = n1 == n3; //Igualdade
    bool v2 = n1 != n2; //Diferença

    bool v3 = n1 > n2; //Maior que
    bool v4 = n3 < n2; //Menor que

    bool v5 = n1 >= n3; //Maior ou igual
    bool v6 = n2 <= n1; //Menor ou igual

    Console.WriteLine(v5);

  }
}
