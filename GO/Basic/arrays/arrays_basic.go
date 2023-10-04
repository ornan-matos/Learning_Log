package main
import "fmt"

func main() {
	marcas := marcasRefri()
	marcas2 := marcaChocolate()
	fmt.Println("Essas são as marcas de refrigerante:", marcas)
	fmt.Println("Essas são as marcas de chocolate:", marcas2)
}

func marcasRefri() [4]string {
	var refri [4]string 
	refri[0] = "coca-cola"
	refri[1] = "sprite"
	refri[2] = "pepsi"
	refri[3] = "fanta"
	
	return refri
}

func marcaChocolate() [3]string  {
	var choco [3]string
	choco[0] = "garoto"
	choco[1] = "lacta"
	choco[2] = "nestle"

	return choco
}