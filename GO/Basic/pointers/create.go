package main

import (
	"fmt"
	"time"
)

func main(){
  var cont1 *int

  cont2 := new(int)

  contTemp := 5

  cont3 := &contTemp

  t := &time.Time{}

  fmt.Printf("cont1: %#v\n", cont1)
  fmt.Printf("cont2: %#v\n", cont2)
  fmt.Printf("cont3: %#v\n", cont3)
  fmt.Printf("time : %#v\n", t)


  cont := &[]int{5}[0]

  fmt.Printf("Endereço: %p\n", cont)
  fmt.Printf("Valor: %d\n", *cont)
  fmt.Printf("Forma alternativa: %#v\n", cont)
}
