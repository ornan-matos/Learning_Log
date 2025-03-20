package main

import "fmt"

/*
Algoritmo de ordenação "Bubble Sort" em Golang.
O código utiliza o método de ordenação por troca de elementos adjacentes.
Em cada iteração, ele compara pares de elementos consecutivos e os troca se estiverem fora de ordem.
O processo é repetido até que a lista esteja completamente ordenada.
*/

func main() {
  // Inicializa a lista de números inteiros desordenados
  lista := []int{5, 8, 2, 4, 0, 1, 3, 7, 9, 6}
  
  // Exibe a lista antes da ordenação
  fmt.Println("Antes:", lista)

  // Laço de repetição para realizar a ordenação
  // O laço continuará enquanto houver troca de elementos, indicado pela variável 'ativar'
  for ativar := true; ativar; {

    // Inicializa 'ativar' como false, assumindo que a lista já está ordenada
    ativar = false

    // Laço que percorre a lista comparando elementos adjacentes
    for i := 1; i < len(lista); i++ {

      // Se o elemento anterior for maior que o próximo, troca de lugar
      if lista[i-1] > lista[i] {

        // Realiza a troca de posições entre os elementos
        lista[i], lista[i-1] = lista[i-1], lista[i]

        // Se ocorrer uma troca, define 'ativar' como true para continuar a ordenação
        ativar = true
      }
    }
  }

  // Exibe a lista após a ordenação
  fmt.Println("Apos:", lista)
}

