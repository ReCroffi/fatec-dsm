def ler_nota():
    return round(float(input("Entre com a nota: ")), 2)


def classificar_nota(nota):
    if nota == 6:
        return "Média"
    elif nota > 6:
        return "Maior que a média"
    else:
        return "Menor que a média"


if __name__ == "__main__":
    nota = ler_nota()
    classificacao = classificar_nota(nota)
    print(classificacao)
