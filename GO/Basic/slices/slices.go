package main

import "fmt"
import "reflect"

/*
O código demonstra o uso de slices para armazenar coleções de dados. 
Ele cria dois slices: um de strings chamado 'nomes' e um de inteiros chamado 'numeros'. 
O código utiliza o pacote 'reflect' para imprimir o tipo de cada slice e a quantidade de elementos que eles contêm. 
Além disso, ele exibe os valores armazenados em ambos os slices.
*/

func main() {
	
	//Atribuições de valores (string) ao slice nomes
	nomes := []string{"Ornan", "João", "Carlos", "Maria"}
	
	/*Impressão de informações sobre o tipo (reflect.typeOf) e quantidade de valores
	contidos (len()) no slice */
	fmt.Println(" \n" +
	"Tipo de slice:", reflect.TypeOf(nomes))
	fmt.Println("Quantidade de Valores:", len(nomes), " \n")
	
	//Atribuições de valores (int) ao slice nomes
	numeros := []int{1, 2 ,3, 4}
	
	/*Impressão de informações sobre o tipo (reflect.typeOf) e quantidade de valores
	contidos (len()) no slice */
	fmt.Println("Tipo de slice:", reflect.TypeOf(numeros))
	fmt.Println("Quantidade de Valores:", len(numeros), " \n")

	/*Impressão de todos os valores contidos em cada um dos slices*/
	fmt.Println("Esses são os nomes:", nomes, " \n" +
"Esse são os números:", numeros, " \n")

}
