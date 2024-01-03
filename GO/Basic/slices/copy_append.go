package main

import "fmt"

func main() {
slice1 := []int{1, 2}
slice2 := make([]int, 2) //make prepara o slice2 para ser escrito
copy(slice2, slice1) //copia o conteudo do slice1 para o slice2

slice3 := []int{3, 4}
slice4 := append(slice2, slice3...) //append entre slice2 e slice3
fmt.Println(slice4)


}
