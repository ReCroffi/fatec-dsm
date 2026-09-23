package main

// Ex 2 — Área do retângulo
// Lê a base e a altura de um retângulo e exibe sua área.
import "fmt"

func main() {
	var base, altura float32
	fmt.Println("Entre a base do retangulo: ")
	fmt.Scan(&base)
	fmt.Println("Entre com a altura: ")
	fmt.Scan(&altura)
	fmt.Println("Área do retangulo: ", base*altura)
}
