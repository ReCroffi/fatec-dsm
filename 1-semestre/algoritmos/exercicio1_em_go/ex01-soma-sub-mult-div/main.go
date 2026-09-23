package main

// Ex 1 — Soma, Subtração, Multiplicação e Divisão
// Lê dois números e exibe a soma, a subtração, a multiplicação e a divisão entre eles.
import "fmt"

func main() {
	var a, b float32
	fmt.Println("Entre um numero: ")
	fmt.Scan(&a)
	fmt.Println("Entre outro numero: ")
	fmt.Scan(&b)
	fmt.Println("Soma: ", a+b)
	fmt.Println("Subtração: ", a-b)
	fmt.Println("Multiplicação: ", a*b)
	fmt.Println("Divisão: ", a/b)

}
