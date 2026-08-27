def entrada():
    n1 = float(input("Entre com a base do retangulo: "))
    n2 = float(input("Entre com a altura do retangulo: "))
    return n1, n2
def area(a, b):
    return a * b


a, b  = entrada()

area = area(a,b)

print(f"A área do retangulo é: {area}")