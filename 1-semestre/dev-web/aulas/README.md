# Desenvolvimento Web I - FATEC Olímpia/SP

## Aluno: Renan Croffi

## Professor: Rodrigo Attique

Registros das aulas de desenvolvimento web I, do curso de DSM da FATEC de Olímpia.

## Aulas

| Aula | Tema | Pasta |
| --- | --- | --- |
| 1 | Introdução à Web | *(teórica, sem código)* |
| 2 | Primeiros passos com HTML | [`aula02-primeiro-site/`](aula02-primeiro-site/) |
| 3 | Semântica | [`aula03-semantica/`](aula03-semantica/) |
| 4 | Listas e Links | [`aula04-listas-links/`](aula04-listas-links/) |
| 5 | CSS | [`aula05-css/`](aula05-css/) |
| 5 | CSS — exercício feito em aula | [`aula05-exercicio/`](aula05-exercicio/) |
| 11 | Tabelas e estilização — exercício | [`exercicio_tabelas/`](exercicio_tabelas/tabelas_renan_croffi.html) |

A aula 5 foi o primeiro contato com CSS: em `aula05-css/` o estilo é aplicado
direto por seletor de elemento (`h1` e `nav`). Já o `aula05-exercicio/` é o
exercício proposto na mesma aula, com foco nos **tipos de seletor**: `*`,
elemento, `.classe`, `#id` e o seletor de filho `nav > ul`.

O `exercicio_tabelas/` (aula 11) monta uma tabela de sabores e preços com
`<table>`, `<tr>`, `<th>` e `<td>`, com uma imagem por linha e estilo em
`assets/css/style.css`. É a primeira página com o cabeçalho padrão pedido pelo
professor (comentário no topo com descrição, exercício, aluno e turma), e o
arquivo segue a convenção de nome da entrega: `tabelas_renan_croffi.html`.

## Estrutura

Cada aula é uma pasta com seu próprio `index.html`. Até a aula 4, o `styles.css`
ficava ao lado do HTML e as imagens compartilhadas em `assets/imagens/`. A partir
da aula 5 foi adotada a organização em `assets/css/` _dentro_ da pasta da aula,
que é a estrutura que o professor passou.

```
aulas/
├── assets/imagens/            # imagens compartilhadas (usadas pela aula 2)
├── aula02-primeiro-site/
│   └── index.html
├── aula03-semantica/
│   ├── index.html
│   └── styles.css
├── aula04-listas-links/
│   └── index.html
├── aula05-css/
│   ├── assets/css/styles.css
│   └── index.html
├── aula05-exercicio/
│   ├── assets/css/style.css
│   └── index.html
└── exercicio_tabelas/
    ├── assets/css/style.css
    ├── assets/img/            # fotos dos sabores
    └── tabelas_renan_croffi.html
```

Os caminhos de `href` e `src` devem ser **relativos** (`./assets/...`), para que a
página abra tanto pelo Live Server quanto por duplo clique no arquivo. Um caminho
começando com `/` procura a partir da raiz do servidor, não da pasta da aula, e
o arquivo não carrega.
