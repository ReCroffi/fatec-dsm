def ler_valor_compra():
    return round(float(input("Entre o valor da compra: ")), 2)


def ler_vip():
    resposta = input("Cliente VIP (S/N): ").upper()
    return resposta == "S"


def aprovar_desconto(vip, valor):
    if vip or valor > 100:
        return "Desconto aprovado"
    else:
        return "Desconto reprovado"


if __name__ == "__main__":
    valor = ler_valor_compra()
    vip = ler_vip()

    desconto = aprovar_desconto(vip, valor)
    print(desconto)
