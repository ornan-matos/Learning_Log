// O programa a seguir conta e imprime o número de elementos pares em um array de inteiros de tamanho 10.
// O array é inicializado com valores de 1 a 10. O código percorre o array e conta quantos desses valores são pares.

package main

import "fmt"

func main() {
    // Inicializa um array de inteiros com valores de 1 a 10
    num := [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    // Variável para contar o número de elementos pares
    x := 0

    // Loop para percorrer cada elemento do array
    for i := 0; i < 10; i++ {
        // Verifica se o elemento atual é par
        if num[i] % 2 == 0 {
            x++ // Incrementa o contador de números pares
        }
    }

    // Imprime o total de números pares encontrados no array
    fmt.Println("Número de pares no array:", x)
}
