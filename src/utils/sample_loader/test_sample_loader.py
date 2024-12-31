from pathlib import Path

import pytest

from .sample_loader import SampleLoader


@pytest.fixture
def create_temp_markdown():
    """
    Fixture para criar e limpar arquivos temporários Markdown.
    """
    temp_files = []

    def _create_temp_markdown(file_name: str, content: str) -> Path:
        temp_path = Path(file_name)
        temp_path.write_text(content)
        temp_files.append(temp_path)
        return temp_path

    yield _create_temp_markdown

    # Cleanup: Remove todos os arquivos criados após o teste
    for temp_file in temp_files:
        temp_file.unlink()


def test_sample_loader_hello_world(create_temp_markdown):
    markdown_content = """
    | Input Sample | Output Sample |
    | ------------ | ------------- |
    |              | Hello World!  |
    """
    temp_markdown = create_temp_markdown(
        "temp_challenge_hello_world.md", markdown_content
    )
    loader = SampleLoader(temp_markdown)
    samples = loader.extract_samples()
    assert samples == [{"input": "", "output": "Hello World!"}]


def test_sample_loader(create_temp_markdown):
    markdown_content = """
    | Input Sample | Output Sample |
    | ------------ | ------------- |
    | 10<br>9      | X = 19        |
    | -10<br>4     | X = -6        |
    | 15<br>-7     | X = 8         |
    """
    temp_markdown = create_temp_markdown("temp_challenge.md", markdown_content)
    loader = SampleLoader(temp_markdown)
    samples = loader.extract_samples()
    assert samples == [
        {"input": "10\n9", "output": "X = 19"},
        {"input": "-10\n4", "output": "X = -6"},
        {"input": "15\n-7", "output": "X = 8"},
    ]
