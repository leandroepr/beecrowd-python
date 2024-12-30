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
│       └── solution_runner/
├── pyproject.toml
├── .gitignore
└── README.md
```

## Objetivo

-   Consolidar as soluções do Beecrowd em um único repositório organizado.
-   Demonstrar boas práticas de programação, incluindo TDD e automação de testes.

## Utilitários

### Solution Runner

O `SolutionRunner` é um utilitário que executa soluções Python em um ambiente isolado, fornecendo entradas e capturando saídas. É utilizado para garantir que cada solução funcione corretamente com diferentes casos de teste.

#### Exemplo de Uso

```python
from src.utils.solution_runner import SolutionRunner

runner = SolutionRunner("path_to_solution.py")

# Executa a solução com entrada fornecida
output = runner.run("5\n10\n")
print(output)  # Exibe a saída gerada pela solução
```

#### Testes

Testes automatizados garantem a funcionalidade do `SolutionRunner`. Para executá-los:

```bash
pytest src/utils/solution_runner/test_solution_runner.py
```
