"""Testes dos 16 exercícios da Aula 05 (25/08).

Rodar de dentro de exercicio1/:

    .venv/bin/pytest            # todos
    .venv/bin/pytest -k ex14    # só os que têm "ex14" no nome
    .venv/bin/pytest -v         # mostra cada caso separado

Só as funções de cálculo/decisão entram aqui. As ler_*() dependem de input()
e ficam de fora.
"""

import pytest

import ex1
import ex2
import ex3
import ex4
import ex5
import ex6
import ex7
import ex9
import ex10
import ex11
import ex12
import ex13
import ex14
import ex15
import ex16


# =============================================================================
# ex1 — dois números: soma, subtração, multiplicação e divisão
# teste de mesa: 20 e 4
# funções: ex1.soma, ex1.subtracao, ex1.multiplicacao, ex1.divisao
# atenção: divisao(a, 0) devolve None, não levanta erro
# =============================================================================
def test_ex1_soma():
    assert ex1.soma(20, 4) == 24


def test_ex1_subtracao():
    assert ex1.subtracao(20, 4) == 16


def test_ex1_multiplicacao():
    assert ex1.multiplicacao(20, 4) == 80


def test_ex1_divisao():
    assert ex1.divisao(20, 4) == 5


def test_ex1_divisao_por_zero_retorna_none():
    assert ex1.divisao(20, 0) is None


# =============================================================================
# ex2 — área do retângulo
# teste de mesa: 8 e 5 (esperado 40)
# função: ex2.calcular_area(base, altura)
# =============================================================================
def test_ex2_area_do_retangulo():
    assert ex2.calcular_area(8, 5) == 40


# =============================================================================
# ex3 — média de três notas
# teste de mesa: 7, 5 e 8 (esperado 6.67 arredondado)
# função: ex3.calcular_media(n1, n2, n3)
# =============================================================================
def test_ex3_calculo_media_tres_notas():
    assert round(ex3.calcular_media(7, 5, 8), 2) == 6.67


# =============================================================================
# ex4 — antecessor e sucessor de um inteiro
# teste de mesa: 10 (esperado 9 e 11)
# função: ex4.antecessor_e_sucessor(num) -> tupla
# =============================================================================
def test_ex4_antecessor_sucessor():
    assert ex4.antecessor_e_sucessor(10) == (9, 11)


# =============================================================================
# ex5 — total da compra: quantidade x preço
# teste de mesa: 4 e 25 (esperado 100)
# função: ex5.calcular_total(quantidade, preco)
# =============================================================================
def test_ex5_total_compra():
    assert ex5.calcular_total(4, 25) == 100


# =============================================================================
# ex6 — Celsius para Fahrenheit
# teste de mesa: 25 °C (esperado 77)
# função: ex6.celsius_para_fahrenheit(celsius)
# =============================================================================
def test_ex6_conversao_celsius_fahrenheit():
    assert ex6.celsius_para_fahrenheit(25) == 77


# =============================================================================
# ex7 — área do trapézio
# teste de mesa: 10, 6 e 4 (esperado 32)
# função: ex7.calcular_area(base_maior, base_menor, altura)
# =============================================================================
def test_ex7_area_do_trapezio():
    assert ex7.calcular_area(10, 6, 4) == 32


# =============================================================================
# ex8 — "Olá, <nome>"
# sem função de cálculo: o arquivo é só entrada e saída, não há o que testar
# =============================================================================


# =============================================================================
# ex9 — média: aprovado (>= 6) ou reprovado
# teste de mesa: 7, 5 e 8; borda 6, 6 e 6 (média exatamente 6 -> Aprovado)
# funções: ex9.calcular_media(n1, n2, n3), ex9.situacao(media)
# =============================================================================
def test_ex9_calcular_media():
    assert round(ex9.calcular_media(7, 5, 8), 2) == 6.67


@pytest.mark.parametrize(
    "media, esperado",
    [
        (7, "Aprovado"),
        (6, "Aprovado"),  # a borda: >= 6 aprova
        (5.99, "Reprovado"),
        (5, "Reprovado"),
    ],
)
def test_ex9_situacao(media, esperado):
    assert ex9.situacao(media) == esperado


# =============================================================================
# ex10 — número: positivo, negativo ou zero
# teste de mesa: 5, -3 e 0
# função: ex10.classificar_numero(num)
# =============================================================================
@pytest.mark.parametrize(
    "entrada, esperado",
    [
        (5, "Positivo"),
        (-3, "Negativo"),
        (0, "Igual a Zero"),
    ],
)
def test_ex10_positivo_negativo_zero(entrada, esperado):
    assert ex10.classificar_numero(entrada) == esperado


# =============================================================================
# ex11 — maior entre dois números, considerando igualdade
# teste de mesa: 8 e 3, 3 e 8, 4 e 4
# função: ex11.comparar(n1, n2) -> frase pronta
# =============================================================================
@pytest.mark.parametrize(
    "n1, n2, esperado",
    [
        (8, 3, "8 é maior que 3"),
        (3, 8, "3 é menor que 8"),
        (4, 4, "4 é igual a 4"),
    ],
)
def test_ex11_comparar(n1, n2, esperado):
    assert ex11.comparar(n1, n2) == esperado


# =============================================================================
# ex12 — maior de idade
# teste de mesa: 17, 18 e 19 (borda: 18 já é maior de idade)
# função: ex12.classificar_idade(idade)
# =============================================================================
@pytest.mark.parametrize(
    "entrada, esperado",
    [
        (17, "Menor de idade"),
        (18, "Maior de idade"),
        (19, "Maior de idade"),
    ],
)
def test_ex12_maioridade(entrada, esperado):
    assert ex12.classificar_idade(entrada) == esperado


# =============================================================================
# ex13 — situação por faixas de nota
# teste de mesa: 4, 6 e 8 — uma entrada por faixa
# função: ex13.classificar_nota(nota)
# =============================================================================
@pytest.mark.parametrize(
    "entrada, esperado",
    [
        (4, "Menor que a média"),
        (6, "Média"),
        (8, "Maior que a média"),
    ],
)
def test_ex13_faixa_nota(entrada, esperado):
    assert ex13.classificar_nota(entrada) == esperado


# =============================================================================
# ex14 — aprovação: nota >= 6 E frequência >= 75
# teste de mesa: 7/80, 7/50, 5/80, 5/50; borda 6/75 -> Aprovado
# função: ex14.classificar_aprovacao(media, frequencia)
# =============================================================================
@pytest.mark.parametrize(
    "media, frequencia, esperado",
    [
        (7, 80, "Aprovado"),
        (7, 50, "Reprovado"),
        (5, 80, "Reprovado"),
        (5, 50, "Reprovado"),
        (6, 75, "Aprovado"),  # a borda: os dois no limite aprovam
        (5.99, 75, "Reprovado"),
        (6, 74, "Reprovado"),
    ],
)
def test_ex14_aprovacao(media, frequencia, esperado):
    assert ex14.classificar_aprovacao(media, frequencia) == esperado


# =============================================================================
# ex15 — desconto: VIP OU compra > 100
# teste de mesa: 150/S, 150/N, 50/S, 50/N; borda 100 -> reprovado (é > 100)
# função: ex15.aprovar_desconto(vip, valor)  — vip é bool
# =============================================================================
@pytest.mark.parametrize(
    "vip, valor, esperado",
    [
        (True, 150, "Desconto aprovado"),
        (False, 150, "Desconto aprovado"),
        (True, 50, "Desconto aprovado"),
        (False, 50, "Desconto reprovado"),  # só reprova com os dois falsos
        (False, 100, "Desconto reprovado"),  # a borda: o corte é > 100
        (False, 100.01, "Desconto aprovado"),
    ],
)
def test_ex15_desconto(vip, valor, esperado):
    assert ex15.aprovar_desconto(vip, valor) == esperado


# =============================================================================
# ex16 — acesso: login E senha E NÃO bloqueado
# teste de mesa: as 8 combinações; só 123/456/False aprova
# função: ex16.aprovar_login(login, senha, bloqueado)
# constantes do módulo: ex16.LOGIN_TESTE (123), ex16.SENHA_TESTE (456)
# =============================================================================
@pytest.mark.parametrize(
    "login, senha, bloqueado, esperado",
    [
        (123, 456, False, "Login aprovado"),  # única combinação que aprova
        (123, 456, True, "Login reprovado"),
        (123, 999, False, "Login reprovado"),
        (123, 999, True, "Login reprovado"),
        (999, 456, False, "Login reprovado"),
        (999, 456, True, "Login reprovado"),
        (999, 999, False, "Login reprovado"),
        (999, 999, True, "Login reprovado"),
    ],
)
def test_ex16_acesso(login, senha, bloqueado, esperado):
    assert ex16.aprovar_login(login, senha, bloqueado) == esperado
