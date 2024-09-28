package main

import "fmt"

/*
O programa realiza a conversão de pés para metros. O usuário insere uma quantidade em pés, e o programa calcula e exibe o equivalente em metros usando a constante de conversão apropriada.
*/

func main() {

  // Constante que define quantos metros correspondem a um pé
  const metrosConv = 0.3048

  var inputPes float64 // Variável para armazenar a entrada do usuário em pés

  // Solicita ao usuário que insira a quantidade de pés
  fmt.Println("Digite a quantidade de pes: ")

  // Lê a entrada do usuário e a armazena na variável inputPes
  fmt.Scanf("%f", &inputPes)
  
  // Converte a quantidade de pés para metros
  metros := inputPes * metrosConv

  // Exibe o resultado da conversão, formatado para duas casas decimais
  fmt.Printf("Valor convertido é: %.2fm\n", metros)

}
