package main

import (
	"fmt"
)

// Este programa verifica se um carro foi multado em uma rodovia.
// O usuário insere a velocidade do carro e o programa compara
// essa velocidade com o limite permitido. Se a velocidade 
// exceder o limite, o programa indica que o carro foi multado.

func main() {
	// Definimos o limite de velocidade da rodovia
	const limiteVelocidade = 80

	// Solicitamos ao usuário que insira a velocidade do carro
	fmt.Print("Digite a velocidade do carro (em km/h): ")
	var velocidadeCarro int
	fmt.Scan(&velocidadeCarro)

	// Verificamos se a velocidade do carro excede o limite permitido
	if velocidadeCarro > limiteVelocidade {
		// Se a velocidade exceder o limite, indicamos que o carro foi multado
		fmt.Println("O carro foi multado por excesso de velocidade.")
	} else {
		// Se a velocidade estiver dentro do limite, indicamos que o carro não foi multado
		fmt.Println("O carro não foi multado.")
	}
}
