package main

import "fmt"

func mian()  {
  nome := []string{}
  
  for i:=0; i < 3; i++{
    if i == 0 {
      fmt.Println("Insira o primeiro nome: ")
      fmt.Scanf("s%", &nome)
    } else if i == 1 {
      fmt.Println("Insira o segundo nome: ")
    } else if i == 2 {
      fmt.Println("Insira o terceiro nome: ")
    }
  }
  for x:=0; x < len(nome); x++{
    fmt.Printf("%s", nome[x])
  }
  fmt.Println()
}
