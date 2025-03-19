package main

import (
	"fmt"
	"strconv"
)

func loop() string{

  i := 0
  for i = 1;i < 100; i++{
    if i % 3 == 0 && i % 5 == 0{
      fmt.Println("FizzBuzz")
    } else if i % 3 == 0{
      fmt.Println("Fizz")
    } else if i % 5 == 0{
      fmt.Println("Buzz")
    } else {
      fmt.Println(i)
    }
  }
    return strconv.Itoa(i)
}

func main(){

  result := loop()
  
  fmt.Println(result)
}
