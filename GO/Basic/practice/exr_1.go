// Programa para preencher um array com os números de 0 a 10
// e imprimir cada elemento à medida que é preenchido.

package main

import "fmt"

func main() {

    // Declaração de um array com 11 posições, inicializado com zeros.
    var x [11]int

    // Loop para preencher o array com os índices (0 a 10) e imprimir os valores.
    for i := 0; i < len(x); i++ {
        x[i] += i // Atribui ao elemento atual o valor do índice.
        fmt.Println(x[i]) // Exibe o valor do elemento preenchido.
    }
}

