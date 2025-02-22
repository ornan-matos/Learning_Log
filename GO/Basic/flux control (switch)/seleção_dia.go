package main

import "fmt"

func main(){

  fmt.Println("Opções:\n1. Domingo\n2. Segunda\n3. Terça\n4. Quarta\n5. Quinta\n6. Sexta\n7. Sábado");

  var op string

  fmt.Scanf("%s", &op)

  switch op{
  
  case "1":
    fmt.Println("Alternativa escolhida, %s Domingo ", op)
 
  case "2":
    fmt.Println("Alternativa escolhida, %s Segunda ", op)
 
  case "3":
    fmt.Println("Alternativa escolhida, %s Terça ", op)

 
  case "4":
    fmt.Println("Alternativa escolhida, %s Quarta ", op)

 
  case "5":
    fmt.Println("Alternativa escolhida, %s Quinta ", op)

 
  case "6":
    fmt.Println("Alternativa escolhida, %s Sexta ", op)

 
  case "7":
    fmt.Println("Alternativa escolhida, %s Sábado ", op)

  default:
    
    fmt.Println("Alternativa Incorreta!")

  }
}
