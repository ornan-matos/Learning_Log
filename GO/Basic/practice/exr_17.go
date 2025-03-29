package main

/*
Verifica se um número inteiro é um palíndromo. Um número palíndromo é aquele que permanece o mesmo quando lido de trás para frente, como 121 ou 12321. O código realiza a verificação convertendo o número em uma lista de dígitos e comparando os elementos de maneira simétrica.
*/

import "fmt"

// Função isPalindrome recebe um número inteiro e retorna verdadeiro se o número for um palíndromo, falso caso contrário.
func isPalindrome(x int) bool {

  // Se o número for negativo, ele não pode ser um palíndromo, pois números negativos não são simétricos.
  if x < 0 {
    return false
  }

  // Cria um slice para armazenar os dígitos do número.
  var digitos []int

  // Armazena o número original para manipulação.
  n := x

  // Converte o número em uma lista de dígitos.
  for n > 0 {

    // Obtém o último dígito do número (resto da divisão por 10).
    digito := n % 10

    // Adiciona o dígito à frente da lista de dígitos.
    digitos = append([]int{digito}, digitos...)

    // Divide o número por 10 para remover o último dígito.
    n = n / 10
  }

  // Compara os dígitos na lista para verificar se são simétricos (palíndromos).
  for i := 0; i < len(digitos)/2; i++ {
        // Compara os elementos nas posições i e len(slice)-1-i
        if digitos[i] != digitos[len(digitos)-1-i] {
            // Se algum par de dígitos não for igual, retorna falso (não é um palíndromo).
            return false
        }
    }

    // Se a comparação de todos os dígitos for bem-sucedida, o número é um palíndromo.
    return true
}

func main() {

  // Chama a função isPalindrome passando um número (-121).
  num := isPalindrome(-121)

  // Exibe se o número é um palíndromo ou não com base no retorno da função.
  if num {
    fmt.Println("O número é um palíndromo.")
  } else {
    fmt.Println("O número não é um palíndromo.")
  }
}

