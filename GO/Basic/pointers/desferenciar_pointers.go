package main

import "fmt"



func main(){

  a, b := 5, 10

  fmt.Println(a , b)

  fmt.Println("-----------")

  swap(&a,&b)

  fmt.Println(a , b)

  fmt.Println("-----------")

  fmt.Println(a == 10, b == 5)
}

func swap(a *int, b *int){

  *a = 10
  *b = 5
  
}
