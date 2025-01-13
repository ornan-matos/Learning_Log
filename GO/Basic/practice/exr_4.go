
/*
Programa para encontrar o maior e o menor número em uma lista de inteiros.
*/

package main

import "fmt"

func main() {

  // Array de inteiros para análise
  x := []int{
    48, 96, 86, 68,
    57, 82, 63, 70,
    37, 34, 83, 27,
    19, 97, 9, 17,
  }

  // Encontrar o maior número
  var mn int = x[0] // Inicializa com o primeiro valor do array
  for _, v := range x {
    if v > mn { // Atualiza mn se encontrar um número maior
      mn = v
    }
  }

  fmt.Println("Maior número: ", mn) // Exibe o maior número

  // Encontrar o menor número
  var men int = x[0] // Inicializa com o primeiro valor do array
  for _, v := range x {
    if v < men { // Atualiza men se encontrar um número menor
      men = v
    }
  }

  fmt.Println("Menor número: ", men) // Exibe o menor número
}

