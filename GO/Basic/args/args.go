/*
Este programa em Go lê três argumentos passados na linha de comando e verifica se o número de argumentos fornecidos é exatamente 3.

1. O programa extrai e imprime os argumentos fornecidos.
2. Chama a função `verifArgs` para validar o número de argumentos.
3. A função `verifArgs` verifica se o número de argumentos é correto e imprime mensagens apropriadas.

Observações:
- O programa encerra a execução com um código de status 0 se o número correto de argumentos for fornecido.
- Se o número de argumentos for incorreto, o programa imprime uma mensagem de erro e encerra com um código de status 1.
*/

package main

import (
	"fmt"
	"os"
)

func main() {
	// Extrai os argumentos da linha de comando
	unidadeFinal := os.Args[len(os.Args)-1]
	unidadeInicio := os.Args[1]
	unidadeMeio := os.Args[2]

	// Imprime os argumentos recebidos
	fmt.Println("Primeiro Argumento:", unidadeInicio, "Segundo Argumento:", unidadeMeio, "Terceiro Argumento:", unidadeFinal)

	// Verifica se os argumentos fornecidos estão corretos
	verifArgs()
	// Encerra o programa com status 0
	os.Exit(0)
}

func verifArgs() {
	// Verifica o número de argumentos fornecidos
	for {
		if len(os.Args) == 4 {
			// Mensagem de sucesso se o número de argumentos for 3 (incluindo o nome do programa)
			fmt.Println("Obrigado, por inserir os argumentos corretos!")
			os.Exit(0)
		} else if len(os.Args) < 2 {
			// Mensagem de erro se houver menos de 2 argumentos (excluindo o nome do programa)
			fmt.Println("Desculpe as informações de argumento estão incorretas.\n" +
				"Tente novamente, usando:\n" +
				"comando + <valor metrico> + <identificação da medida>")
			os.Exit(1)
		} else {
			// Mensagem de erro para qualquer outro número de argumentos
			fmt.Println("Erro! insira apenas um argumento.\n" +
				"Tente novamente, usando:\n" +
				"comando + <valor metrico> + <identificação da medida>")
			os.Exit(1)
		}
	}
}
