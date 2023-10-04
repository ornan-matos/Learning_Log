package main
import (
	"fmt"
	"os"
	"net/http"
)

func main() {
	boasVindas()
	menu()
}

func boasVindas() {
	var versao float32 = 1.0
	fmt.Println("Monitor Web HTTP", versao)
	fmt.Println(" ")
	fmt.Println("Vamos começar...\n" +
" ")
}

func coletarInfo() string {
	var primeiroNome, segundoNome  string
	fmt.Println("Por favor, informe o seu primeiro nome:")
	fmt.Scan(&primeiroNome)
	fmt.Println("Agora informe o segundo nome: ")
	fmt.Scan(&segundoNome)
	return primeiroNome
}

func menu() int8 {
	var comandoMenu int8
	
	fmt.Print(" \n" +
"Olá ", coletarInfo(), ", bem-vindo!\n" +
"----------------------\n" +
"Menu Principal - Escolha uma das alternativas\n" +
"----------------------\n")
	fmt.Println("1 - Iniciar o monitoramento HTTP")
	fmt.Println("2 - Registrar Logs")
	fmt.Println("3 - Sair")
	fmt.Scan(&comandoMenu)
	

	switch comandoMenu {
	case 1:
		monitoramentoHttp()
	
	case 2:
		fmt.Println("Analisando logs...")

	case 3:
		fmt.Print("Fechando...")
		os.Exit(0)

	default:
		fmt.Println("O comando não foi reconhecido.")
		os.Exit(1)
	} 
	return comandoMenu
}

func monitoramentoHttp()  {
	var site string
	fmt.Println("Iniciando Monitoramento HTTP.\n" +
"Insira o endereço do site:")
	fmt.Scan(&site)
	resp, _ := http.Get(site)

	if resp.StatusCode == 200 {
		fmt.Println("O site", site, "esta operacional!")
	} else {
		fmt.Println("O site fora do ar.\n"+
		"Status Code:", resp.StatusCode)
		os.Exit(0)
	}
}
