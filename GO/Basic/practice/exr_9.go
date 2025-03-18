package main

import (
	"fmt"
	"time"
)

func main(){

  switch dayUser := time.Sunday;{
    
  case dayUser == time.Sunday || dayUser == time.Saturday:
    fmt.Println("Nascido no fim de semana")

  default:
    fmt.Println("Nascido em outro dia")

  }

}
