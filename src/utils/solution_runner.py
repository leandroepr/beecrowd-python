import subprocess
import tempfile


class SolutionRunner:
    def __init__(self, solution_code: str):
        """
        Initializes the SolutionRunner.

        Args:
            solution_code (str): Python code of the solution.
        """
        self.solution_code = solution_code

    def run(self, input_data: str) -> str:
        """
        Executes the Python code with the provided input data.

        Args:
            input_data (str): Input data for the program.

        Returns:
            str: Program output.

        Raises:
            RuntimeError: If there is an error during program execution.
        """
        # Creates a temporary file with the solution code
        with tempfile.NamedTemporaryFile(
            suffix=".py", mode="w", delete=True
        ) as temp_file:
            temp_file.write(self.solution_code)
            temp_file.flush()

            # Executes the code in a subprocess
            process = subprocess.run(
                ["python3", temp_file.name],
                input=input_data,  # Pass as string directly
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,  # Ensure text mode is enabled
            )

        if process.returncode != 0:
            raise RuntimeError(
                f"Error during program execution: {process.stderr.strip()}"
            )

        return process.stdout.strip()
