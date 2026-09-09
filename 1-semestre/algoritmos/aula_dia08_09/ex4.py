def saldo_apos_meses(saldo_inicial, meses):
    saldo_atual = saldo_inicial
    for mes in range(1, meses + 1):
        saldo_atual += 25
        print(f'Saldo após {mes} mês(es): {saldo_atual:.2f}')
    return saldo_atual

while True:
    try:
        saldo_inicial = float(input('Entre o saldo inicial: '))
        meses = int(input('Entre o número de meses: '))
        
        saldo_final = saldo_apos_meses(saldo_inicial, meses)
        print(f'O saldo final após {meses} mês(es) é: {saldo_final:.2f}')
        
        continuar = input('Deseja continuar? [S/N]: ').upper()
        if continuar == 'N':
            print('Programa encerrado!')
            break
        elif continuar != 'S':
            print('Opção inválida! Continuando...')
    except ValueError:
        print('Entrada inválida! Por favor, insira números válidos.')