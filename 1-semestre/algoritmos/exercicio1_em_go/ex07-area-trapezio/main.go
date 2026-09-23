package main

// Ex 7 — Área do trapézio
// Lê a base maior, a base menor e a altura de um trapézio e exibe sua área.
import "fmt"

func main() {

	var baseMenor, baseMaior, altura float32
	fmt.Println("Entre o valor da base menor: ")
	_, err := fmt.Scan(&baseMenor)
	if err != nil {
		fmt.Println("Valor incorreto.")
		return
	}
	fmt.Println("Entre o valor da base maior: ")
	_, err = fmt.Scan(&baseMaior)
	if err != nil {
		fmt.Println("Valor incorreto.")
		return
	}
	fmt.Println("Entre o valor da altura: ")
	_, err = fmt.Scan(&altura)
	if err != nil {
		fmt.Println("Valor incorreto.")
		return
	}
	area := ((baseMaior + baseMenor) * altura) / 2
	fmt.Printf("A área do trapézio é: %.2f\n", area)
}
