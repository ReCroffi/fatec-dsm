package main

// Ex 14 — Aprovação
// Lê a nota e a frequência de um aluno e exibe se ele foi aprovado
// (nota >= 6 e frequência >= 75) ou reprovado.
import "fmt"

func main() {
	var nota float32
	var freq int
	fmt.Printf("Entre a nota do aluno:\n ")
	_, err := fmt.Scan(&nota)
	if err != nil {
		fmt.Printf("Erro na leitura da nota. \n")
	}
	fmt.Printf("Entre a frequencia do aluno: \n")
	_, err = fmt.Scan(&freq)
	if err != nil {
		fmt.Printf("Erro na leitura da frequencia! \n")
	}

	if nota >= 6 && freq >= 75 {
		fmt.Printf("Aluno aprovado com média %.2f e frequencia %d", nota, freq)

	} else {
		fmt.Printf("Aluno reprovado")
	}
}
