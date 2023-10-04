package main

import (
	"fmt"
	"os"
)

func main() {

	unidadeFinal := os.Args[len(os.Args)-1]
	unidadeInicio := os.Args[1]
	unidadeMeio := os.Args[2]
	arr := [2]string {unidadeInicio, unidadeFinal}
	arr2 := [3]int {1, 2, 3}
	arr3 := [3]int {1, 2, 3}
	fmt.Println("O valor de inicio é", unidadeInicio, "Valor do meio", unidadeMeio, "Valor final é", unidadeFinal," \n" +
"Valor de Arrey (string):", arr, "Valor Arrey (int):", arr2 == arr3)

	verifArgs()
	os.Exit(0)
}

func verifArgs() {

	for {
		if len(os.Args) == 4 {
			fmt.Println("Obrigado, por inseri argumentos!")
			os.Exit(0)
		} else if len(os.Args) < 2 {
			fmt.Println("Desculpe as informações de argumento estão incorretas.\n" +
				"Tente novamente.")
			os.Exit(1)
		} else {
			fmt.Println("Erro! insira três argumento.\n" +
				"Tente novamente")
			os.Exit(1)
		}
	}
}
