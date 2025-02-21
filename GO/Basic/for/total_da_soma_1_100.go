package main

import "fmt"

func main(){

total := 0

  for i := 1; i <= 100; i++{
    total += i
    fmt.Println(total)
  }

  fmt.Println("A soma total dos número de 1 a 100 é:", total)
}
