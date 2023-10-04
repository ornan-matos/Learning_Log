package main

import "fmt"

func main(){
	var nome string
	var versao float32 = 1.3
	var comando int8
	fmt.Println("Digite o seu nome:")
	fmt.Scan(&nome)
	fmt.Println("Olá,", nome)
	fmt.Println("A versão do programa é", versao)
	fmt.Println("----------------------")
	fmt.Println("Escolha uma das opções do menu.")
	fmt.Println("1 - Iniciar Aplicação")
	fmt.Println("2 - Executar Comando Especifico")
	fmt.Println("3 - Sair")
	fmt.Scan(&comando)

	switch comando{
	case 1:
		fmt.Println("Iniciando aplicação. Aguarde...")
	case 2:
		fmt.Println("Executando comando.")
	case 3:
		fmt.Println("Saindo da aplicação.")
	default:
		fmt.Println("Desculpe esse comando não é reconhecido. Tente novamente.")
	}

}