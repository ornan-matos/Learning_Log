package main

import "fmt"

/* 
Este programa implementa e utiliza uma função recursiva em Go para calcular
números da sequência de Fibonacci. A sequência de Fibonacci é definida como:
F(0) = 0, F(1) = 1 e F(n) = F(n-1) + F(n-2) para n > 1.
O programa exibe o resultado para diferentes entradas fornecidas na função main.
*/

func main() {
    // Testa a função Fibonacci com diferentes valores de entrada e exibe os resultados
    fmt.Println(fibonacci(0))  // Exibe o 0º número da sequência (0)
    fmt.Println(fibonacci(1))  // Exibe o 1º número da sequência (1)
    fmt.Println(fibonacci(6))  // Exibe o 6º número da sequência (8)
    fmt.Println(fibonacci(10)) // Exibe o 10º número da sequência (55)
}

// Função recursiva para calcular o n-ésimo número da sequência de Fibonacci
func fibonacci(x int) int {
    if x == 0 {
        // Caso base: se x é 0, retorna 0
        return x
    } else if x == 1 {
        // Caso base: se x é 1, retorna 1
        return x
    } else {
        // Caso recursivo: retorna a soma dos dois números anteriores na sequência
        return fibonacci(x - 1) + fibonacci(x - 2)
    }
}

