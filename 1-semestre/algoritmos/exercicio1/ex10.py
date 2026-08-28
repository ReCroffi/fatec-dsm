def entrada():
    return int(input("Entre com o número: "))


def check(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Igual a Zero"


n = entrada()

verificacao = check(num=n)

print(f"{n} é {verificacao}")
