/*
Este programa em Go realiza a busca de um número inteiro fornecido 
pelo usuário em um array predefinido de números inteiros.
*/

package main

import "fmt"

func main() {
  // Inicializa o array 'num' com 5 valores inteiros
  num := [5]int{1, 3, 5, 7, 9}
  
  // Declara uma variável para armazenar o número a ser pesquisado
  var x int 
  
  // Variável para armazenar o resultado da busca, inicializada como false
  encontrado := false
  
  // Solicita ao usuário que insira um número inteiro
  fmt.Println("Insira um número inteiro para verificar:")
  
  // Lê o número inteiro inserido pelo usuário
  fmt.Scanf("%d", &x)

  // Percorre cada valor do array 'num'
  for _, value := range num {
    
    // Verifica se o valor atual é igual ao número inserido pelo usuário
    if value == x {
      // Se encontrado, define 'encontrado' como true e interrompe o loop
      encontrado = true
      break
    }
  }
  
  // Exibe o resultado da busca
  fmt.Println(encontrado)
}