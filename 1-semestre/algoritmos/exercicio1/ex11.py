def ler_numeros():
    n1 = int(input("Entre o primeiro número: "))
    n2 = int(input("Entre o segundo número: "))
    return n1, n2


def comparar(n1, n2):
    if n1 > n2:
        return f"{n1} é maior que {n2}"
    elif n1 == n2:
        return f"{n1} é igual a {n2}"
    else:
        return f"{n1} é menor que {n2}"


if __name__ == "__main__":
    n1, n2 = ler_numeros()

    comparacao = comparar(n1, n2)

    print(comparacao)
