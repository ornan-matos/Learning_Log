/*
Programa para demonstrar a manipulação e a impressão de um array em Go.

Este programa cria um array de strings com 4 elementos, imprime o array completo, 
e em seguida imprime os elementos do array na ordem inversa.
*/

package main

import "fmt"

func main() {
    // Inicializa um array de strings com 4 elementos.
    name := [4]string{"bra", "usa", "can", "chi"}
    
    // Imprime o array completo.
    fmt.Println(name)
    
    // Loop para iterar sobre o array na ordem inversa.
    for i := len(name) - 1; i >= 0; i-- {
        // Imprime cada elemento do array na ordem inversa.
        fmt.Printf("%s ", name[i])
    }
    
    // Adiciona uma nova linha ao final da saída.
    fmt.Println()
}