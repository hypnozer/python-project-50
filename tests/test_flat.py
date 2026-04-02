import os
import pytest

from gendiff import generate_diff


BASE_DIR = os.path.dirname(__file__)
TEST_DATA_PATH = os.path.join(BASE_DIR, "test_data", "flat")


def read_fixture(filename):
    path = os.path.join(TEST_DATA_PATH, filename)
    with open(path, encoding="utf-8") as file:
        return file.read()


@pytest.mark.parametrize("extension", ["json", "yml"])
def test_generate_diff_stylish(extension):
    file1 = os.path.join(TEST_DATA_PATH, f"file1.{extension}")
    file2 = os.path.join(TEST_DATA_PATH, f"file2.{extension}")
    expected = read_fixture("expected_stylish.txt")

    result = generate_diff(file1, file2)

    assert result.strip() == expected.strip()
