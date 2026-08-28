SENHA_TESTE = 456
LOGIN_TESTE = 123


def ler_login():
    return int(input("Entre seu numero de usuario: "))


def ler_senha():
    return int(input("Entre sua senha: "))


def ler_bloqueado():
    resposta = input("Usuario Bloqueado (S/N): ").upper()
    return resposta == "S"


def aprovar_login(login, senha, bloqueado):
    if login == LOGIN_TESTE and senha == SENHA_TESTE and not bloqueado:
        return "Login aprovado"
    else:
        return "Login reprovado"


if __name__ == "__main__":
    login = ler_login()
    senha = ler_senha()
    bloqueado = ler_bloqueado()
    acesso = aprovar_login(login, senha, bloqueado)
    print(acesso)
