from pathlib import Path

import pytest

from .solution_runner import SolutionRunner


@pytest.fixture
def solution_without_input():
    """
    Fixture to create a temporary solution that does not require input.

    Returns:
        Path: The path to the temporary solution file.
    """
    solution_code = """print(\"Hello World!\")"""
    temp_solution = Path("temp_solution_without_input.py")
    temp_solution.write_text(solution_code)
    yield temp_solution
    temp_solution.unlink()  # Cleanup after the test


@pytest.fixture
def solution_with_input():
    """
    Fixture to create a temporary solution that requires input.

    Returns:
        Path: The path to the temporary solution file.
    """
    solution_code = """n = int(input())\nprint(n * 2)"""
    temp_solution = Path("temp_solution_with_input.py")
    temp_solution.write_text(solution_code)
    yield temp_solution
    temp_solution.unlink()  # Cleanup after the test


def test_solution_runner_without_arguments(solution_without_input):
    runner = SolutionRunner(solution_without_input)

    # Test the output without input arguments
    assert runner.run("") == "Hello World!"


def test_solution_runner(solution_with_input):
    runner = SolutionRunner(solution_with_input)

    # Test the output for different inputs
    assert runner.run("5") == "10"
    assert runner.run("-3") == "-6"
