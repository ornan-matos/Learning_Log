package main
/*
Este programa em Go realiza uma validação de um número inteiro e trata erros de maneira simples. A função validação verifica se o valor fornecido é negativo, maior que 100 ou divisível por 7, retornando um erro correspondente em cada uma dessas condições. Caso contrário, ela retorna nil. No main, o valor é validado e, caso um erro seja retornado, ele é impresso. Se não houver erro, o programa verifica se o número é par ou ímpar.
*/

import (
	"errors"
	"fmt"
)

// A função validacao recebe um valor inteiro e retorna um erro dependendo das condições especificadas.
func validacao(valor int) error{
	// Se o valor for negativo, retorna um erro.
	if valor < 0 {
		return errors.New("Erro! Número negativo.")
	} 
	// Se o valor for maior que 100, retorna um erro.
	else if valor > 100 {
		return errors.New("Erro! Maior que 100.")
	} 
	// Se o valor for divisível por 7, retorna um erro.
	else if valor % 7 == 0 {
		return errors.New("O valor é divisível por 7")
	} 
	// Caso contrário, retorna nil indicando que não há erro.
	else {
		return nil
	}
}

func main(){
	// O valor que será validado
	valor := -10

	// Chama a função validacao e verifica se ocorreu algum erro.
	if err := validacao(valor); err != nil {
		// Se houver erro, imprime a mensagem do erro.
		fmt.Println(err)
	} 
	// Se não houver erro, verifica se o número é par ou ímpar.
	else if valor % 2 == 0 {
		fmt.Println("O valor é par")
	} else {
		fmt.Println("O valor é ímpar")
	}
}

