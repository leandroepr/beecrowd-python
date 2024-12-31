# src/utils/sample_loader/test_sample_loader.py
from pathlib import Path

from .sample_loader import SampleLoader


def test_sample_loader_hello_world():
    markdown_content = """
    | Input Sample | Output Sample |
    | ------------ | ------------- |
    |              | Hello World!  |
    """

    temp_markdown = Path("temp_challenge_hello_world.md")
    temp_markdown.write_text(markdown_content)

    loader = SampleLoader(temp_markdown)
    samples = loader.extract_samples()

    assert samples == [
        {"input": "", "output": "Hello World!"},
    ]

    temp_markdown.unlink()  # Cleanup after the test


def test_sample_loader():
    markdown_content = """
    | Input Sample | Output Sample |
    | ------------ | ------------- |
    | 10<br>9      | X = 19        |
    | -10<br>4     | X = -6        |
    | 15<br>-7     | X = 8         |
    """

    temp_markdown = Path("temp_challenge.md")
    temp_markdown.write_text(markdown_content)

    loader = SampleLoader(temp_markdown)
    samples = loader.extract_samples()

    assert samples == [
        {"input": "10\n9", "output": "X = 19"},
        {"input": "-10\n4", "output": "X = -6"},
        {"input": "15\n-7", "output": "X = 8"},
    ]

    temp_markdown.unlink()  # Cleanup after the test
