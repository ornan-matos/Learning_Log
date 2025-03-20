package main

import (
	"fmt"
	"math/rand"
)

func main(){

  for {
    r := rand.Intn(10)

    if r % 3 == 0{
      fmt.Println("Skip")
      continue
    } else if r % 2 == 0{
      fmt.Println("Stop")
      break
    }

    fmt.Println(r)

  }
}
