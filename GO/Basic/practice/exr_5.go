package main

import "fmt"

/*
Exercício slice, make, comprimento através do índice do slice 
*/

func main()  {

  x := make([]float32, 5, 10)

  for i := 0; i < len(x); i++{
  x[i] = float32(i) + 1
}

fmt.Println(x[2:4])
fmt.Println(x[:len(x)])
  
}
