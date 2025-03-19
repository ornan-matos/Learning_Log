package main

import "fmt"

/*
Este programa em Go cria um mapa de palavras e suas respectivas contagens. 
A função `loop` percorre o mapa para encontrar a palavra com o maior valor (contagem).
No final, a palavra com a maior contagem é impressa junto com o valor associado.
*/

// Definição de um mapa contendo palavras como chave e seus respectivos valores inteiros.
var tabela = map[string]int{
  "Gonna": 3,
  "You": 3,
  "Give": 2,
  "Never": 1,
  "Up": 4,
}

// Função loop percorre o mapa 'tabela' para encontrar a chave (palavra) com o maior valor (contagem).
func loop() string{

  var (
    chave string // Armazena a chave da palavra com maior contagem.
    valor int    // Armazena o valor (contagem) da palavra mais popular.
  )

  // Itera sobre cada chave (palavra) e valor (contagem) do mapa
  for key, value := range tabela {

    // Exibe a palavra e sua contagem
    fmt.Println(key, value)

    // Se a contagem atual for maior do que a armazenada, atualiza a chave e o valor
    if value > valor {
      valor = value
      chave = key
    }
  }

  // Retorna a chave (palavra) com maior contagem
  return chave
}

func main() {

  // Chama a função loop para obter a palavra mais popular
  chave := loop()

  // Imprime um separador visual
  fmt.Println("------------------------------------")

  // Exibe a palavra mais popular e sua contagem
  fmt.Println("A palavra mais popular:", chave)
  fmt.Println("Com a contagem de:", tabela[chave])
}

