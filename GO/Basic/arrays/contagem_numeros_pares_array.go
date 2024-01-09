package main

import "fmt"

func main()  {

  num := [10]int{1,2,3,4,5,6,7,8,9,10}
  x := 0
  for i:=0; i < 10; i++{
    if num[i] % 2 == 0 {
      x++ 
    }
  }
  fmt.Println("Numeros pares no arrey: ", x)
}
