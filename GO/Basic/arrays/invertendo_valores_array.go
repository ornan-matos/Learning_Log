package main

import "fmt"

func main()  {
  
  name := [4]string{"bra", "usa", "can", "chi"}
  fmt.Println(name)
  
  for i:=len(name) -1; i >=0; i--{
    fmt.Printf("%s ", name[i])
  }
  fmt.Println()
}
