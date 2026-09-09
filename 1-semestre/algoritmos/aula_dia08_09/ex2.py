def ajuste_percentual(valor, percentual):
    """
    Ajusta um valor com base em um percentual.

    :param valor: O valor original da compra a ser ajustado.
    :param percentual: O percentual de ajuste (positivo para aumento, negativo para redução).
    :return: O valor ajustado.
    """
    ajuste = valor * (percentual / 100)
    return valor + ajuste

while True:
    try:
        valor_compra = float(input('Entre o valor da compra: '))
        percentual_ajuste = float(input('Entre o percentual de ajuste (positivo para aumento, negativo para redução): '))
        
        valor_ajustado = ajuste_percentual(valor_compra, percentual_ajuste)
        print(f'O valor ajustado da compra é: {valor_ajustado:.2f}')
        
        continuar = input('Deseja continuar? [S/N]: ').upper()
        if continuar == 'N':
            print('Programa encerrado!')
            break
        elif continuar != 'S':
            print('Opção inválida! Continuando...')
    except ValueError:
        print('Entrada inválida! Por favor, insira números válidos.')