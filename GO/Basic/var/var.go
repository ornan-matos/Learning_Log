
package main

import "fmt"

/*
Este programa simples em Go exibe uma mensagem de boas-vindas ao usuário,
verifica e exibe a idade do usuário e mostra a versão do programa.
*/

func main() {
    // Declaração de variáveis
	var nome string = "Ornan"    // Nome do usuário
	var versao float32 = 1.2      // Versão do programa
	var idade int = 26             // Idade do usuário
	
	// Mensagem de boas-vindas
	fmt.Println("Olá", nome, "bem-vindo ao nosso terminal")
	
	// Mensagem informando que a idade está sendo verificada
	fmt.Println("Verificando a sua idade em nossa Database.")
	fmt.Println("...")
	
	// Exibe a idade do usuário
	fmt.Println("A sua idade é", idade, "anos.")
	
	// Exibe a versão do programa
	fmt.Println("Versão:", versao)
}
