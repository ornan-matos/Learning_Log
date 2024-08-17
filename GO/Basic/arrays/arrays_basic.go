// Este programa define duas funções que retornam arrays de marcas de produtos.
// A função 'marcasRefri' retorna marcas de refrigerante e a função 'marcaChocolate' 
// retorna marcas de chocolate.
// O programa principal exibe essas marcas no console.

package main

import "fmt"

func main() {
	// Obtém o array de marcas de refrigerante usando a função 'marcasRefri'
	marcas := marcasRefri()
	// Obtém o array de marcas de chocolate usando a função 'marcaChocolate'
	marcas2 := marcaChocolate()
	
	// Imprime as marcas de refrigerante
	fmt.Println("Essas são as marcas de refrigerante:", marcas)
	// Imprime as marcas de chocolate
	fmt.Println("Essas são as marcas de chocolate:", marcas2)
}

// Função que retorna um array de 4 strings com marcas de refrigerante
func marcasRefri() [4]string {
	var refri [4]string
	refri[0] = "coca-cola"
	refri[1] = "sprite"
	refri[2] = "pepsi"
	refri[3] = "fanta"
	
	return refri
}

// Função que retorna um array de 3 strings com marcas de chocolate
func marcaChocolate() [3]string {
	var choco [3]string
	choco[0] = "garoto"
	choco[1] = "lacta"
	choco[2] = "nestle"

	return choco
}



