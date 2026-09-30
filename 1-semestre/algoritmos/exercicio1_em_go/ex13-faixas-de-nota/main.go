package main

// Ex 13 — Faixas de nota
// Lê uma nota e exibe se ela é igual, abaixo ou acima da média (média = 6).
import "fmt"

func main() {
	var n int
	fmt.Printf("Digite a nota do aluno: \n")
	_, err := fmt.Scan(&n)
	if err != nil {
		fmt.Println("Erro a ler a nota!\n ")
	} else {
		if n < 0 || n > 10 {
			for {
				fmt.Printf("Entre uma nota válida: \n")
				_, err = fmt.Scan(&n)
				if err != nil {
					fmt.Printf("Erro ao ler a nota\n")
				} else if n >= 0 && n <= 10 {
					break
				}
				fmt.Printf("Valor inválido\n")
			}
		}

		if n < 6 {
			fmt.Printf("Abaixo da média")
		} else if n == 6 {
			fmt.Printf("Na média")
		} else {
			fmt.Printf("Acima da média")
		}
	}
}
