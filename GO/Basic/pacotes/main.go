package main

import (
  "fmt"
  "modulo/auxiliar"
  "github.com/badoux/checkmail"
)

func main(){
  fmt.Println("Escrevendo do arquivo main")
  auxiliar.Escrever()
  auxiliar.Escrever2()

  //Verificar se o formato de email inserido é valido

  var email string

  fmt.Println("\nDigite um email valido:")
  fmt.Scanf("%s", &email)

  error :=  checkmail.ValidateFormat(email)

  if error == nil {

  fmt.Println("Ok!", error)

  } else {

  fmt.Println("Erro!", error)

  }
}

