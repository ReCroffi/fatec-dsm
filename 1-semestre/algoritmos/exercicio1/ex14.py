def ler_media_frequencia():
    media = round(float(input("Entre com a média do aluno: ")), 2)
    frequencia = int(input("Entre a frequencia do aluno: "))
    return media, frequencia


def classificar_aprovacao(media, frequencia):
    if media >= 6 and frequencia >= 75:
        return "Aprovado"
    else:
        return "Reprovado"


if __name__ == "__main__":
    media, frequencia = ler_media_frequencia()
    classificacao = classificar_aprovacao(media, frequencia)
    print(classificacao)
