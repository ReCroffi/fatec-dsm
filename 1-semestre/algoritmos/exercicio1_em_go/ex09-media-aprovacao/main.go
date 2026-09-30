package main

// Ex 9 — Média + aprovação
// Lê duas notas, calcula a média e exibe se o aluno foi aprovado (média >= 6) ou reprovado.
import "fmt"

func main() {
	var n1, n2 float32
	fmt.Println("Entre a nota 1")
	_, err := fmt.Scan(&n1)
	if err != nil {
		fmt.Println("Erro a ler a nota! ")
	}

	fmt.Println("Entre a nota 1")
	_, err = fmt.Scan(&n2)
	if err != nil {
		fmt.Println("Erro a ler a nota! ")
	}
	media := (n1 + n2) / 2
	if media >= 6 {
		fmt.Printf("Aprovado com média : %.2f\n", media)
	} else {
		fmt.Printf("Reprovado com média: %.2f\n", media)
	}
}
