package main

import (
	"fmt"
	"time"
)

func main (){

  var cont1 *int

  cont2 := new(int)

  contTemp := 5

  cont3 := &contTemp

  t := &time.Time{}

  if cont1 != nil {
    fmt.Printf("cont1: %#v\n", *cont1)
  }

  if cont2 != nil {
    fmt.Printf("cont2: %#v\n", *cont2)
  }

  if cont3 != nil {
    fmt.Printf("cont3: %#v\n", *cont3)
  }

  if t != nil {
    fmt.Printf("time: %#v\n", *t)
    fmt.Printf("time: %#v\n", t.String())
  }

}
