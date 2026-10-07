# Algoritmos e Lógica de Programação

Professor: Eric — FATEC Olímpia/SP, 1º semestre de DSM.

A matéria é dada e entregue em **pseudocódigo (VisuAlg)**, sempre com teste de mesa.
Aqui os mesmos exercícios são **refeitos em linguagens de verdade** (Python, Go e C):
a entrega oficial continua sendo o PDF em pseudocódigo, o código é a versão praticada.

| Pasta | O que é |
|---|---|
| [`exercicio1/`](exercicio1/) | Aula 05 — operadores, lógica, tabela-verdade e teste de mesa, em Python (16 de 16, com testes automatizados) |
| [`exercicio1_em_go/`](exercicio1_em_go/) | Os mesmos 16 exercícios da Aula 05 em Go (13 de 16) |
| [`exercicios_em_C/`](exercicios_em_C/) | Os 16 exercícios da Aula 05 em C, mais os 6 da lista de repetição com enquanto (06/10), com Makefile e tarefas do VS Code (22 de 22) |
| [`aula_dia08_09/`](aula_dia08_09/) | Aula de 08/09 — laços de repetição e funções, com os fluxogramas no draw.io |

---

## exercicio1 — Aula 05 (25/08/2026)

- Enunciado: [`25_08 Atividade Algoritmos.pdf`](exercicio1/25_08%20Atividade%20Algoritmos.pdf)
- Entrega em pseudocódigo + teste de mesa: [`Exercicios_algoritmo_renan_croffi.pdf`](exercicio1/Exercicios_algoritmo_renan_croffi.pdf)

São 16 exercícios. Progresso da versão em Python: **16 de 16** — Partes A e B concluídas.

### Parte A — operadores matemáticos

| # | Problema | Teste de mesa | Python |
|---|---|---|---|
| 1 | Dois números: soma, subtração, multiplicação e divisão | 20 e 4 | [`ex1.py`](exercicio1/ex1.py) |
| 2 | Área de um retângulo | 8 e 5 | [`ex2.py`](exercicio1/ex2.py) |
| 3 | Média de três notas | 7, 5 e 8 | [`ex3.py`](exercicio1/ex3.py) |
| 4 | Antecessor e sucessor de um inteiro | 10 | [`ex4.py`](exercicio1/ex4.py) |
| 5 | Total da compra: quantidade × preço | 4 e 25 | [`ex5.py`](exercicio1/ex5.py) |
| 6 | Celsius para Fahrenheit | 25 °C | [`ex6.py`](exercicio1/ex6.py) |
| 7 | Área do trapézio | 10, 6 e 4 | [`ex7.py`](exercicio1/ex7.py) |
| 8 | Ler o nome e mostrar "Olá, \<nome\>" | entrada e saída | [`ex8.py`](exercicio1/ex8.py) |

### Parte B — decisões

| # | Problema | Teste de mesa | Python |
|---|---|---|---|
| 9 | Média: aprovado (>= 6) ou reprovado | 7 e 5 | [`ex9.py`](exercicio1/ex9.py) |
| 10 | Número: positivo, negativo ou zero | 5, -3 e 0 | [`ex10.py`](exercicio1/ex10.py) |
| 11 | Maior entre dois números, considerando igualdade | 8 e 3, 3 e 8, 4 e 4 | [`ex11.py`](exercicio1/ex11.py) |
| 12 | Maior de idade | 17, 18 e 19 | [`ex12.py`](exercicio1/ex12.py) |
| 13 | Situação por faixas de nota | 4, 6 e 8 — uma por faixa | [`ex13.py`](exercicio1/ex13.py) |
| 14 | Aprovação: nota >= 6 **E** frequência >= 75 | 7/80, 7/50, 5/80, 5/50 | [`ex14.py`](exercicio1/ex14.py) |
| 15 | Desconto: VIP **OU** compra > 100 | 150/S, 150/N, 50/S, 50/N | [`ex15.py`](exercicio1/ex15.py) |
| 16 | Acesso: login **E** senha **E NÃO** bloqueado | as 8 combinações de login, senha e bloqueio | [`ex16.py`](exercicio1/ex16.py) |

---

## aula_dia08_09 — laços e funções (08/09/2026)

Quatro exercícios que repetem até o usuário decidir parar (`while` com
confirmação ou `try/except` para entrada inválida). Cada um tem o fluxograma
feito no [draw.io](https://app.diagrams.net): o `.drawio` é o arquivo editável e
o `.png` é a imagem exportada.

| # | Problema | Python | Fluxograma |
|---|---|---|---|
| 1 | Multiplicação de dois números, recusando negativos | [`ex1.py`](aula_dia08_09/ex1.py) | [`multiplicacaocomcondicao`](multiplicacaocomcondicao.drawio.png) |
| 2 | Valor da compra com ajuste percentual (aumento ou desconto) | [`ex2.py`](aula_dia08_09/ex2.py) | [`somacomajuste`](somacomajuste.drawio.png) |
| 3 | Saque com taxa de 5%, sem deixar o saldo negativo | [`ex3.py`](aula_dia08_09/ex3.py) | [`saquecomtaxa`](saquecomtaxa.drawio.png) |
| 4 | Saldo mês a mês, com depósito fixo de R$ 25 | [`ex4.py`](aula_dia08_09/ex4.py) | [`atualizacaosaldo`](atualizacaosaldo.drawio.png) |

---

## Como rodar

Só biblioteca padrão, nenhuma dependência:

```bash
python3 exercicio1/ex1.py
```

Os scripts leem os valores por `input()` — use os testes de mesa da tabela acima
para conferir se a saída bate com a do pseudocódigo.

Cada exercício separa as funções (fora da guarda `if __name__ == "__main__"`) do
roteiro de entrada e saída, então dá para importar qualquer um e chamar as funções
direto. Os testes de mesa estão automatizados em
[`exercicio1/test_exercicio1.py`](exercicio1/test_exercicio1.py):

```bash
cd exercicio1
python3 -m venv .venv && .venv/bin/pip install pytest   # só na primeira vez
.venv/bin/pytest -v
```

A venv fica em `exercicio1/.venv/`, fora do versionamento. Os mesmos testes
rodam no GitHub Actions a cada push nesta pasta (o selo no README da raiz).

As versões em Go e em C têm as instruções no README de cada pasta:
[`exercicio1_em_go/`](exercicio1_em_go/) e [`exercicios_em_C/`](exercicios_em_C/).
