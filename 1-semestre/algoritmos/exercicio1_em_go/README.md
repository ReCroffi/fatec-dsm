# exercicio1_em_go

Os mesmos 16 exercícios da Aula 05 refeitos em Go. A entrega oficial continua
sendo o PDF em pseudocódigo; aqui é a versão praticada na linguagem, como em
[`../exercicio1/`](../exercicio1/) (Python) e [`../exercicios_em_C/`](../exercicios_em_C/) (C).

Cada exercício é uma pasta com um `main.go` (pacote `main`), e todas dividem o
mesmo módulo ([`go.mod`](go.mod)). Progresso: **13 de 16**: faltam o 12, o 15 e o 16, que ainda têm o `main` vazio, com o enunciado no comentário do topo.

## Parte A — operadores matemáticos

| # | Problema | Teste de mesa | Arquivo | Feito |
|---|---|---|---|---|
| 1 | Dois números: soma, subtração, multiplicação e divisão | 20 e 4 | [`ex01-soma-sub-mult-div/`](ex01-soma-sub-mult-div/main.go) | ✅ |
| 2 | Área de um retângulo | 8 e 5 | [`ex02-area-retangulo/`](ex02-area-retangulo/main.go) | ✅ |
| 3 | Média de três notas | 7, 5 e 8 | [`ex03-media/`](ex03-media/main.go) | ✅ |
| 4 | Antecessor e sucessor de um inteiro | 10 | [`ex04-antecessor-sucessor/`](ex04-antecessor-sucessor/main.go) | ✅ |
| 5 | Total da compra: quantidade × preço | 4 e 25 | [`ex05-total-compra/`](ex05-total-compra/main.go) | ✅ |
| 6 | Celsius para Fahrenheit | 25 °C | [`ex06-celsius-fahrenheit/`](ex06-celsius-fahrenheit/main.go) | ✅ |
| 7 | Área do trapézio | 10, 6 e 4 | [`ex07-area-trapezio/`](ex07-area-trapezio/main.go) | ✅ |
| 8 | Ler o nome e mostrar "Olá, \<nome\>" | um nome qualquer | [`ex08-ola/`](ex08-ola/main.go) | ✅ |

## Parte B — decisões

| # | Problema | Teste de mesa | Arquivo | Feito |
|---|---|---|---|---|
| 9 | Média: aprovado (>= 6) ou reprovado | 7 e 5 | [`ex09-media-aprovacao/`](ex09-media-aprovacao/main.go) | ✅ |
| 10 | Número: positivo, negativo ou zero | 5, -3 e 0 | [`ex10-positivo-negativo-zero/`](ex10-positivo-negativo-zero/main.go) | ✅ |
| 11 | Maior entre dois números, considerando igualdade | 8 e 3, 3 e 8, 4 e 4 | [`ex11-maior-ou-menor/`](ex11-maior-ou-menor/main.go) | ✅ |
| 12 | Maior de idade | 17, 18 e 19 | [`ex12-maioridade/`](ex12-maioridade/main.go) | ⬜ |
| 13 | Situação por faixas de nota | 4, 6 e 8 — uma por faixa | [`ex13-faixas-de-nota/`](ex13-faixas-de-nota/main.go) | ✅ |
| 14 | Aprovação: nota >= 6 **E** frequência >= 75 | 7/80, 7/50, 5/80, 5/50 | [`ex14-aprovacao/`](ex14-aprovacao/main.go) | ✅ |
| 15 | Desconto: VIP **OU** compra >= 100 | 150/S, 150/N, 50/S, 50/N | [`ex15-desconto/`](ex15-desconto/main.go) | ⬜ |
| 16 | Acesso: login **E** senha **E NÃO** bloqueado | as 8 combinações | [`ex16-login/`](ex16-login/main.go) | ⬜ |

---

## Como rodar

Precisa do Go instalado (`go version`). De dentro desta pasta:

```bash
go run ./ex01-soma-sub-mult-div     # compila e roda um exercício
go build ./...                      # confere se todos compilam
go vet ./...                        # aponta erros comuns
```

O `go run` compila num diretório temporário, então não sobra binário na pasta.
Se usar `go build` dentro de um exercício, o executável gerado fica fora do
versionamento pelo `.gitignore` da raiz.
