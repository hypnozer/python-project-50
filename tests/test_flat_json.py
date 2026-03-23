import json
import os

from gendiff import generate_diff

BASE_DIR = os.path.dirname(__file__)
FIXTURES_PATH = os.path.join(BASE_DIR, "fixtures", "flat")


def read_json(filename):
    path = os.path.join(FIXTURES_PATH, filename)
    with open(path) as f:
        return json.load(f)


def read_fixture(filename):
    path = os.path.join(FIXTURES_PATH, filename)
    with open(path) as f:
        return f.read()


def test_generate_diff_stylish():
    data1 = read_json("file1.json")
    data2 = read_json("file2.json")
    expected = read_fixture("expected_stylish.txt")

    result = generate_diff(data1, data2)

    assert result.strip() == expected.strip()
