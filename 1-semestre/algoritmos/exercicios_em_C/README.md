# exercicios_em_C

Os mesmos 16 exercícios da Aula 05, refeitos em C — agora porque a aula da
faculdade vai pedir em C. A entrega oficial continua sendo o PDF em pseudocódigo;
aqui é a versão praticada na linguagem, como já foi feito em
[`../exercicio1/`](../exercicio1/) (Python) e
[`../exercicio1_em_go/`](../exercicio1_em_go/) (Go).

Cada pasta tem um `main.c` com o enunciado e o teste de mesa no cabeçalho, e o
corpo do `main` vazio pra resolver.

## Parte A — operadores matemáticos

| # | Problema | Teste de mesa | Arquivo |
|---|---|---|---|
| 1 | Dois números: soma, subtração, multiplicação e divisão | 20 e 4 | [`ex01-soma-sub-mult-div/`](ex01-soma-sub-mult-div/main.c) |
| 2 | Área de um retângulo | 8 e 5 | [`ex02-area-retangulo/`](ex02-area-retangulo/main.c) |
| 3 | Média de três notas | 7, 5 e 8 | [`ex03-media/`](ex03-media/main.c) |
| 4 | Antecessor e sucessor de um inteiro | 10 | [`ex04-antecessor-sucessor/`](ex04-antecessor-sucessor/main.c) |
| 5 | Total da compra: quantidade × preço | 4 e 25 | [`ex05-total-compra/`](ex05-total-compra/main.c) |
| 6 | Celsius para Fahrenheit | 25 °C | [`ex06-celsius-fahrenheit/`](ex06-celsius-fahrenheit/main.c) |
| 7 | Área do trapézio | 10, 6 e 4 | [`ex07-area-trapezio/`](ex07-area-trapezio/main.c) |
| 8 | Ler o nome e mostrar "Olá, \<nome\>" | um nome qualquer | [`ex08-ola/`](ex08-ola/main.c) |

## Parte B — decisões

| # | Problema | Teste de mesa | Arquivo |
|---|---|---|---|
| 9 | Média: aprovado (>= 6) ou reprovado | 7 e 5 | [`ex09-media-aprovacao/`](ex09-media-aprovacao/main.c) |
| 10 | Número: positivo, negativo ou zero | 5, -3 e 0 | [`ex10-positivo-negativo-zero/`](ex10-positivo-negativo-zero/main.c) |
| 11 | Maior entre dois números, considerando igualdade | 8 e 3, 3 e 8, 4 e 4 | [`ex11-maior-ou-menor/`](ex11-maior-ou-menor/main.c) |
| 12 | Maior de idade | 17, 18 e 19 | [`ex12-maioridade/`](ex12-maioridade/main.c) |
| 13 | Situação por faixas de nota | 4, 6 e 8 — uma por faixa | [`ex13-faixas-de-nota/`](ex13-faixas-de-nota/main.c) |
| 14 | Aprovação: nota >= 6 **E** frequência >= 75 | 7/80, 7/50, 5/80, 5/50 | [`ex14-aprovacao/`](ex14-aprovacao/main.c) |
| 15 | Desconto: VIP **OU** compra >= 100 | 150/S, 150/N, 50/S, 50/N | [`ex15-desconto/`](ex15-desconto/main.c) |
| 16 | Acesso: login **E** senha **E NÃO** bloqueado | as 8 combinações | [`ex16-login/`](ex16-login/main.c) |

---

## Como rodar

### No VS Code

Com o `.c` aberto:

- **Ctrl+Shift+B** — compila o arquivo atual (gcc com `-Wall -Wextra -Wpedantic -g`).
- **Ctrl+Alt+N** — compila **e roda** no terminal integrado (Code Runner).
  É o caminho mais curto pra testar; o `scanf` recebe o teclado normalmente.
- **Ctrl+Shift+P → Run Test Task** — mesma coisa, sem depender do Code Runner.
- **F5** — debug com gdb (breakpoint na margem, F10 passo a passo).

### No terminal

```bash
cd exercicios_em_C

make run EX=ex01     # compila e roda (basta o prefixo)
make                 # compila todos
make list            # lista os exercicios
make clean           # apaga os binarios
```

---

## Diferenças de C que pegam nesses exercícios

Vindo do Python/Go, estes são os pontos onde o C muda o jogo:

**1. Toda variável precisa de tipo declarado e o `scanf` precisa do `&`.**

```c
float a;
scanf("%f", &a);   // sem o & o programa quebra em runtime
```

Formatos: `%d` int, `%f` float, `%lf` double, `%c` char, `%s` string.
No `printf`, `float` e `double` usam os dois `%f` — a promoção é automática.

**2. Divisão entre inteiros trunca.**

`7 / 2` dá `3`, não `3.5`. Nos exercícios de média (3, 9) e conversão (6),
declare as variáveis como `float`/`double`, ou force a conversão: `(float)soma / 3`.

**3. Não existe tipo string.** É um array de `char`:

```c
char nome[50];
scanf("%49s", nome);   // sem &, e para no primeiro espaço
fgets(nome, sizeof nome, stdin);   // le a linha inteira, inclui o '\n'
```

Para comparar (ex. 16) **não use `==`** — isso compara endereços. Use
`strcmp(a, b) == 0`, com `#include <string.h>`.

**4. Não existe booleano nativo até o C23.** Para os exercícios 15 e 16,
ou lê um `char` `'S'`/`'N'`, ou usa `#include <stdbool.h>` e `bool`.

**5. Misturar `scanf("%d")` com leitura de texto deixa o `\n` no buffer.**
Se o `fgets` depois de um `scanf` parecer "pulado", é isso. Consuma a sobra:

```c
scanf("%d", &n);
while (getchar() != '\n') { }   // limpa o resto da linha
```

**6. Decimal é ponto, não vírgula.** O `scanf` roda no locale `C` por padrão,
então digite `3.5` — `3,5` vai ler só o `3`.
