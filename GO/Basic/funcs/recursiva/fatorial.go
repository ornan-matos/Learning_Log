
/* Este programa calcula o fatorial de um número inteiro usando uma função recursiva. A recursão ocorre quando uma função chama a si mesma para resolver subproblemas menores. Aqui, a função 'add' retorna o fatorial do número passado como argumento.
*/
package main

import "fmt"

func main() {

    // Calcula e imprime o fatorial de 6.
    fmt.Println(add(6)) // Saída: 720 (6 * 5 * 4 * 3 * 2 * 1)

    // Calcula e imprime o fatorial de 0.
    // Por definição, o fatorial de 0 é 1.
    fmt.Println(add(0)) // Saída: 1
}

// A função 'add' calcula o fatorial de 'x' recursivamente.
func add(x int) int {

    // Caso base: se 'x' for 0, retorna 1.
    // Este é o ponto onde a recursão para.
    if x == 0 {
        return 1
    }

    // Chamada recursiva: multiplica 'x' pelo resultado do fatorial de (x - 1).
    return x * add(x - 1)
}

