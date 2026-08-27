def tempC():
    t = float(input("Entre a temperatura em Celsius: "))
    return t


def converter(temp):
    tf = (9 / 5 * temp) + 32
    return tf


temperatura = tempC()
tempF = converter(temp=temperatura)
print(f"{temperatura}ºC em Fahrenheit é: {tempF}")
