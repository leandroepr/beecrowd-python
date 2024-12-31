from pathlib import Path

import pytest

from .solution_runner import SolutionRunner


@pytest.fixture
def create_temp_solution():
    """
    Fixture para criar e limpar arquivos temporários de solução.
    """
    temp_files = []

    def _create_temp_solution(file_name: str, content: str) -> Path:
        temp_path = Path(file_name)
        temp_path.write_text(content)
        temp_files.append(temp_path)
        return temp_path

    yield _create_temp_solution

    # Cleanup: Remove todos os arquivos criados após o teste
    for temp_file in temp_files:
        temp_file.unlink()


def test_solution_runner_without_arguments(create_temp_solution):
    solution_code = """print("Hello World!")"""
    temp_solution = create_temp_solution(
        "temp_solution_without_input.py", solution_code
    )

    runner = SolutionRunner(temp_solution)

    # Test the output without input arguments
    assert runner.run("") == "Hello World!"


def test_solution_runner(create_temp_solution):
    solution_code = """n = int(input())\nprint(n * 2)"""
    temp_solution = create_temp_solution("temp_solution_with_input.py", solution_code)

    runner = SolutionRunner(temp_solution)

    # Test the output for different inputs
    assert runner.run("5") == "10"
    assert runner.run("-3") == "-6"
