/*
O programa imprime os números de 0 a 50. Para cada número:
- Se o número é divisível por 3 e 5, imprime "FizzBuzz".
- Se o número é divisível apenas por 3, imprime "Fizz".
- Se o número é divisível apenas por 5, imprime "Buzz".
- Caso contrário, o número não é impresso.

Esta é uma implementação do clássico problema "FizzBuzz".
*/

package main

import "fmt"

func main() {
  // Loop de 0 a 50 (inclusive)
  for i := 0; i <= 50; i++ {

    // Verifica se o número é divisível por 3 e 5
    if i % 3 == 0 && i % 5 == 0 {
      fmt.Printf("%d - FizzBuzz\n", i)
    // Verifica se o número é divisível apenas por 3
    } else if i % 3 == 0 {
      fmt.Printf("%d - Fizz\n", i)
    // Verifica se o número é divisível apenas por 5
    } else if i % 5 == 0 {
      fmt.Printf("%d - Buzz\n", i)
    }
  }
}