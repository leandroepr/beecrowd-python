import re
from typing import Dict, List


class InvalidMarkdownFormatError(Exception):
    """Exception for errors in Markdown format."""


class SampleExtractor:
    HEADER_PATTERN = r"^\|\s*Input Sample\s*\|\s*Output Sample\s*\|$"

    def __init__(self, content: str):
        self.content = content

    def _find_table(self) -> List[str]:
        """
        Identifies the table in the Markdown text.

        Returns:
            List[str]: Table lines (including header and separator).
        """
        lines = self.content.splitlines()
        table_lines = []
        inside_table = False

        for line in lines:
            # Checks if the line is the table header
            if re.match(self.HEADER_PATTERN, line.strip()):
                inside_table = True
                table_lines.append(line.strip())
                continue

            # If we are inside the table, accumulate lines that start with a pipe
            if inside_table:
                if line.strip().startswith("|"):
                    table_lines.append(line.strip())
                else:
                    break  # Line is not part of the table, stop accumulating

        # Validates if a table was found
        if not table_lines:
            raise InvalidMarkdownFormatError("Table not found in the Markdown file.")

        return table_lines

    def _process_table(self, table_lines: List[str]) -> List[Dict[str, str]]:
        """
        Processes the table lines to extract the samples.

        Args:
            table_lines (List[str]): Table lines.

        Returns:
            List[Dict[str, str]]: List of samples with `input` and `output`.
        """
        # Ignore header and separator
        data_lines = table_lines[2:]
        samples = []

        for line in data_lines:
            # Split values between pipes
            columns = [col.strip() for col in line.split("|")[1:-1]]
            if len(columns) == 2:
                input_data, output_data = columns
                samples.append(
                    {
                        "input": input_data.replace("<br>", "\n"),
                        "output": output_data.replace("<br>", "\n"),
                    }
                )

        return samples

    def extract_samples(self) -> List[Dict[str, str]]:
        """
        Extracts the samples from the table in the Markdown.

        Returns:
            List[Dict[str, str]]: List of samples with `input` and `output`.
        """
        table_lines = self._find_table()
        samples = self._process_table(table_lines)
        return samples
