package main

import (
	"fmt"
	"os"
)

func main() {

	unidadeFinal := os.Args[len(os.Args)-1]
	unidadeInicio := os.Args[1]
	unidadeMeio := os.Args[2]
	fmt.Println("Primeiro Argumento:", unidadeInicio, "Segundo Argumento:", unidadeMeio, "Terceiro Argumento:", unidadeFinal)

	verifArgs()
	os.Exit(0)
}

func verifArgs() {

	for {
		if len(os.Args) == 4 {
			fmt.Println("Obrigado, por inserir os argumentos corretos!")
			os.Exit(0)
		} else if len(os.Args) < 2 {
			fmt.Println("Desculpe as informações de argumento estão incorretas.\n" +
				"Tente novamente, usando:\n" +
				"comando + <valor metrico> + <identificação da medida>")
			os.Exit(1)
		} else {
			fmt.Println("Erro! insira apenas um argumento.\n" +
				"Tente novamente, usando:\n" +
				"comando + <valor metrico> + <identificação da medida>")
			os.Exit(1)
		}
	}
}