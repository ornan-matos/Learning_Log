
package main

import "fmt"

/*
O programa solicita ao usuário que insira três nomes e os armazena em um slice. 
Após a coleta, ele exibe os nomes inseridos.
*/

func main() {
    // Cria um slice chamado 'nome' com 3 posições para armazenar os nomes.
    nome := make([]string, 3) 
    
    // Loop para solicitar os nomes ao usuário.
    for i := 0; i < 3; i++ { 
        // Verifica qual nome está sendo solicitado.
        if i == 0 {
            fmt.Println("Insira o primeiro nome: ") // Solicita o primeiro nome
            fmt.Scanf("%s", &nome[i]) // Lê o nome e o armazena no slice
        } else if i == 1 { // Verifica se é o segundo nome
            fmt.Println("Insira o segundo nome: ") // Solicita o segundo nome
            fmt.Scanf("%s", &nome[i]) // Lê o nome e o armazena no slice
        } else if i == 2 { // Verifica se é o terceiro nome
            fmt.Println("Insira o terceiro nome: ") // Solicita o terceiro nome
            fmt.Scanf("%s", &nome[i]) // Lê o nome e o armazena no slice
        }
    }
    
    // Loop para exibir os nomes armazenados no slice.
    for x := 0; x < len(nome); x++ { 
        fmt.Printf("%s ", nome[x]) // Exibe cada nome
    }
    
    fmt.Println() // Adiciona uma nova linha após a lista de nomes
}
