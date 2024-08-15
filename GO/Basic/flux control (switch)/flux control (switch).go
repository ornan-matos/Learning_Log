/*
Programa de Menu Simples

Este programa solicita ao usuário seu nome e exibe uma mensagem de boas-vindas junto com a versão do programa. 
Depois, apresenta um menu com três opções para o usuário escolher:
1. Iniciar Aplicação
2. Executar Comando Específico
3. Sair

O programa executa a ação correspondente à opção escolhida e, se uma opção inválida for fornecida, informa o usuário sobre o erro.
*/

package main

import "fmt"

func main(){
	// Declara uma variável para armazenar o nome do usuário.
	var nome string
	
	// Declara e inicializa a variável para a versão do programa.
	var versao float32 = 1.3
	
	// Declara uma variável para armazenar o comando do menu.
	var comando int8
	
	// Solicita ao usuário que digite seu nome e lê o input.
	fmt.Println("Digite o seu nome:")
	fmt.Scan(&nome)
	
	// Exibe uma mensagem de boas-vindas ao usuário.
	fmt.Println("Olá,", nome)
	
	// Exibe a versão atual do programa.
	fmt.Println("A versão do programa é", versao)
	
	// Exibe uma linha separadora para melhor visualização.
	fmt.Println("----------------------")
	
	// Exibe as opções do menu para o usuário.
	fmt.Println("Escolha uma das opções do menu.")
	fmt.Println("1 - Iniciar Aplicação")
	fmt.Println("2 - Executar Comando Especifico")
	fmt.Println("3 - Sair")
	
	// Lê o comando escolhido pelo usuário.
	fmt.Scan(&comando)

	// Executa a ação correspondente ao comando escolhido pelo usuário.
	switch comando{
	case 1:
		// Caso 1: Inicia a aplicação e exibe uma mensagem de aguarde.
		fmt.Println("Iniciando aplicação. Aguarde...")
	case 2:
		// Caso 2: Executa um comando específico e exibe uma mensagem.
		fmt.Println("Executando comando.")
	case 3:
		// Caso 3: Encerra a aplicação e exibe uma mensagem de saída.
		fmt.Println("Saindo da aplicação.")
	default:
		// Caso padrão: Exibe uma mensagem de erro para comandos não reconhecidos.
		fmt.Println("Desculpe esse comando não é reconhecido. Tente novamente.")
	}
}
