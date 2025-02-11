using System;

class break_continue{
  static void Main(){
    int num = 0;

    while (num <= 10){
      if(num % 2 == 1){
        //Num impar
        num++;
        continue;
      }
      Console.WriteLine(num);
      num++;
    }

    while (num <= 20){
      
      num++;
      
      if (num == 15){
        break;
      }
      Console.WriteLine(num);
    }
  }
}
