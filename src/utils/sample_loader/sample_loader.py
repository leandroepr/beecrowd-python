from pathlib import Path
from typing import Dict, List


class SampleLoader:
    def __init__(self, markdown_path: Path):
        """
        Inicializa o SampleLoader.

        Args:
            markdown_path (Path): Caminho para o arquivo Markdown.
        """
        self.markdown_path = Path(markdown_path)
        if not self.markdown_path.exists():
            raise FileNotFoundError(
                f"Arquivo Markdown não encontrado: {self.markdown_path}"
            )

    def extract_samples(self) -> List[Dict[str, str]]:
        """
        Extrai samples do arquivo Markdown.

        Returns:
            List[Dict[str, str]]: Lista de samples com 'input' e 'output'.
        """
        content = self.markdown_path.read_text()
        parser = MarkdownParser(content)
        return parser.parse()


class MarkdownParser:
    HEADER_ROW = ["Input Sample", "Output Sample"]

    def __init__(self, content: str):
        self.content = content

    def _validate_header(self, rows: List[str]) -> None:
        if not rows or self.HEADER_ROW != [
            col.strip() for col in rows[0].split("|")[1:-1]
        ]:
            raise InvalidMarkdownFormatError(
                "O arquivo Markdown não possui cabeçalhos válidos."
            )

    def parse(self) -> List[Dict[str, str]]:
        rows = self.content.strip().split("\n")
        self._validate_header(rows)

        # Processa linhas do corpo, ignorando cabeçalhos e separadores
        data_rows = rows[2:]  # Ignora cabeçalhos e separadores
        samples = []

        for row in data_rows:
            columns = [col.strip() for col in row.split("|")[1:-1]]
            if len(columns) == 2:
                input_data, output_data = columns
                samples.append(
                    {
                        "input": "\n".join(input_data.split("<br>")).strip(),
                        "output": "\n".join(output_data.split("<br>")).strip(),
                    }
                )

        return samples


class SampleLoaderError(Exception):
    """Exceção base para erros no SampleLoader."""

    pass


class InvalidMarkdownFormatError(SampleLoaderError):
    """Exceção para erros de formato no arquivo Markdown."""

    pass
