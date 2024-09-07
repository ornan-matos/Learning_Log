package main

import "fmt"

/*
O programa cria um slice de inteiros com capacidade inicial para 3 elementos.
Em um loop, solicita ao usuário que insira três números, os quais são adicionados ao slice.
Após o loop, o programa imprime os números inseridos.
*/

func main() {

  // Cria um slice de inteiros com comprimento 0 e capacidade 3
  num := make([]int, 0, 3)

  // Loop para receber 3 números do usuário
  for i := 0; i <= 2; i++ {

    var temp int
    fmt.Println("Insira um número:")

    // Lê um número inteiro da entrada padrão e armazena em 'temp'
    fmt.Scanf("%d", &temp)

    // Adiciona o número inserido ao slice
    num = append(num, temp)
  }
  
  // Exibe os números armazenados no slice
  fmt.Println("Os números inseridos no slice são:", num)
}