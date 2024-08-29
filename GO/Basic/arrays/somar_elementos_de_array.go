package main

import "fmt"

/*
O programa demonstra operações básicas com arrays e loops. Inicialmente, um array de inteiros é declarado e alguns valores são atribuídos a ele. Em seguida, são realizados cálculos simples, como a soma de elementos específicos do array e a soma de todos os elementos usando um loop for.
*/

func main()  {
  
  // Declaração de um array de inteiros com 10 posições e inicialização dos primeiros 5 elementos.
  x := [10]int{1,2,3,4,5}
  
  // Declaração de uma variável inteira y para armazenar a soma dos elementos do array.
  var y int 
  
  // Impressão dos primeiros 5 elementos do array x.
  fmt.Println(x[0:5])
  
  // Impressão da soma dos primeiros 5 elementos do array x.
  fmt.Println(x[0] + x[1] + x[2] + x[3] + x[4])
  
  // Loop para somar todos os elementos do array x e armazenar o resultado em y.
  for i := 0; i < len(x); i++ {
    y += x[i] 
  }
  
  // Impressão do valor total de y, que é a soma de todos os elementos do array x.
  fmt.Println(y)
}
