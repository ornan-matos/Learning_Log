/* Programa em Go que gera e exibe uma sequência aleatória de asteriscos (*).

1. Inicializa o gerador de números aleatórios com um seed baseado no tempo atual.
2. Gera um número aleatório entre 1 e 5.
3. Cria uma string contendo esse número de asteriscos (*).
4. Exibe a string gerada no console.
*/ 

package main

import (
  "fmt"
  "math/rand"
  "strings"
  "time"
)

func main() {
  // Inicializa o gerador de números aleatórios com a semente baseada no tempo atual
  rand.Seed(time.Now().UnixNano())

  // Gera um número aleatório entre 1 e 5
  r := rand.Intn(5) + 1

  // Cria uma string contendo 'r' asteriscos
  starts := strings.Repeat("*", r)

  // Exibe a string gerada no console
  fmt.Println(starts)
}

