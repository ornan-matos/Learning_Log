/*
Programa para avaliação de notas escolares.

Este programa solicita ao usuário que insira uma nota. O valor inserido é validado para garantir que esteja entre 0 e 100. Se a nota estiver fora desse intervalo, o usuário é solicitado a inserir uma nova nota. Após a entrada válida, o programa determina se o aluno foi aprovado (nota >= 70) ou reprovado (nota < 70) e exibe o resultado.

*/

package main

import "fmt"

func main() {
    // Declara a variável para armazenar a nota
    var nota int

    // Solicita ao usuário que insira uma nota
    fmt.Println("Insira a nota: ")
    fmt.Scanf("%d", &nota)
  
    // Verifica se a nota está fora do intervalo permitido (0 a 100)
    for nota > 100 || nota < 0 {
        fmt.Println("Nota inválida!") // Informa que a nota é inválida
        fmt.Println("Insira a nota: ") // Solicita uma nova entrada
        fmt.Scanf("%d", &nota) // Lê a nova entrada do usuário
    }
  
    // Determina e exibe o status de aprovação ou reprovação baseado na nota
    if nota >= 70 && nota <= 100 {
        fmt.Println("Aprovado!") // Nota dentro do intervalo de aprovação
    } else {
        fmt.Println("Reprovado!") // Nota fora do intervalo de aprovação
    }
}
