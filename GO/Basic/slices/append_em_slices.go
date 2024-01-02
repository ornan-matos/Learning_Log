package main

import	"fmt"

func main()  {
  num := make([]int, 0, 3)

  for i:=0; i <= 2; i++{
    var temp int 
    fmt.Println("Insira um número:")
    fmt.Scanf("%d", &temp)
    num = append(num, temp)
  }
  fmt.Println("Os numeros inseridos no slice são:", num)
} 
