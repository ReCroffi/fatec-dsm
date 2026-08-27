def entrada():
    base_maior = float(input("Entre com a base maior: "))
    base_menor = float(input("Entre com a base menor: "))
    altura = float(input("Entre a altura: "))
    return base_maior, base_menor, altura


def area(b, bm, h):
    return ((b + bm) * h) / 2


b, bm, h = entrada()
area_calculada = area(b, bm, h)
print(f"A área do trapézio é {area_calculada}")
