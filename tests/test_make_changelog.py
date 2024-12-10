from gendiff.modules.make_changelog import make_changelog


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
        {"key": "host", "type": "unchanged"},
        {"key": "timeout", "type": "unchanged"},
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
        {"key": "host", "type": "unchanged"},
        {"key": "timeout", "type": "changed"},
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
        {"key": "host", "type": "unchanged"},
        {"key": "timeout", "type": "added"},
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
        {"key": "host", "type": "unchanged"},
        {"key": "timeout", "type": "deleted"},
    ]
    result = make_changelog(original_file, changed_file)
    assert result == expected_output


def test_make_changelog_mixed_changes():
    original_file = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
    }

    changed_file = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io",
    }

    expected_output = [
        {"key": "host", "type": "unchanged"},
        {"key": "proxy", "type": "deleted"},
        {"key": "timeout", "type": "changed"},
        {"key": "verbose", "type": "added"},
    ]
    result = make_changelog(original_file, changed_file)
    assert result == expected_output
