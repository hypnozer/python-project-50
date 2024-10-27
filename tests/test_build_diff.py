import json
from gendiff.modules.build_diff import build_diff


# Определяем TYPES_OF_CHANGES в тестах
TYPES_OF_CHANGES = {
    "unchanged": "  ",
    "changed_old": "- ",
    "changed_new": "+ ",
    "deleted": "- ",
    "added": "+ ",
}

# Ожидаемый результат
EXPECTED_OUTPUT = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""


def test_build_diff():
    original_file = json.load(open("tests/fixtures/file1.json"))
    changed_file = json.load(open("tests/fixtures/file2.json"))

    result = build_diff(original_file, changed_file)
    assert result == EXPECTED_OUTPUT


def test_build_diff_no_changes():
    original_file = json.load(open("tests/fixtures/file1.json"))

    changed_file = json.load(open("tests/fixtures/file1.json"))

    expected_output = """{
    follow: False
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    result = build_diff(original_file, changed_file)
    assert result == expected_output


def test_build_diff_only_added():
    original_file = json.load(open("tests/fixtures/empty.json"))
    changed_file = json.load(open("tests/fixtures/only_added1.json"))

    expected_output = """{
  + host: hexlet.io
  + timeout: 50
}"""

    result = build_diff(original_file, changed_file)
    assert result == expected_output


def test_build_diff_only_deleted():
    original_file = json.load(open("tests/fixtures/only_added1.json"))
    changed_file = json.load(open("tests/fixtures/empty.json"))

    expected_output = """{
  - host: hexlet.io
  - timeout: 50
}"""

    result = build_diff(original_file, changed_file)
    assert result == expected_output


def test_build_diff_changed_and_added():
    original_file = json.load(open("tests/fixtures/only_added1.json"))
    changed_file = json.load(open("tests/fixtures/file1.json"))

    expected_output = """{
  + follow: False
    host: hexlet.io
  + proxy: 123.234.53.22
    timeout: 50
}"""

    result = build_diff(original_file, changed_file)
    assert result == expected_output
