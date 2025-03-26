
package main

import (
	"fmt"
	"math"
	"math/big"
)

/* O código demonstra a diferença entre os tipos de dados inteiros em Go,especificamente os tipos int64 e big.Int. Ele mostra como ocorre um overflow com o tipo int64 e como podemos usar o tipo big.Int
para lidar com números maiores que o valor máximo do tipo int64.
*/

func main() {
	// O maior valor possível para um inteiro de 64 bits
	intA := math.MaxInt64
	
	// Aqui estamos tentando somar 1 ao maior valor possível para int64,
	// o que resulta em um overflow, pois o valor excede o limite de int64.
	intA = intA + 1

	// Criamos um big.Int inicializado com o maior valor de int64
	bigA := big.NewInt(math.MaxInt64)

	// Aqui, somamos 1 ao big.Int. Não ocorre overflow, pois big.Int
	// pode armazenar números inteiros arbitrariamente grandes.
	bigA.Add(bigA, big.NewInt(1))

	// Exibindo os resultados. O intA causou overflow, enquanto o bigA
	// pode armazenar corretamente o valor.
	fmt.Println("MaxInt64: ", math.MaxInt64)
	fmt.Println("Int :", intA) // O valor de intA após o overflow
	fmt.Println("Big Int : ", bigA.String()) // O valor de bigA sem overflow
}

