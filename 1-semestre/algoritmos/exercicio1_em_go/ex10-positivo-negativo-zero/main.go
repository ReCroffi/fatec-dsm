package main

// Ex 10 — Positivo, negativo ou zero
// Lê um número e exibe se ele é positivo, negativo ou igual a zero.
import "fmt"

func main() {
	var n int
	fmt.Printf("Entre um valor: \n")

	_, err := fmt.Scan(&n)
	if err != nil {
		fmt.Println("Erro a ler a nota! ")
	} else {

		if n > 0 {
			fmt.Printf("%d é positivo\n", n)
		} else if n < 0 {
			fmt.Printf("%d é negativo\n", n)
		} else {
			fmt.Printf("%d é zero :P", n)
		}

	}
}
