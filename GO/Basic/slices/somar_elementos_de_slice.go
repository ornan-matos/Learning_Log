package main

import "fmt"

func main()  {
  num := make([]int, 0, 3)
  var total int
  for i:=0; i <=2; i++{
    var temp int
    fmt.Println("Insira um número:")
    fmt.Scanf("%d", &temp)
    num = append(num, temp)
  }
  for x:=0; x < len(num); x++{
    total += num[x]
  }
  fmt.Println("A soma dos números:", total)
}
