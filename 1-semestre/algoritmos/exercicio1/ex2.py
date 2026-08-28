def ler_dimensoes():
    base = float(input("Entre com a base do retangulo: "))
    altura = float(input("Entre com a altura do retangulo: "))
    return base, altura


def calcular_area(base, altura):
    return base * altura


if __name__ == "__main__":
    base, altura = ler_dimensoes()

    area = calcular_area(base, altura)

    print(f"A área do retangulo é: {area}")
