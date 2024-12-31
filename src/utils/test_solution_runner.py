from textwrap import dedent

from src.utils.solution_runner import SolutionRunner


def test_solution_runner_without_arguments():
    solution_code = """print("Hello World!")"""
    runner = SolutionRunner(solution_code)

    assert runner.run("") == "Hello World!"


def test_solution_runner_multiplication():
    solution_code = dedent(
        """
        n1 = int(input())
        n2 = int(input())
        print(f"{n1} * {n2} = {n1 * n2}")
        """
    )
    runner = SolutionRunner(solution_code)

    # Teste com dois números como entrada
    assert runner.run("2\n2") == "2 * 2 = 4"
    assert runner.run("3\n5") == "3 * 5 = 15"
    assert runner.run("-2\n6") == "-2 * 6 = -12"


def test_solution_runner_error_code():
    solution_code = """raise Exception("Error!")"""
    runner = SolutionRunner(solution_code)

    try:
        runner.run("")
    except RuntimeError as e:
        assert "Error during program execution:" in str(e)
        assert "Exception: Error!" in str(e)
