package main

import "fmt"
 
/*

Programa para coletar e exibir três nomes fornecidos pelo usuário. O código solicita que o usuário insira três nomes, um de cada vez, e armazena esses nomes em um slice de strings. Em seguida, o programa imprime todos os nomes inseridos na mesma linha.

*/

func main() {  // Corrigido de 'mian' para 'main'
  nomes := make([]string, 3)  // Cria um slice de strings com capacidade para 3 elementos
  
  for i := 0; i < 3; i++ {
    // Solicita ao usuário para inserir um nome com base no índice 'i'
    fmt.Printf("Insira o %dº nome: ", i+1)
    fmt.Scanf("%s", &nomes[i])  // Lê uma string do usuário e armazena no slice 'nomes'
  }
  
  fmt.Println("Nomes inseridos: ")
  // Imprime cada nome armazenado no slice
  for _, nome := range nomes {
    fmt.Printf("%s ", nome)
  }
  fmt.Println()  // Adiciona uma nova linha após a impressão dos nomes
}
