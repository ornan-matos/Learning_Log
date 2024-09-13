package main

import "fmt"

/*
O programa recebe três números do usuário, os armazena em um slice e, em seguida, calcula e imprime a soma desses números. O código utiliza funções básicas de entrada, saída e iteração para realizar a operação.
*/

func main() {
  // Cria um slice de inteiros com capacidade inicial de 3, mas sem valores.
  num := make([]int, 0, 3)
  
  // Variável para armazenar a soma total dos números.
  var total int

  // Laço para solicitar três números ao usuário.
  for i := 0; i <= 2; i++ {
    var temp int
    fmt.Println("Insira um número:") // Solicita a entrada do usuário.
    fmt.Scanf("%d", &temp)           // Lê o número inserido e armazena em 'temp'.
    
    // Adiciona o número inserido ao slice 'num'.
    num = append(num, temp)
  }

  // Laço para percorrer o slice e somar os números.
  for x := 0; x < len(num); x++ {
    total += num[x] // Adiciona cada número ao total.
  }

  // Imprime o resultado da soma.
  fmt.Println("A soma dos números:", total)
}

