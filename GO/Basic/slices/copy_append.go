package main

import "fmt"

/*
O código demonstra o uso de slices em Go, incluindo a criação, cópia e concatenação de slices. Cria dois slices e copia os elementos de um para o outro. Concatena um terceiro slice ao slice copiado e imprime o resultado.
*/

func main() {
    // Cria um slice 'slice1' com elementos 1 e 2
    slice1 := []int{1, 2}
    
    // Cria um novo slice 'slice2' com tamanho 2, pronto para ser preenchido
    slice2 := make([]int, 2) 
    
    // Copia os elementos de 'slice1' para 'slice2'
    copy(slice2, slice1) 
    
    // Cria um novo slice 'slice3' com elementos 3 e 4
    slice3 := []int{3, 4}
    
    // Concatena 'slice2' com 'slice3' e atribui o resultado a 'slice4'
    slice4 := append(slice2, slice3...) // O operador '...' é utilizado para expandir 'slice3' como uma lista de argumentos
    
    // Imprime o conteúdo de 'slice4', que agora contém os elementos concatenados
    fmt.Println(slice4)
}
