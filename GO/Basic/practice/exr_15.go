
package main

import "fmt"

/* 
O código demonstra duas formas de percorrer uma string em Go. A primeira forma trata a string como uma sequência de bytes, enquanto a segunda converte cada byte em um caractere (string) antes de imprimi-lo.
*/

func main() {

	// A variável userName contém uma string com caracteres especiais
	userName := "Sir_King_Über"

	// Primeira forma de percorrer a string: acessando os bytes diretamente
	// Cada caractere da string é tratado como um byte
	for i := 0; i < len(userName); i++ {
		// Imprime o valor do byte, que é o código ASCII de cada caractere
		// Pode resultar em uma impressão errada para caracteres especiais (ex: "Ü")
		fmt.Print(userName[i], " ")
	}
	fmt.Println("") // Para pular uma linha entre as duas impressões

	// Segunda forma de percorrer a string: convertendo o byte para string
	// Aqui, cada caractere é impresso corretamente, incluindo caracteres especiais
	for i := 0; i < len(userName); i++ {
		// Convertendo o byte para string antes de imprimir, garantindo a exibição correta
		fmt.Print(string(userName[i]), " ")
	}
}

