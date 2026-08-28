def ler_numero():
    return int(input("Entre com o número: "))


def classificar_numero(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Igual a Zero"


if __name__ == "__main__":
    num = ler_numero()

    classificacao = classificar_numero(num)

    print(f"{num} é {classificacao}")
