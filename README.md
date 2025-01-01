# Beecrowd Solutions in Python

Este repositório contém soluções para os desafios do Beecrowd, organizadas por categorias e problemas individuais. O projeto segue boas práticas de estruturação e automação para facilitar a manutenção e consulta das soluções.

## Configuração do ambiente

**Requisitos:** Certifique-se de ter o Python 3.11 instalado em seu sistema.

1. Clone o repositório:

    ```bash
    git clone https://github.com/leandroepr/beecrowd-python.git
    cd beecrowd-python
    ```

2. Instale as dependências utilizando o `Makefile`:

    ```bash
    make install
    ```

### Tabelas de Navegação

-   [Lista Geral de Problemas Resolvidos](docs/all_problems.md)
-   Listas por Categoria:
    -   [Beginner](docs/beginner.md)
    -   [Ad-Hoc](docs/ad_hoc.md)
    -   [Strings](docs/strings.md)
    -   [Data Structures and Libraries](docs/data_structures_and_libraries.md)
    -   [Mathematics](docs/mathematics.md)
    -   [Paradigms](docs/paradigms.md)
    -   [Graph](docs/graph.md)
    -   [Computational Geometry](docs/computational_geometry.md)
    -   [SQL](docs/sql.md)

## Estrutura inicial do projeto

```
beecrowd_python/
├── docs/
├── src/
│   ├── challenges/
│   │   └── challenge_1000_hello_world
│   │       ├── CHALLENGE.md
│   │       ├── solution.py
│   │       └── test_solution.py
│   └── utils/
│       ├── file_reader.py
│       ├── sample_extractor.py
│       ├── solution_runner.py
│       └── ... (tests)
├── Makefile
├── pyproject.toml
├── .gitignore
└── README.md
```

## Objetivo

-   Consolidar as soluções do Beecrowd em um único repositório organizado.
-   Demonstrar boas práticas de programação, incluindo TDD e automação de testes.

## Utilitários

### Solution Runner

O `SolutionRunner` é um utilitário que permite executar soluções Python fornecendo o conteúdo do código diretamente como string. Ele cria um ambiente isolado para executar o código com entradas simuladas e captura as saídas, permitindo validar e testar soluções de forma prática.

#### Exemplo de Uso

```python
from src.utils.solution_runner import SolutionRunner

solution_code = """print(f\"You said: {input()}\")"""

runner = SolutionRunner(solution_code)

# Executa a solução com entrada fornecida
output = runner.run("Hello World!\n")
print(output)  # Exibe: You said: Hello World!
```

### Sample Extractor

O `SampleExtractor` é um utilitário que processa arquivos Markdown para extrair exemplos de entrada e saída organizados em tabelas. Isso facilita a criação de testes automatizados para as soluções.

#### Exemplo de Uso

```python
from src.utils.sample_extractor import SampleExtractor

markdown_content = """
| Input Sample | Output Sample |
| ------------ | ------------- |
| 5            | 10            |
| 7            | 14            |
"""

extractor = SampleExtractor(markdown_content)
samples = extractor.extract_samples()
print(samples)
# Saída esperada:
# [{'input': '5', 'output': '10'}, {'input': '7', 'output': '14'}]
```

### File Reader

O `FileReader` é um utilitário que abstrai a leitura de arquivos, garantindo um tratamento adequado para casos de arquivo não encontrado ou erros de leitura.

#### Exemplo de Uso

```python
from src.utils.file_reader import FileReader

file_path = "path/to/file.txt"
reader = FileReader()

try:
    content = reader.read(file_path)
    print(content)
except FileNotFoundError:
    print("Arquivo não encontrado.")
except IOError:
    print("Erro ao ler o arquivo.")
```

### Testes Automatizados

Testes garantem que os utilitários e soluções funcionem corretamente. Para rodar todos os testes:

```bash
make test
```

Para assistir as alterações e rodar os testes automaticamente:

```bash
make test-watch
```

Para rodar apenas testes filtrados por um padrão:

```bash
make test FILTER=1000
```

## Linting e Formatação

-   Para verificar problemas de estilo de código:

    ```bash
    make lint
    ```

-   Para corrigir automaticamente problemas de formatação:

    ```bash
    make format
    ```

## CI/CD

O repositório utiliza **GitHub Actions** para garantir que todos os testes sejam executados automaticamente em pull requests. Isso inclui:

-   Verificação de formatação e estilo.
-   Execução de todos os testes automatizados.

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Fork o repositório.
2. Crie uma branch para sua contribuição:

    ```bash
    git checkout -b challenge-1000
    ```

3. Envie suas alterações:

    ```bash
    git push origin challenge-1000
    ```

4. Abra um pull request no GitHub.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
