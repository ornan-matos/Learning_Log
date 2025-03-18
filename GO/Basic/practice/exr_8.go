
package main

import (
	"fmt"
	"time"
)

/* 
Este programa determina o dia da semana em que o usuário nasceu,e imprime uma mensagem indicando se nasceu em um dia útil ou no fim de semana.
Depois, imprime uma característica associada ao dia da semana de nascimento,com uma verificação de erro no caso de um dia inválido.
*/

func main() {

	// A variável 'dayUser' armazena o dia da semana em que o usuário nasceu.
	dayUser := time.Saturday

	// Primeiro 'switch': Verifica se o dia é útil ou fim de semana.
	switch dayUser {

	case time.Monday, time.Tuesday, time.Wednesday, time.Thursday, time.Friday:
		// Caso seja um dia útil, imprime a mensagem abaixo.
		fmt.Println("Nasceu em um dia útil")
	case time.Saturday, time.Sunday:
		// Caso seja fim de semana, imprime a mensagem abaixo.
		fmt.Println("Nasceu no fim de semana")
	}

	// Segundo 'switch': Imprime uma característica associada ao dia da semana de nascimento.
	switch dayUser {

	case time.Monday:
		// Característica para quem nasceu na segunda-feira.
		fmt.Println("A criança de segunda-feira é de rosto bonito")
	case time.Tuesday:
		// Característica para quem nasceu na terça-feira.
		fmt.Println("A criança de terça-feira é cheia de graça")
	case time.Wednesday:
		// Característica para quem nasceu na quarta-feira.
		fmt.Println("A criança de quarta-feira é cheia de tristeza")
	case time.Thursday:
		// Característica para quem nasceu na quinta-feira.
		fmt.Println("A criança de quinta-feira tem muito a percorrer")
	case time.Friday:
		// Característica para quem nasceu na sexta-feira.
		fmt.Println("A criança de sexta-feira é amorosa e generosa")
	case time.Saturday:
		// Característica para quem nasceu no sábado.
		fmt.Println("A criança de sábado trabalha duro para viver")
	case time.Sunday:
		// Característica para quem nasceu no domingo.
		fmt.Println("A criança de domingo é linda e alegre")

	default:
		// Caso o valor de 'dayUser' não corresponda a nenhum dia válido, entra no 'default'.
		// Isso é útil para capturar qualquer erro de entrada, como um valor inválido.
		fmt.Println("Erro, dia de nascimento inválido")
	}
}

