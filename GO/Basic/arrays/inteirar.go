package main

import "fmt"

/*
Inteira valores em todas a posições de um array e calcular média desse valores no final
*/

func main(){

  var arr [5]int

  for i := 0; i < len(arr); i++{
    arr[i] = 1 + i
    fmt.Println(arr[i])
  }

  var total float32

  for _, x := range arr{

    total += float32(x)

  }

  fmt.Println("Total =", total / float32(len(arr)))
}
