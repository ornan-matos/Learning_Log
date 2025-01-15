
package main

import "fmt"

/*  
Uma closure é uma função dentro de outra função que "captura" as variáveis do seu contexto externo, permitindo que elas mantenham seu estado entre as chamadas. O código demonstra como usar closures para criar funções que compartilham e mantêm estado de maneira independente.
*/

func main() {

    // Declara uma variável 'x' no escopo da função principal.
    x := 0

    // 'increment' é uma closure que usa a variável 'x' definida no escopo da função 'main'.
    // A cada chamada, 'x' é incrementado e o valor atualizado é retornado.
    increment := func() int {
        x++ // Incrementa o valor de 'x'.
        return x // Retorna o valor atualizado de 'x'.
    }

    // Chama a função 'increment' várias vezes e imprime os resultados.
    // Como 'increment' é uma closure, a variável 'x' mantém seu estado entre as chamadas.
    fmt.Println(increment()) // Saída: 1
    fmt.Println(increment()) // Saída: 2
    fmt.Println(increment()) // Saída: 3

    fmt.Println("----------")

    // 'add' é uma função que retorna outra função, criando uma closure.
    add_2 := add() // Cria uma nova closure onde a variável 'i' está encapsulada.

    // Chama a closure retornada por 'add' e imprime os resultados.
    // Como a closure mantém o estado da variável 'i', os valores retornados aumentam a cada chamada.
    fmt.Println(add_2()) // Saída: 1
    fmt.Println(add_2()) // Saída: 2
    fmt.Println(add_2()) // Saída: 3
}

// A função 'add' retorna uma closure que encapsula a variável 'i'.
// A variável 'i' mantém seu estado mesmo após a saída da função 'add'.
func add() func() int {
    i := 0 // Variável 'i' é inicializada no escopo da função 'add'.

    // Retorna uma função anônima que incrementa e retorna 'i'.
    return func() int {
        i++ // Incrementa 'i' a cada chamada.
        return i // Retorna o valor atualizado de 'i'.
    }
}
