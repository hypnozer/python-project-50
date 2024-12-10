import json
from gendiff.modules.build_diff import build_diff
from gendiff.modules.parse_file_formats import load_file


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
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


# Проверяем два стандартных файла в разных сочетаниях форматов
def test_build_diff_two_json():
    original_file = load_file("tests/fixtures/file1.json")
    changed_file = load_file("tests/fixtures/file2.json")

    result = build_diff(original_file, changed_file)
    assert result == EXPECTED_OUTPUT

def test_build_diff_two_yml():
    original_file = load_file("tests/fixtures/file1.yml")
    changed_file = load_file("tests/fixtures/file2.yml")

    result = build_diff(original_file, changed_file)
    assert result == EXPECTED_OUTPUT


def test_build_diff_two_yaml():
    original_file = load_file("tests/fixtures/file1.yaml")
    changed_file = load_file("tests/fixtures/file2.yaml")

    result = build_diff(original_file, changed_file)
    assert result == EXPECTED_OUTPUT


def test_build_diff_json_yml():
    original_file = load_file("tests/fixtures/file1.json")
    changed_file = load_file("tests/fixtures/file2.yml")

    result = build_diff(original_file, changed_file)
    assert result == EXPECTED_OUTPUT


def test_build_diff_yml_json():
    original_file = load_file("tests/fixtures/file1.yml")
    changed_file = load_file("tests/fixtures/file2.json")

    result = build_diff(original_file, changed_file)
    assert result == EXPECTED_OUTPUT

# Проверяем два одинаковых файла
def test_build_diff_no_changes():
    original_file = load_file("tests/fixtures/file1.json")

    changed_file = load_file("tests/fixtures/file1.json")

    expected_output = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    result = build_diff(original_file, changed_file)
    assert result == expected_output


# Проверяем с измененным файлом (данные добавлены)
def test_build_diff_only_added():
    original_file = load_file("tests/fixtures/empty.json")
    changed_file = load_file("tests/fixtures/only_added1.json")

    expected_output = """{
  + host: hexlet.io
  + timeout: 50
}"""

    result = build_diff(original_file, changed_file)
    assert result == expected_output


# Проверяем с измененным (пустым) файлом (данные удалены)
def test_build_diff_only_deleted():
    original_file = load_file("tests/fixtures/only_added1.json")
    changed_file = load_file("tests/fixtures/empty.json")

    expected_output = """{
  - host: hexlet.io
  - timeout: 50
}"""

    result = build_diff(original_file, changed_file)
    assert result == expected_output


# Проверяем с измененным файлом (часть данных удалена, часть добавлена)
def test_build_diff_changed_and_added():
    original_file = load_file("tests/fixtures/only_added1.json")
    changed_file = load_file("tests/fixtures/file1.json")

    expected_output = """{
  + follow: false
    host: hexlet.io
  + proxy: 123.234.53.22
    timeout: 50
}"""

    result = build_diff(original_file, changed_file)
    assert result == expected_output
