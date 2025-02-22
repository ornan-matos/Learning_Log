package main

import (
  "fmt"
  "math"
)


func main(){



  for i := 0; i <= 100; i++{

  primo := true

    if i < 2 {
      primo = false
    }

    for x := 2; x <= int(math.Sqrt(float64(i))); x++{

      if i % x == 0{
        primo = false // Se for divisível
        break
      }
    }

    if primo {
      fmt.Println(i, "É primo!")
    } else {
      fmt.Println(i, "Não é primo")
    }
  }
}
