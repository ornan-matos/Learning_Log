using System;

class operadores{
  static void Main(){
    
    bool b1 = true;
    bool b2 = true;
    bool b3 = false;
    bool b4 = false;

    bool exp = b3 && b4; //AND (e)
    
    bool exp2 = b1 || b3; //OR (ou)

    bool exp3 = b4 || b3; //OR (ou)

    bool exp4 = b1 == b2 && b3 == b4;

    Console.WriteLine($"{exp}, {exp2}, {exp3}, {exp4}");

    Console.WriteLine($"{!b1}, {!b3}");

    Console.WriteLine(!(b1 == b2));

  }
}
