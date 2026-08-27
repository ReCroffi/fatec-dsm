def compras():
    item = int(input("Entre a quantidade de itens: "))
    valor = float(input("Entre o valor individual do item: "))
    return item, valor

def total(quant, preco):
    return quant * preco


quant, preco = compras()

valor_total = total(quant, preco)

print(f"O valor total da compra foi: {valor_total}")
