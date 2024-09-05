package main

import "fmt"

/*

Este programa exibe uma mensagem de boas-vindas ao usuário, mostra a versão do programa e apresenta um menu com opções. O usuário deve inserir um número para selecionar uma opção. O código captura a entrada do usuário e exibe a opção escolhida.

*/

func main() {
	// Definição das variáveis do programa
	nome := "Ornan Matos"          // Nome do usuário
	programa := "SkyDrive"         // Nome do programa
	var versao float32 = 1.2       // Versão atual do programa
	idade := 26                   // Idade do usuário

	// Impressão de uma mensagem de boas-vindas com as informações do usuário e do programa
	fmt.Println("Olá", nome, "sua idade é", idade, "seja bem-vindo ao", programa)
	fmt.Println("A versão do programa:", versao)
	fmt.Println("-------------------------------")
	fmt.Println("Escolha uma das opções")

	// Impressão das opções disponíveis para o usuário
	fmt.Println("3 - Iniciar Monitoramento")
	fmt.Println("2 - Exibir logs")
	fmt.Println("0 - Sair do Programa")

	// Variável para armazenar a opção escolhida pelo usuário
	var comando int

	// Captura a entrada do usuário e armazena na variável 'comando'
	fmt.Scanf("%d", &comando)
	
	// Impressão da opção escolhida pelo usuário
	fmt.Println(comando, "- foi a opção escolhida.")
}