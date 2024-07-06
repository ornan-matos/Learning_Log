// Este programa realiza uma contagem regressiva de 10 a 1.
// Ele utiliza um loop 'for' para iterar de 10 até 1 e, a cada iteração,
// diminui o valor do contador em 1 e espera por 1 segundo.
// Ao final da contagem regressiva, o programa imprime "Feliz Ano Novo!".

package main

import (
	"fmt"
	"time"
)

func main() {
	// Inicializa o contador com o valor de 10
	countdown := 10

	// Loop 'for' que executa enquanto o contador for maior que 0
	for countdown > 0 {
		// Imprime o valor atual do contador
		fmt.Println(countdown)

		// Aguarda 1 segundo antes de continuar
		time.Sleep(1 * time.Second)

		// Decrementa o valor do contador em 1
		countdown--
	}

	// Imprime a mensagem final
	fmt.Println("Feliz Ano Novo!")
}
