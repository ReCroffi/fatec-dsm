def ler_dimensoes():
    base_maior = float(input("Entre com a base maior: "))
    base_menor = float(input("Entre com a base menor: "))
    altura = float(input("Entre a altura: "))
    return base_maior, base_menor, altura


def calcular_area(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2


if __name__ == "__main__":
    base_maior, base_menor, altura = ler_dimensoes()

    area = calcular_area(base_maior, base_menor, altura)

    print(f"A área do trapézio é {area}")
