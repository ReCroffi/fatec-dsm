package main

// Ex 11 — Maior ou menor
// Lê dois números e exibe se são iguais, ou qual deles é o maior e qual é o menor.
import "fmt"

func main() {
	var n1, n2 int
	fmt.Printf("Entre o primeiro número: \n")
	_, err := fmt.Scan(&n1)
	if err != nil {
		fmt.Println("Erro ao ler o número! ")
	} else {
		fmt.Printf("Entre o segundo número: \n")
		_, err = fmt.Scan(&n2)
		if err != nil {
			fmt.Println("Erro ao ler o número! ")
		} else {
			if n1 > n2 {
				fmt.Printf("%d é maior que %d", n1, n2)
			} else if n1 < n2 {
				fmt.Printf("%d é menor que %d", n1, n2)
			} else {
				fmt.Printf("%d é igual a %d", n1, n2)
			}
		}
	}
}
