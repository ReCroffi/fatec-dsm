def notas():
    n1 = float(input("Entre com a nota 1: "))
    n2 = float(input("Entre com a nota 2: "))
    n3 = float(input("Entre com a nota 3: "))
    return n1, n2, n3


def calculo_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def aprov(media):
    match media:
        case media if media >= 6:
            return "Aprovado"
        case _:
            return "Reprovado"


n1, n2, n3 = notas()
media = calculo_media(n1, n2, n3)
aprovacao = aprov(media)

print(f"A média do aluno é {media}, e ele está {aprovacao}")
