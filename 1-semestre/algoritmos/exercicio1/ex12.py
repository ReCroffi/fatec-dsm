def ler_idade():
    return int(input("Entre com a idade: "))


def classificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"


if __name__ == "__main__":
    idade = ler_idade()
    classificacao = classificar_idade(idade)

    print(classificacao)
