package main

import"fmt"

/*
O programa permite ao usuário substituir um nome de fruta em um array pré-definido. O programa solicita que o usuário insira o índice de um elemento do array e o nome de uma nova fruta. Em seguida, ele substitui a fruta original pelo novo nome no índice indicado e exibe o array atualizado.
*/

func main(){
  
  // Declara um array de strings com 3 frutas
  fruit := [3]string{"pera ", "uva ", "pinha "}
  
  // Declara uma variável inteira para armazenar o índice escolhido pelo usuário
  var x int
  
  // Exibe os nomes das frutas originais
  fmt.Println("Nomes originais: ", fruit)
 
  // Solicita que o usuário insira um índice para escolher qual fruta será alterada
  fmt.Println("\nInsira o número do índice (0 a 2):")
  fmt.Scanf("%d", &x)
  
  // Solicita que o usuário insira o nome de uma nova fruta
  fmt.Println("\nInsira a nova fruta:")
  fmt.Scanf("%s", &fruit[x])
  
  // Exibe o array de frutas atualizado com a alteração realizada pelo usuário
  fmt.Println("\nNomes alterados: ", fruit)
}