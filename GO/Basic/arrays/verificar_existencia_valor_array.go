package main

import "fmt"

func main()  {
  num := [5]int{1, 3, 5, 7, 9}
  var x int 
  encontrado := false
  
  fmt.Println("Insira um número inteiro para verificar:")
  fmt.Scanf("%d", &x)


  for _, value := range num{
    
    if value == x {
      encontrado = true
      break
    }

  }
  fmt.Println(encontrado)
}
