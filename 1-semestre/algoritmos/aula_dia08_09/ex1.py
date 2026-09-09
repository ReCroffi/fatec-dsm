RODANDO = True

def continuar():
    global RODANDO
    resp = input('Deseja continuar? [S/N]: ').upper()
    if resp == 'N':
        RODANDO = False
        print('Programa encerrado!')
    elif resp != 'S':
        print('Opção inválida!')

        
while RODANDO:
    n1 = int(input('Entre um número: '))
    n2 = int(input('Entre outro número: '))

    if n1 < 0 or n2 < 0:
        print('Não é permitido números negativos')
        continuar()
    else:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é: {mult}')
        continuar()



    