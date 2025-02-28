package main

import (
	"fmt"
)

/* Este programa demonstra o uso de mapas (maps) em Go, que são coleções de pares chave-valor. 
O código apresenta um mapa simples para armazenar elementos químicos e um mapa aninhado para armazenar mais detalhes dos elementos.
*/

func main() {
	// Criando um mapa simples com elementos químicos
	elements := map[string]string{
		"H":  "Hydrogen",
		"He": "Helium",
		"Li": "Lithium",
	}

	// Verificando se a chave "H" existe no mapa
	if name, ok := elements["H"]; ok {
		fmt.Println("Chave existe:", name)
	} else {
		fmt.Println("Chave não existe")
	}

	// Criando um mapa aninhado para armazenar mais informações dos elementos
	tabela := map[string]map[string]string{
		"O": {
			"name":  "Oxygen",
			"state": "gas",
		},
		"F": {
			"name":  "Fluorine",
			"state": "gas",
		},
		"Ne": {
			"name":  "Neon",
			"state": "gas",
		},
	}

	// Verificando se a chave "O" existe e imprimindo suas informações
	if el, ok := tabela["O"]; ok {
		fmt.Println(el["name"], el["state"])
	} else {
		fmt.Println("Chave não existe")
	}
}

