package main

import "fmt"

/* 
Este programa demonstra o uso de funções variádicas em Go.Funções variádicas permitem que um número variável de argumentos seja passado para o último parâmetro.
*/

func main() {
    // Chamada da função `sum` com múltiplos inteiros.
    fmt.Println(sum(10, 20, 30, 40)) // Saída: 100

    // Chamada da função `concat` com múltiplas strings.
    fmt.Println(concat("Olá", " mundo!")) // Saída: "Olá mundo!"
}

// A função `sum` aceita um número variável de inteiros (args ...int)
// e retorna a soma de todos os números fornecidos.
func sum(args ...int) int {
    total := 0 // Variável para armazenar o total

    // Itera sobre todos os números fornecidos em `args`
    for _, v := range args {
        total += v // Soma cada número ao total
    }

    return total // Retorna o total calculado
}

// A função `concat` aceita um número variável de strings (word ...string)
// e retorna uma única string concatenada.
func concat(word ...string) string {
    var phrase string // Variável para construir a frase concatenada

    // Itera sobre todas as strings fornecidas em `word`
    for _, w := range word {
        phrase += w // Adiciona cada string à frase
    }

    return phrase // Retorna a frase concatenada
}

