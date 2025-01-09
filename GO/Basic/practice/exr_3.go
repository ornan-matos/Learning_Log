// Programa para calcular a média de duas notas fornecidas pelo usuário.

package main

import "fmt"

func main() {

    // Declaração de um array para armazenar duas notas.
    var n [2]float32
    var total float32 // Variável para armazenar o total das notas.

    // Loop para capturar as notas e calcular o total.
    for i := 0; i < len(n); i++ {
        fmt.Printf("Insira o valor da nota %d: ", i+1) // Solicita a entrada do usuário.
        fmt.Scan(&n[i]) // Lê a entrada e armazena no array.
        total += n[i] // Soma a nota ao total.
    }

    // Exibe o total e a média das notas.
    fmt.Println("Total =", total)
    fmt.Println("Média =", total/float32(len(n)))
}

