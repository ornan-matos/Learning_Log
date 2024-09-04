package main

import "fmt"

/* 

FizzBuzz é um clássico problema de programação que imprime números de 0 a 100.
Para múltiplos de 3, imprime "Fizz".
Para múltiplos de 5, imprime "Buzz".
Para múltiplos de ambos 3 e 5, imprime "FizzBuzz".
Caso contrário, imprime o número.

*/

func main() {
    // Loop de 0 até 100
    for i := 0; i <= 100; i++ {
        // Verifica se o número é múltiplo de 3 e 5
        if i % 3 == 0 && i % 5 == 0 {
            fmt.Println("FizzBuzz")
        // Verifica se o número é múltiplo de 3
        } else if i % 3 == 0 {
            fmt.Println("Fizz")
        // Verifica se o número é múltiplo de 5
        } else if i % 5 == 0 {
            fmt.Println("Buzz")
        // Se não for múltiplo de 3 ou 5, imprime o número
        } else {
            fmt.Println(i)
        }
    }
}
