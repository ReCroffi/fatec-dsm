package main

// Ex 8 — Olá
// Lê o nome da pessoa e exibe uma saudação com esse nome.
import "fmt"

func main() {
	var name string
	fmt.Print("Digite seu nome: ")
	fmt.Scanln(&name)
	fmt.Printf("Olá, %s!\n", name)
}
