package main

/* 
Programa que calcula a soma das taxas de vendas para três itens diferentes.
O programa calcula a taxa de vendas com base no preço do item e na taxa de imposto e exibe o total de imposto a ser pago.
*/

import (
	"fmt"
)

// Função que calcula o imposto sobre um item com base no seu custo e taxa de imposto.
// Recebe dois parâmetros: o custo do item e a taxa de imposto.
// Retorna o valor do imposto para o item.
func calc(cost float32, tax float32) float32 {
	// Calcula a taxa de imposto multiplicando o custo pelo valor da taxa (dividido por 100)
	total := ((cost * tax) / 100)

	// Retorna o valor calculado do imposto
	return total
}

func main() {
	// Define os preços dos itens: bolo, leite e manteiga
	var Cake, Milk, Butter float32 = 0.99, 2.75, 0.87 

	// Calcula o imposto de cada item utilizando a função calc e soma os resultados
	var totalTax float32 = calc(Cake, 7.5) + calc(Milk, 1.5) + calc(Butter, 2.0)
	
	// Exibe o valor total de imposto calculado
	fmt.Println("Taxa total de vendas: ", totalTax)
}

