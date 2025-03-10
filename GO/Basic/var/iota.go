package main

import "fmt"

func main(){

  const(
    Domingo = iota
    Segunda 
    Terça
    Quarta
    Quinta
    Sexta
    _
    Sabado 
  )

  fmt.Println(Quinta)
  fmt.Println(Sexta)
}
