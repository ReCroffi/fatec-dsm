def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."

def entrada():
    n1 = float(input("Entre um número: "))
    n2 = float(input("Entre o segundo número: "))
    return n1, n2


a, b = entrada()

adicao = soma(a,b)
sub = subtracao(a,b)
multi = multiplicacao(a,b)
div = divisao(a,b)

print(f"Soma: {adicao} \nSubtração: {sub} \nMultiplicação: {multi} \nDivisão: {div}")