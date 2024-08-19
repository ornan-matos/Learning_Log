// Programa Go que demonstra o uso de slices e arrays
// Este código cria um array de números de ponto flutuante e, 
// em seguida, cria um slice que é uma fatia desse array.
// O slice é então impresso para mostrar os elementos que ele contém.

package main

import "fmt"

func main() {
    // Criação de um array de 5 elementos do tipo float64
    arr := [5]float64{1, 2, 3, 4, 5}

    // Criação de um slice que começa no índice 0 e vai até o índice 3 do array (não incluindo o índice 4)
    x := arr[0:4]

    // Imprime o slice, que deve conter os elementos [1, 2, 3, 4]
    fmt.Println(x)
}
