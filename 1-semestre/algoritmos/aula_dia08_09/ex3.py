def saque(valor, saldo):
    if valor <= saldo:
        saldo -= valor * 1.05
        return saldo
    else:
        print("Saldo insuficiente.")
        return saldo


saldo_atual = float(input('Entre o saldo atual: '))
while True:
    try:
        print(f'Saldo atual: {saldo_atual:.2f}')
        valor_saque = float(input('Entre o valor do saque: '))
        
        saldo_atual = saque(valor_saque, saldo_atual)
        print(f'O saldo após o saque é: {saldo_atual:.2f}')
        
        continuar = input('Deseja continuar? [S/N]: ').upper()
        if continuar == 'N':
            print('Programa encerrado!')
            break
        elif continuar != 'S':
            print('Opção inválida! Continuando...')
    except ValueError:
        print('Entrada inválida! Por favor, insira números válidos.')