using System;

class metodos{
  static void Main(){
    int[] vetor = {1,2,3,4,5};

    //Posição do valor definido
    int pos = Array.BinarySearch(vetor, 3);
    Console.WriteLine(pos);
    
    //Conteúdo da posição definida
    object pos2 = vetor.GetValue(3);
    Console.WriteLine(pos2);

    //Menor valor do index do array
    int min_index = vetor.GetLowerBound(0);
    //Maior valor do index do array
    int max_index = vetor.GetUpperBound(0);

    Console.WriteLine(String.Format("\nMenor valor do index:{0}\nMaior valor do index:{1}\n", min_index, max_index));

    Array.Reverse(vetor);
    foreach(int n in vetor){
      Console.WriteLine(n);
    }

  }
}
