def ler_compra():
    quantidade = int(input("Entre a quantidade de itens: "))
    preco = float(input("Entre o valor individual do item: "))
    return quantidade, preco


def calcular_total(quantidade, preco):
    return quantidade * preco


if __name__ == "__main__":
    quantidade, preco = ler_compra()

    valor_total = calcular_total(quantidade, preco)

    print(f"O valor total da compra foi: {valor_total}")
