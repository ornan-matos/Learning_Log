package main

import "fmt"

func main() {

	nome := "Ornan Matos"
	programa := "SkyDrive"
	var versao float32 = 1.2
	idade := 26

	fmt.Println("Olá", nome, "sua idade é", idade, "seja bem-vindo ao ", programa)
	fmt.Println("A versão do programa:", versao)
	fmt.Println("-------------------------------")
	fmt.Println("Escolha uma das opções")
	
	fmt.Println("3 - Iniciar Monitoramento")
	fmt.Println("2 - Exibir logs")
	fmt.Println("0 - Sair do Programa")

	var comando int

	fmt.Scanf("%d", &comando)
	fmt.Println(comando, "- foi a opção escolhida.")

}