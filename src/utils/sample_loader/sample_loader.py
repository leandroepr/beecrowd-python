import re
from pathlib import Path


class SampleLoader:
    def __init__(self, markdown_path):
        """
        Initializes the SampleLoader.

        Args:
            markdown_path (str or Path): Path to the Markdown file.
        """
        self.markdown_path = Path(markdown_path)
        if not self.markdown_path.exists():
            raise FileNotFoundError(f"Markdown file not found: {self.markdown_path}")

    def extract_samples(self):
        """
        Extracts samples from the Markdown file.

        Returns:
            list of dict: A list of samples in the format:
                [{"input": "input data", "output": "output data"}, ...]
        """
        content = self.markdown_path.read_text()

        # Match rows in the table
        rows = re.findall(r"\|\s*(.*?)\s*\|\s*(.*?)\s*\|", content)

        samples = []
        input_buffer = []
        output_buffer = []

        for i, (input_data, output_data) in enumerate(rows):
            # Skip the header row and separator rows
            if (
                i == 0
                or (
                    input_data.strip() == "Input Sample"
                    and output_data.strip() == "Output Sample"
                )
                or (
                    input_data.strip().startswith("-")
                    and output_data.strip().startswith("-")
                )
            ):
                continue

            # Handle multi-line input/output split by <br>
            input_lines = input_data.strip().split("<br>") if input_data.strip() else []
            output_lines = (
                output_data.strip().split("<br>") if output_data.strip() else []
            )

            # If there are both input and output lines, create a sample
            if input_lines or output_lines:
                input_buffer.extend(input_lines)
                output_buffer.extend(output_lines)

                # Append sample and reset buffers when transitioning to a new row
                if input_lines and output_lines:
                    samples.append(
                        {
                            "input": "\n".join(input_buffer).strip(),
                            "output": "\n".join(output_buffer).strip(),
                        }
                    )
                    input_buffer.clear()
                    output_buffer.clear()

        # Add any remaining data as the last sample
        if input_buffer or output_buffer:
            samples.append(
                {
                    "input": "\n".join(input_buffer).strip(),
                    "output": "\n".join(output_buffer).strip(),
                }
            )

        return samples
