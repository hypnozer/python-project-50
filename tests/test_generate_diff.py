from gendiff.modules.generate_diff import generate_diff

# Ожидаемый результат для сравнения file1.json и file2.json
EXPECTED_DIFF = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


def test_generate_diff_same_files():
    # Тест для двух одинаковых файлов
    result = generate_diff("tests/fixtures/file1.json",
                           "tests/fixtures/file1.json")
    assert result == """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""


def test_generate_diff_different_files():
    # Тест для разных файлов (file1.json и file2.json)
    result = generate_diff("tests/fixtures/file1.json",
                           "tests/fixtures/file2.json")
    assert result == EXPECTED_DIFF


def test_generate_diff_one_empty_file():
    # Ожидаемый результат для сравнения пустого файла с file2.json
    expected_output = """{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}"""
    result = generate_diff("tests/fixtures/empty.json",
                           "tests/fixtures/file2.json")
    assert result == expected_output
