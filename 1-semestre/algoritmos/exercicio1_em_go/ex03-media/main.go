package main

// Ex 3 — Média
// Lê três notas e exibe a média aritmética entre elas.

import "fmt"

func main() {
	var n1, n2, n3 float32
	fmt.Println("Entre a primeira nota: ")
	fmt.Scan(&n1)
	fmt.Println("Entre a segunda nota: ")
	fmt.Scan(&n2)
	fmt.Println("Entre a terceira nota: ")
	fmt.Scan(&n3)
	fmt.Println("Média das notas: ", (n1+n2+n3)/3)

}
