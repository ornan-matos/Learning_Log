package main
import "fmt"
func main() {

  marca := make(map[int]string)

  marca [1] = "FORD" 
  marca [2] = "MERCEDES"
  marca [3] = "FIAT"

  for _, value := range marca{
  fmt.Println(value)
}
  nome := make(map[string]string)
  nome["O"] = "Ornan"
  nome["L"] = "Luiz"
  
  fmt.Printf("\nElemento map nome pessoal:\n")
  fmt.Println(nome["O"])
}
