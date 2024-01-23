package main


import "fmt"

func main(){
  const metrosConv = 0.3048
  var inputPes float64

  fmt.Println("Digite a quantidade de pes: ")
  fmt.Scanf("%f", &inputPes)
  
  metros := inputPes * metrosConv

  fmt.Printf("Valor convertido é: %.2fm\n", metros)
}
