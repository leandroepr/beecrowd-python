from pathlib import Path

import pytest

from src.utils.file_reader import FileReader
from src.utils.sample_extractor import SampleExtractor
from src.utils.solution_runner import SolutionRunner


@pytest.fixture
def setup_challenge_1000():
    markdown_path = Path("src/challenges/challenge_1000_hello_world/CHALLENGE.md")
    markdown_content = FileReader(markdown_path).read()
    extractor = SampleExtractor(markdown_content)
    samples = extractor.extract_samples()

    solution_path = Path("src/challenges/challenge_1000_hello_world/solution.py")
    solution_code = FileReader(solution_path).read()
    solution = SolutionRunner(solution_code)

    return solution, samples


def test_sample_1(setup_challenge_1000):
    runner, samples = setup_challenge_1000
    sample = samples[0]

    result = runner.run(sample["input"])
    assert result == sample["output"]
