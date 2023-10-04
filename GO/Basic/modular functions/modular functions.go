package main
import "fmt"
import "os"

func main() {

	presentation()
	menu()
		
	var comando int8 = entradaDeComando()

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
		os.Exit(0)
	default:
		fmt.Println("Desculpe esse comando não é reconhecido. Tente novamente.")
		os.Exit(-1)
	}

}

func presentation() {

	var nome string
	fmt.Println("Digite o seu nome para iniciarmos.")
	fmt.Scan(&nome)
	fmt.Println("Olá,", nome, "bem-vindo Modularização de Funções.")

}

func menu() {
	fmt.Println("Escolha uma das opções do menu.")
	fmt.Println("1 - Iniciar Aplicação")
	fmt.Println("2 - Executar Comando Especifico")
	fmt.Println("3 - Informações do Programa")
	fmt.Println("4 - Sair")

}

func entradaDeComando() int8 {
	var comandoLido int8
	fmt.Scan(&comandoLido)
	fmt.Println("O opção escolhida foi", comandoLido)
	return comandoLido

}