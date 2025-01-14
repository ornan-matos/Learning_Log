package main

import "fmt"

/* Este programa demonstra como usar funções variádicas para encontrar o maior número em uma lista de inteiros.
*/

func main() {
    // Chamada da função `max` com múltiplos inteiros.
    fmt.Println(max(2, 5, 3, 10, 20, 1, 9)) // Saída: 20
}

// A função `max` aceita um número variável de inteiros (num ...int)
// e retorna o maior número entre os fornecidos.
func max(num ...int) int {
    // Inicializamos a variável `maior` com o primeiro número da lista.
    maior := num[0]

    // Iteramos sobre todos os números fornecidos em `num`.
    for _, v := range num {
        // Se o número atual (v) for maior que `maior`, atualizamos `maior`.
        if v > maior {
            maior = v
        }
    }

    // Retornamos o maior número encontrado.
    return maior
}

