import pytest

from src.utils.sample_extractor import InvalidMarkdownFormatError, SampleExtractor


def test_valid_markdown_with_table():
    markdown_content = """
    Some irrelevant content.

    | Input Sample | Output Sample |
    | ------------ | ------------- |
    | 1            | 2             |
    | 3            | 4             |

    Some other irrelevant content.
    """
    extractor = SampleExtractor(markdown_content)
    samples = extractor.extract_samples()

    assert samples == [
        {"input": "1", "output": "2"},
        {"input": "3", "output": "4"},
    ]


def test_markdown_with_multiline_input_output():
    markdown_content = """
    |  Input Sample  |   Output Sample    |
    | -------------- | ------------------ |
    | Line1<br>Line2 | Result1<br>Result2 |
    """
    extractor = SampleExtractor(markdown_content)
    samples = extractor.extract_samples()

    assert samples == [
        {"input": "Line1\nLine2", "output": "Result1\nResult2"},
    ]


def test_markdown_with_extra_rows():
    markdown_content = """
    | Input Sample | Output Sample |
    | ------------ | ------------- |
    | 1            | 2             |
    | 3            | 4             |
    Extra row that should be ignored.
    """
    extractor = SampleExtractor(markdown_content)
    samples = extractor.extract_samples()

    # Verifica que a linha extra é ignorada
    assert samples == [
        {"input": "1", "output": "2"},
        {"input": "3", "output": "4"},
    ]


def test_markdown_without_table():
    markdown_content = """
    This markdown does not contain any table.
    """
    extractor = SampleExtractor(markdown_content)

    with pytest.raises(
        InvalidMarkdownFormatError, match="Table not found in the Markdown file."
    ):
        extractor.extract_samples()
