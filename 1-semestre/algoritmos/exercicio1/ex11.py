def entrada():
    n1 = int(input("Entre o primeiro número: "))
    n2 = int(input("Entre o segundo número: "))
    return n1, n2


def check(n1, n2):
    if n1 > n2:
        return f"{n1} é maior que {n2}"
    elif n1 == n2:
        return f"{n1} é igual {n2}"
    else:
        return f"{n1} é menor que {n2}"


n1, n2 = entrada()

verif = check(n1, n2)
print(f"{verif}")
