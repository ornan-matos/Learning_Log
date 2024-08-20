/*
1. Captura argumentos da linha de comando e armazena alguns deles em variáveis.
2. Cria e inicializa arrays de diferentes tipos.
3. Imprime os valores armazenados e compara dois arrays.
4. Verifica a quantidade de argumentos passados e exibe mensagens apropriadas.
*/

package main

import (
	"fmt"
	"os"
)

func main() {
	// Captura o último argumento e armazena em unidadeFinal
	unidadeFinal := os.Args[len(os.Args)-1]

	// Captura o primeiro e o segundo argumento
	unidadeInicio := os.Args[1]
	unidadeMeio := os.Args[2]

	// Cria um array de strings com dois elementos
	arr := [2]string{unidadeInicio, unidadeFinal}

	// Cria dois arrays de inteiros para comparação
	arr2 := [3]int{1, 2, 3}
	arr3 := [3]int{1, 2, 3}

	// Imprime os valores capturados e a comparação dos arrays
	fmt.Println("O valor de inicio é", unidadeInicio, "Valor do meio", unidadeMeio, "Valor final é", unidadeFinal, "\n" +
		"Valor de Arrey (string):", arr, "Valor Arrey (int):", arr2 == arr3)

	// Chama a função para verificar a quantidade de argumentos
	verifArgs()
	
	// Encerra o programa com sucesso
	os.Exit(0)
}

func verifArgs() {
	// Loop infinito para verificar o número de argumentos
	for {
		// Se o número de argumentos é 4 (incluindo o nome do programa), exibe mensagem de sucesso
		if len(os.Args) == 4 {
			fmt.Println("Obrigado, por inseri argumentos!")
			os.Exit(0)
		} else if len(os.Args) < 2 {
			// Se menos de 2 argumentos foram passados, exibe mensagem de erro
			fmt.Println("Desculpe as informações de argumento estão incorretas.\n" +
				"Tente novamente.")
			os.Exit(1)
		} else {
			// Para outros casos, exibe mensagem pedindo exatamente 3 argumentos
			fmt.Println("Erro! insira três argumento.\n" +
				"Tente novamente")
			os.Exit(1)
		}
	}
}