def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return None
    return a / b


def ler_numeros():
    n1 = float(input("Entre um número: "))
    n2 = float(input("Entre o segundo número: "))
    return n1, n2


if __name__ == "__main__":
    a, b = ler_numeros()

    adicao = soma(a, b)
    sub = subtracao(a, b)
    multi = multiplicacao(a, b)
    div = divisao(a, b)

    resultado_div = "indefinida (divisão por zero)" if div is None else div

    print(
        f"Soma: {adicao} \nSubtração: {sub} \n"
        f"Multiplicação: {multi} \nDivisão: {resultado_div}"
    )
