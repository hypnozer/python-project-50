import json
from gendiff.modules.make_changelog import make_changelog
from gendiff.modules.format_changelog import format_changelog
from gendiff.modules.parse_file_formats import load_file


# Ожидаемые результаты
EXPECTED_OUTPUT = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

EXPECTED_OUTPUT_FOR_NESTED = """
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
"""


# Проверяем два стандартных файла в разных сочетаниях форматов
def test_format_changelog_two_json():
    original_file = load_file("tests/fixtures/file1.json")
    changed_file = load_file("tests/fixtures/file2.json")
    result = format_changelog(make_changelog(original_file, changed_file))
    print(result)
    assert result == EXPECTED_OUTPUT

def test_format_changelog_two_yml():
    original_file = load_file("tests/fixtures/file1.yml")
    changed_file = load_file("tests/fixtures/file2.yml")

    result = format_changelog(make_changelog(original_file, changed_file))
    assert result == EXPECTED_OUTPUT


def test_format_changelog_two_yaml():
    original_file = load_file("tests/fixtures/file1.yaml")
    changed_file = load_file("tests/fixtures/file2.yaml")

    result = format_changelog(make_changelog(original_file, changed_file))
    assert result == EXPECTED_OUTPUT


def test_format_changelog_json_yml():
    original_file = load_file("tests/fixtures/file1.json")
    changed_file = load_file("tests/fixtures/file2.yml")

    result = format_changelog(make_changelog(original_file, changed_file))
    assert result == EXPECTED_OUTPUT


def test_format_changelog_yml_json():
    original_file = load_file("tests/fixtures/file1.yml")
    changed_file = load_file("tests/fixtures/file2.json")

    result = format_changelog(make_changelog(original_file, changed_file))
    assert result == EXPECTED_OUTPUT

# Проверяем два одинаковых файла
def test_format_changelog_no_changes():
    original_file = load_file("tests/fixtures/file1.json")

    changed_file = load_file("tests/fixtures/file1.json")

    expected_output = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    result = format_changelog(make_changelog(original_file, changed_file))
    assert result == expected_output


# Проверяем с измененным файлом (данные добавлены)
def test_format_changelog_only_added():
    original_file = load_file("tests/fixtures/empty.json")
    changed_file = load_file("tests/fixtures/only_added1.json")

    expected_output = """{
  + host: hexlet.io
  + timeout: 50
}"""

    result = format_changelog(make_changelog(original_file, changed_file))
    assert result == expected_output


# Проверяем с измененным (пустым) файлом (данные удалены)
def test_format_changelog_only_deleted():
    original_file = load_file("tests/fixtures/only_added1.json")
    changed_file = load_file("tests/fixtures/empty.json")

    expected_output = """{
  - host: hexlet.io
  - timeout: 50
}"""

    result = format_changelog(make_changelog(original_file, changed_file))
    assert result == expected_output


# Проверяем с измененным файлом (часть данных удалена, часть добавлена)
def test_format_changelog_changed_and_added():
    original_file = load_file("tests/fixtures/only_added1.json")
    changed_file = load_file("tests/fixtures/file1.json")

    expected_output = """{
  + follow: false
    host: hexlet.io
  + proxy: 123.234.53.22
    timeout: 50
}"""

    result = format_changelog(make_changelog(original_file, changed_file))
    assert result == expected_output


# Проверяем с измененным файлом сложной структуры (формат json)
def test_format_changelog_changed_and_nested_json():
    original_file = load_file("tests/fixtures/file1_nested.json")
    changed_file = load_file("tests/fixtures/file2_nested.json")

    result = format_changelog(make_changelog(original_file, changed_file))
    assert result == EXPECTED_OUTPUT_FOR_NESTED


# Проверяем с измененным файлом сложной структуры (формат json и yml)
def test_format_changelog_changed_and_nested_json():
    original_file = load_file("tests/fixtures/file1_nested.json")
    changed_file = load_file("tests/fixtures/file2_nested.yml")
    result = format_changelog(make_changelog(original_file, changed_file))
    print(result)
    assert result == EXPECTED_OUTPUT_FOR_NESTED

# Проверяем идентичные файлы сложной структуры

# Повторно проверяем идентичные файлы сложной структуры
