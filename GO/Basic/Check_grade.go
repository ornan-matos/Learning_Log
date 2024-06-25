package main

import "fmt"

func main(){

  var nota int
   
  fmt.Println("Insira a nota: ")
  fmt.Scanf("%d", &nota)
  
  for nota > 100 || nota < 0{
  fmt.Println("Nota inválida!")
  fmt.Println("Insira a nota: ")
  fmt.Scanf("%d", &nota)

  }
  
  if nota >= 70 && nota <= 100{
    fmt.Println("Aprovado!")
  } else{
    fmt.Println("Reprovado!")
  }
}
