package main

// Ex 4 — Antecessor e Sucessor
// Lê um número e exibe seu antecessor e seu sucessor.
import "fmt"

func main() {
	var n int
	fmt.Println("Entre um número: ")
	fmt.Scan(&n)
	fmt.Println("Antecessor: ", n-1)
	fmt.Println("Sucessor: ", n+1)
}
