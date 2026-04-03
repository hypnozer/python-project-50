import json
import os

import pytest

from gendiff import generate_diff

BASE_DIR = os.path.dirname(__file__)
TEST_DATA_PATH = os.path.join(BASE_DIR, "test_data", "json")


def read_fixture(filename):
    path = os.path.join(TEST_DATA_PATH, filename)
    with open(path, encoding="utf-8") as file:
        return file.read()


@pytest.mark.parametrize("extension", ["json", "yml", "yaml"])
def test_generate_diff_json(extension):
    file1 = os.path.join(TEST_DATA_PATH, f"file1.{extension}")
    file2 = os.path.join(TEST_DATA_PATH, f"file2.{extension}")
    expected = read_fixture("expected_json.txt")

    result = generate_diff(file1, file2, "json")

    assert json.loads(result) == json.loads(expected)
