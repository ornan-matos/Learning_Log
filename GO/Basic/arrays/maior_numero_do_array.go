package main

import "fmt"

func main() {
  num := [4]int{3,7,23,5}
  max := num[0] 
  
  for _,value := range num{
    if max < value {
      max = value
    }
  }
  fmt.Println(max)
       
}
  

