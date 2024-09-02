/*
Programa em Go para imprimir números de 0 a 99 que são múltiplos de 3.
Este programa utiliza um loop para iterar de 0 até 99 e verifica se cada número
é múltiplo de 3. Se for, o número é impresso na tela.
*/

package main

import "fmt"

func main() {
    
// Loop que vai de 0 a 99
    for i := 0; i < 100; i++ {
        
	// Verifica se o número atual é múltiplo de 3
        if i % 3 == 0 {
            
	// Imprime o número se for múltiplo de 3
            fmt.Println(i)
        }
    }
}