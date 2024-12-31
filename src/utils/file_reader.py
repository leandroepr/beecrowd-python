from pathlib import Path


class FileReader:
    def __init__(self, file_path: str | Path):
        self.file_path = Path(file_path)

    def read(self) -> str:
        """
        Reads the content of the file.

        Returns:
            str: Content of the file.

        Raises:
            FileNotFoundError: If the file is not found.
            IOError: If the file cannot be read.
        """
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        try:
            return self.file_path.read_text()
        except Exception as e:
            raise IOError(f"Error reading the file: {e}")
