package main

import (
	"fmt"
)

/* 
Este programa implementa um cache simples usando um mapa (map) em Go.
Ele permite armazenar e recuperar informações de livros e CDs a partir de chaves específicas.
Há um limite global para o tamanho do cache, evitando que ele ultrapasse um valor máximo.
*/

const (
	globaLimit    int    = 100  // Limite base para cálculos de cache
	MaxCacheSize  int    = 10 * globaLimit // Tamanho máximo permitido para o cache

	CacheKeyBook  string = "book" // Prefixo para chaves de livros no cache
	CacheKeyCD    string = "cd_"  // Prefixo para chaves de CDs no cache
)

var cache map[string]string // Mapa que atua como o cache em memória

// Função auxiliar para recuperar um valor do cache usando uma chave específica
func cacheGet(key string) string {
	return cache[key]
}

// Recupera um livro do cache com base no ISBN
func GetBook(isbn string) string {
	return cacheGet(CacheKeyBook + isbn)
}

// Recupera um CD do cache com base no SKU
func GetCD(sku string) string {
	return cacheGet(CacheKeyCD + sku)
}

// Função auxiliar para armazenar um valor no cache, respeitando o limite máximo
func cacheSet(key, val string) {
	if len(cache)+1 >= MaxCacheSize { // Verifica se o cache atingiu o limite antes de adicionar
		return
	}
	cache[key] = val // Adiciona o valor ao cache
}

// Armazena um livro no cache usando o ISBN como parte da chave
func SetBook(isbn string, name string) {
	cacheSet(CacheKeyBook+isbn, name)
}

// Armazena um CD no cache usando o SKU como parte da chave
func SetCD(sku string, title string) {
	cacheSet(CacheKeyCD+sku, title)
}

func main() {
	cache = make(map[string]string) // Inicializa o cache como um mapa vazio

	// Adiciona um livro e um CD ao cache
	SetBook("1234-5678", "Get Ready To Go")
	SetCD("1234-5678", "Get Ready To Go Audio Book")

	// Recupera e imprime os itens armazenados no cache
	fmt.Println("Book:", GetBook("1234-5678"))
	fmt.Println("CD:", GetCD("1234-5678"))
}
