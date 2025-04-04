package main

import (
	"fmt"
	"unicode"
)

func passwordCheck(pw string) bool{
  pwR := []rune(pw)

  if len(pwR) < 8 {
    return false
  }

  hasUpper := false
  hasLower := false
  hasNumber := false
  hasSymbol := false

  for _, v := range pwR{
    if unicode.IsUpper(v){
      hasUpper = true
    }

    if unicode.IsLower(v){
      hasLower = true
    }

    if unicode.IsNumber(v){
      hasNumber = true
    }

    if unicode.IsPunct(v) || unicode.IsSymbol(v){
      hasSymbol = true
    }
  }

  return hasUpper && hasLower && hasNumber && hasSymbol

}

func main(){

  if passwordCheck("This!I5A"){
    fmt.Println("Boa senha!")
  } else {
    fmt.Println("Senha ruim!")
  }

  fmt.Println("---------------")

  if passwordCheck("12345678"){
    fmt.Println("Boa senha!")
  } else {
    fmt.Println("Senha ruim!")
  }
}
