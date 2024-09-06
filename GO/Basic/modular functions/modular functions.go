package main

import (
	"fmt"
	"os"
)


/*
Este programa é um exemplo simples de uma aplicação de console em Go que apresenta um menu de opções ao usuário. 
O programa permite ao usuário iniciar a aplicação, executar um comando específico, visualizar informações do programa 
ou sair da aplicação. Dependendo da escolha do usuário, a aplicação exibe uma mensagem correspondente ou encerra o programa.
*/


func main() {
	// Exibe uma apresentação inicial solicitando o nome do usuário
	presentation()
	
	// Exibe o menu de opções para o usuário
	menu()
	
	// Obtém a escolha do usuário
	var comando int8 = entradaDeComando()

	// Executa a ação correspondente à escolha do usuário
	switch comando {
	case 1:
		fmt.Println("Iniciando aplicação. Aguarde...")
	case 2:
		fmt.Println("Executando comando.")
	case 3:
		fmt.Println("O programa está na versão 1.1")
		fmt.Println("O desenvolvedor responsável pela aplicação é Ornan Matos")
		fmt.Println("Obrigado por executar!")
	case 4:
		fmt.Println("Saindo da aplicação.")
		os.Exit(0) // Encerra o programa com status 0 (sucesso)
	default:
		fmt.Println("Desculpe, esse comando não é reconhecido. Tente novamente.")
		os.Exit(-1) // Encerra o programa com status -1 (erro)
	}
}

// Função para exibir uma apresentação inicial e solicitar o nome do usuário
func presentation() {
	var nome string
	fmt.Println("Digite o seu nome para iniciarmos.")
	fmt.Scan(&nome) // Lê o nome do usuário a partir da entrada padrão
	fmt.Println("Olá,", nome, "bem-vindo à Modularização de Funções.")
}

// Função para exibir o menu de opções
func menu() {
	fmt.Println("Escolha uma das opções do menu.")
	fmt.Println("1 - Iniciar Aplicação")
	fmt.Println("2 - Executar Comando Específico")
	fmt.Println("3 - Informações do Programa")
	fmt.Println("4 - Sair")
}

// Função para ler a escolha do usuário e retornar o comando escolhido
func entradaDeComando() int8 {
	var comandoLido int8
	fmt.Scan(&comandoLido) // Lê a escolha do usuário a partir da entrada padrão
	fmt.Println("A opção escolhida foi", comandoLido)
	return comandoLido
}