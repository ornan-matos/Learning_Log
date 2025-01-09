// Programa para multiplicar os elementos de um array por 3
// e armazenar os resultados em um novo array.

package main

import "fmt"

func main() {

    // Declaração do array original com os valores fornecidos.
    a := [5]int{2, 4, 6, 8, 10}
    var b [5]int // Declaração do array para armazenar os resultados.

    // Loop para multiplicar cada elemento de 'a' por 3 e armazenar em 'b'.
    for i := 0; i < len(a); i++ {
        b[i] = a[i] * 3
    }

    // Exibe os arrays originais e modificados.
    fmt.Println("Lista A:", a) // Exibe os valores originais.
    fmt.Println("Lista B:", b) // Exibe os valores multiplicados.
}

