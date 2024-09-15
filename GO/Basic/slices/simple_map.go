package main

import "fmt"

/* 

Este programa demonstra o uso de mapas (map) para armazenar
e iterar sobre pares chave-valor. Dois mapas são criados: 
um para armazenar marcas de carros com chaves numéricas, 
e outro para armazenar nomes pessoais com chaves de string.

*/

func main() {

    // Criação de um mapa para associar números a marcas de carros
    marca := make(map[int]string)

    // Adiciona marcas de carros ao mapa "marca"
    marca[1] = "FORD" 
    marca[2] = "MERCEDES"
    marca[3] = "FIAT"

    // Itera sobre o mapa "marca" e imprime os valores (marcas de carros)
    for _, value := range marca {
        fmt.Println(value)
    }

    // Criação de um mapa para associar letras a nomes
    nome := make(map[string]string)
    nome["O"] = "Ornan"
    nome["L"] = "Luiz"

    // Imprime o valor associado à chave "O" no mapa "nome"
    fmt.Printf("\nElemento map nome pessoal:\n")
    fmt.Println(nome["O"])
}