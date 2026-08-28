def ler_temperatura():
    return float(input("Entre a temperatura em Celsius: "))


def celsius_para_fahrenheit(celsius):
    return (9 / 5 * celsius) + 32


if __name__ == "__main__":
    temperatura = ler_temperatura()

    fahrenheit = celsius_para_fahrenheit(temperatura)

    print(f"{temperatura}ºC em Fahrenheit é: {fahrenheit}")
