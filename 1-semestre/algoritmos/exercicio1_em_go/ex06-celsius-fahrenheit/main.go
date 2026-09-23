package main

import "fmt"

// Ex 6 — Celsius para Fahrenheit
// Lê uma temperatura em Celsius e exibe o valor convertido para Fahrenheit.

func main() {
	tempCelsius := 0.0
	fmt.Print("Digite a temperatura em Celsius: ")
	_, err := fmt.Scan(&tempCelsius)
	if err != nil {
		fmt.Println("Erro ao ler a temperatura.")
		return
	}

	tempFahrenheit := (tempCelsius * 9 / 5) + 32
	fmt.Printf("A temperatura em Fahrenheit é: %.2f\n", tempFahrenheit)
}
