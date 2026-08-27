def entrada():
    n1 = int(input("Entre o número: "))
    return n1

def check(num):
    return num+1, num-1

num = entrada()

ant, suc = check(num)

print(f"O antecessor de {num} é {ant} e o sucessor é {suc}")
