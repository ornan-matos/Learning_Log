package main

import "fmt"

func main()  {
  nome := make([]string, 3) // cria um slice com 3 posições
  
  for i:=0; i < 3; i++ { // atribui os valores
    if i == 0 {
      fmt.Println("Insira o primeiro nome: ") // solicita o nome
      fmt.Scanf("%s", &nome[i]) // atribui o nome
    } else if i == 1 { // verifica se é o segundo nome
      fmt.Println("Insira o segundo nome: ") // solicita o segundo nome
      fmt.Scanf("%s", &nome[i]) 

    } else if i == 2 {
      fmt.Println("Insira o terceiro nome: ")
      fmt.Scanf("%s", &nome[i])
    }
  }
  for x:=0; x < len(nome); x++{ //exibe os nomes
    fmt.Printf("%s ", nome[x])
  }
  fmt.Println()
}
