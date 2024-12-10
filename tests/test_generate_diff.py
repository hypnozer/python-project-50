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

# Тест для двух одинаковых файлов
# Два файла json
def test_generate_diff_same_files_json():
    result = generate_diff("tests/fixtures/file1.json",
                           "tests/fixtures/file1.json")
    assert result == """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""


# Один файл json, другой yml
def test_generate_diff_same_files_json_yml():
    result = generate_diff("tests/fixtures/file1.json",
                           "tests/fixtures/file1.yml")
    assert result == """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""


# Один файл json, другой yAml
def test_generate_diff_same_files_json_yaml():
    result = generate_diff("tests/fixtures/file1.json",
                           "tests/fixtures/file1.yaml")
    assert result == """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""


# Два файла yml
def test_generate_diff_same_files_yml_yml():
    result = generate_diff("tests/fixtures/file1.yml",
                           "tests/fixtures/file1.yml")
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


# Ожидаемый результат для сравнения пустого файла с file2.json
def test_generate_diff_one_empty_file():
    expected_output = """{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}"""
    result = generate_diff("tests/fixtures/empty.json",
                           "tests/fixtures/file2.json")
    assert result == expected_output


# Ожидаемый результат для сравнения пустого файла yml с file2.json
def test_generate_diff_one_empty_file_yml():
    expected_output = """{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}"""
    result = generate_diff("tests/fixtures/empty.yml",
                           "tests/fixtures/file2.json")
    assert result == expected_output
