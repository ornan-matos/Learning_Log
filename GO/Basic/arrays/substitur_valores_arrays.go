package main

import"fmt"

func main(){
  
  fruit := [3]string{"pera ","uva ","pihna "}
  var x int
  
  fmt.Println("Nomes originais: ", fruit)
 
  fmt.Println("\nInsira o número do índice (0 a 2):")
  fmt.Scanf("%d", &x)
  
  fmt.Println("\nInsira a nova fruta:")
  fmt.Scanf("%s", &fruit[x])
  
  fmt.Println("\nNomes alterados: ", fruit)


}
