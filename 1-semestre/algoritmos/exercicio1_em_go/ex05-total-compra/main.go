package main

import "fmt"

// Ex 5 — Total da Compra
// Lê a quantidade de itens e o valor de cada item, e exibe o total da compra.

func main() {
	var qtd int
	var valor float64
	fmt.Printf("Digite a quantidade de itens: ")
	_, err := fmt.Scan(&qtd)
	if err != nil {
		fmt.Println("Erro ao ler a quantidade de itens.")
		return
	}
	fmt.Printf("Digite o valor de cada item: ")
	_, err = fmt.Scan(&valor)
	if err != nil {
		fmt.Println("Erro ao ler o valor de cada item.")
		return
	}
	total := float64(qtd) * valor
	fmt.Printf("O total da compra é: %.2f\n", total)
}
