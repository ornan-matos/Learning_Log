package main

import "fmt"

func main()  {
  
  x:= [10]int{1,2,3,4,5}
  var y int 
  fmt.Println(x[0:5])
  fmt.Println(x[0] + x[1] + x[2] + x[3] + x[4])
  
  for i:=0; i < len(x); i++{
    y += x[i] 
  }
  fmt.Println(y)
}
