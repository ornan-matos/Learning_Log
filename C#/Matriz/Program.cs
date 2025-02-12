using System;

class matriz{
  static void Main(){
    int[,] mat = new int[3,3];

    mat[0,0] = 15; mat[0,1] = 30; mat[0,2] = 60;
    mat[1,0] = 10; mat[1,1] = 45; mat[1,2] = 32;
    mat[2,0] = 23; mat[2,1] = 38; mat[2,2] = 90;

    Console.WriteLine(mat[0,2]);
  }
}
