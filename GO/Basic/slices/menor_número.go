package main

import "fmt"

func main(){

// Encontrar menor número na lista de um slice

  x := [ ]int{
    48,96,86,68,
    57,82,63,70,
    37,34,83,27,
    19,97, 9,17,
  }

  menor := x[0]

  for _, y := range x{
    if y < menor{
      menor = y
    }
  }

  fmt.Println(menor)
}
