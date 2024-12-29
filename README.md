# Beecrowd Solutions in Python

Este repositório contém soluções para os desafios do Beecrowd, organizadas por categorias e problemas individuais. O projeto segue boas práticas de estruturação e automação para facilitar a manutenção e consulta das soluções.

## Configuração do ambiente

**Requisitos:** Certifique-se de ter o Python 3.9 instalado em seu sistema.

1. Clone o repositório:

    ```bash
    git clone https://github.com/leandroepr/beecrowd-python.git
    cd beecrowd-python
    ```

2. Certifique-se de ter o [Poetry](https://python-poetry.org/) instalado:

    ```bash
    pip install --user poetry
    ```

3. Instale as dependências:

    ```bash
    poetry install
    ```

4. Ative o ambiente virtual:

    ```bash
    poetry shell
    ```

## Estrutura inicial do projeto

```
beecrowd_python/
├── docs/
├── src/
│   ├── challenges/
│   └── utils/
├── pyproject.toml
├── .gitignore
└── README.md
```

## Objetivo

-   Consolidar as soluções do Beecrowd em um único repositório organizado.
-   Demonstrar boas práticas de programação, incluindo TDD e automação de testes.
