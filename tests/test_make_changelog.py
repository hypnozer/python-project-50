from gendiff.modules.make_changelog import make_changelog
from gendiff.modules.parse_file_formats import load_file


def test_make_changelog_unchanged():
    original_file = {
        "host": "hexlet.io",
        "timeout": 50,
    }

    changed_file = {
        "host": "hexlet.io",
        "timeout": 50,
    }

    expected_output = [
        {"key": "host", "type": "unchanged", "level": 0, "parent_key": "",
        "original_value": "hexlet.io", "changed_value": "hexlet.io"},
        {"key": "timeout", "type": "unchanged", "level": 0, "parent_key": "",
        "original_value": 50, "changed_value": 50},
    ]
    result = make_changelog(original_file, changed_file)
    assert result == expected_output

def test_make_changelog_added():
    original_file = {
        "host": "hexlet.io",
    }

    changed_file = {
        "host": "hexlet.io",
        "timeout": 50,
    }

    expected_output = [
        {"key": "host", "type": "unchanged", "level": 0, "parent_key": "",
        "original_value": "hexlet.io", "changed_value": "hexlet.io"},
        {"key": "timeout", "type": "added", "level": 0, "parent_key": "",
        "original_value": None, "changed_value": 50},
    ]
    result = make_changelog(original_file, changed_file)
    assert result == expected_output

def test_make_changelog_deleted():
    original_file = {
        "host": "hexlet.io",
        "timeout": 50,
    }

    changed_file = {
        "host": "hexlet.io",
    }

    expected_output = [
        {"key": "host", "type": "unchanged", "level": 0, "parent_key": "",
        "original_value": "hexlet.io", "changed_value": "hexlet.io"},
        {"key": "timeout", "type": "deleted", "level": 0, "parent_key": "",
        "original_value": 50, "changed_value": None},
    ]
    result = make_changelog(original_file, changed_file)
    assert result == expected_output

def test_make_changelog_changed():
    original_file = {
        "host": "hexlet.io",
        "timeout": 50,
    }

    changed_file = {
        "host": "hexlet.io",
        "timeout": 20,
    }

    expected_output = [
        {"key": "host", "type": "unchanged", "level": 0, "parent_key": "",
        "original_value": "hexlet.io", "changed_value": "hexlet.io"},
        {"key": "timeout", "type": "changed", "level": 0, "parent_key": "",
        "original_value": 50, "changed_value": 20},
    ]
    result = make_changelog(original_file, changed_file)
    assert result == expected_output

def test_make_changelog_nested():
    original_file = {
        "host": "hexlet.io",
        "config": {
            "timeout": 50,
            "proxy": "123.234.53.22",
        }
    }

    changed_file = {
        "host": "hexlet.io",
        "config": {
            "timeout": 30,
            "verbose": True,
        }
    }

    expected_output = [
        {"key": "host", "type": "unchanged", "level": 0, "parent_key": "",
         "original_value": "hexlet.io", "changed_value": "hexlet.io"},
        {"key": "timeout", "type": "changed", "level": 1, "parent_key": "config",
         "original_value": 50, "changed_value": 30},
        {"key": "proxy", "type": "deleted", "level": 1, "parent_key": "config",
         "original_value": "123.234.53.22", "changed_value": None},
        {"key": "verbose", "type": "added", "level": 1, "parent_key": "config",
         "original_value": None, "changed_value": True},
    ]
    result = make_changelog(original_file, changed_file)
    assert result == expected_output
