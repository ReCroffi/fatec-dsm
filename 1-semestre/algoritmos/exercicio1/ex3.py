def ler_notas():
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    return n1, n2, n3


def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


if __name__ == "__main__":
    n1, n2, n3 = ler_notas()

    media = round(calcular_media(n1, n2, n3), 2)
    print(f"A média do aluno é: {media}")
