def ler_notas():
    n1 = float(input("Entre com a nota 1: "))
    n2 = float(input("Entre com a nota 2: "))
    n3 = float(input("Entre com a nota 3: "))
    return n1, n2, n3


def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def situacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


if __name__ == "__main__":
    n1, n2, n3 = ler_notas()

    media = calcular_media(n1, n2, n3)
    aprovacao = situacao(media)

    print(f"A média do aluno é {media:.2f}, e ele está {aprovacao}")
