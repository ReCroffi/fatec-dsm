def ler_numero():
    return int(input("Entre o número: "))


def antecessor_e_sucessor(num):
    return num - 1, num + 1


if __name__ == "__main__":
    num = ler_numero()

    ant, suc = antecessor_e_sucessor(num)

    print(f"O antecessor de {num} é {ant} e o sucessor é {suc}")
