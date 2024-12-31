import pytest

from src.utils.file_reader import FileReader


def test_file_reader_valid_file(tmp_path):
    temp_file = tmp_path / "test.txt"
    temp_file.write_text("Hello, World!")

    reader = FileReader(temp_file)
    assert reader.read() == "Hello, World!"


def test_file_reader_file_not_found():
    reader = FileReader("non_existent_file.txt")

    with pytest.raises(FileNotFoundError):
        reader.read()


def test_file_reader_io_error(mocker, tmp_path):
    temp_file = tmp_path / "test.txt"
    temp_file.write_text("Hello, World!")

    mocker.patch("pathlib.Path.read_text", side_effect=Exception("Read error"))

    reader = FileReader(temp_file)
    with pytest.raises(IOError):
        reader.read()
