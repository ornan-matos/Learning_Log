package main

import "fmt"

func add5Value(cont int){
  cont += 5
  fmt.Println("add5Value:     ", cont)
}

func add5Point(cont *int){
  *cont += 5
  fmt.Println("add5Point:     ", *cont)
}

func main(){

  var cont int

  add5Value(cont)

  fmt.Println("add5Value post:", cont)

  add5Point(&cont)

  fmt.Println("add5Point post:", cont)

}

