package main

import (
	"fmt"
	"time"
)

func main(){
  var cont int
  fmt.Printf("Cont     : %#v \n", cont)

  var discont float64
  fmt.Printf("Discont  : %#v \n", discont)

  var debug bool
  fmt.Printf("Debug    : %#v \n", debug)

  var mensage string
  fmt.Printf("Message  : %#v \n", mensage)

  var emails []string
  fmt.Printf("Emails   : %#v \n", emails)

  var startTime time.Time
  fmt.Printf("Start    : %#v \n", startTime)
}
