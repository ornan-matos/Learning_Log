package main

import "fmt"

func main(){

  fmt.Println("Insira um número para ver tabuada de multiplicação:")
  var valor int
  fmt.Scanf("%d", &valor)

  for i := 1 ; i <= 10; i++{
    total := i * valor
    fmt.Println(i, "x", valor, "=", total)
  }

}
