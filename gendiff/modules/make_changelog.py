def make_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)


def make_changelog(original_file, changed_file, level=0):
    """
    Функция создает список изменений (changelog), сравнивая два словаря с учетом вложенности.
    """
    changelog = []
    all_keys = sorted(set(original_file.keys()).union(changed_file.keys()))

    for key in all_keys:
        if key in original_file and key in changed_file:
            if isinstance(original_file[key], dict) and isinstance(changed_file[key], dict):
                # Process nested dictionaries recursively
                changelog.append(
                    {
                        "key": key,
                        "type": "unchanged",
                        "level": level,
                        "original_value": original_file[key],
                        "changed_value": changed_file[key],
                    }
                )
                changelog.extend(
                    make_changelog(
                        original_file[key],
                        changed_file[key],
                        level + 1
                    )
                )
            else:
                change_type = (
                    "unchanged" if original_file[key] == changed_file[key] else "changed"
                )
                changelog.append(
                    {
                        "key": key,
                        "type": change_type,
                        "level": level,
                        "original_value": original_file.get(key),
                        "changed_value": changed_file.get(key),
                    }
                )
        elif key in original_file:
            # Deleted key
            changelog.append(
                {
                    "key": key,
                    "type": "deleted",
                    "level": level,
                    "original_value": original_file.get(key),
                    "changed_value": None,
                }
            )
        elif key in changed_file:
            # Added key
            changelog.append(
                {
                    "key": key,
                    "type": "added",
                    "level": level,
                    "original_value": None,
                    "changed_value": changed_file.get(key),
                }
            )

    return changelog


# удалить
import yaml
import json


def load_file(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(file) or {}
        else:
            raise ValueError(f"Unsupported file format: {file_path}")

original_file1 = load_file('tests/fixtures/file1_nested.json')


changed_file1 = load_file('tests/fixtures/file2_nested.json')


print(make_changelog(original_file1, changed_file1))


def make_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        return format_to_string(value, level=1)
    return str(value)

def format_to_string(data, level=0):
    indent = ' ' * (level * 4)
    nested_indent = ' ' * ((level + 1) * 4)
    lines = ['{']

    for key, value in data.items():
        if isinstance(value, dict):
            nested = format_to_string(value, level + 1)
            lines.append(f"{nested_indent}{key}: {nested}")
        else:
            lines.append(f"{nested_indent}{key}: {value}")

    lines.append(f"{indent}}}")
    return "\n".join(lines)

def format_changelog(changelog):
    def generate_line(change):
        symbol_map = {
            'added': '+',
            'deleted': '-',
            'changed': None,
            'unchanged': ' '
        }

        key = change['key']
        change_type = change['type']
        level = change['level']
        original_value = make_string(change['original_value'])
        changed_value = make_string(change['changed_value'])

        indent = ' ' * (level * 4)
        if change_type == 'changed':
            return [
                f"{indent}- {key}: {original_value}",
                f"{indent}+ {key}: {changed_value}"
            ]
        elif change_type in symbol_map:
            symbol = symbol_map[change_type]
            value = original_value if change_type == 'deleted' else changed_value
            return [f"{indent}{symbol} {key}: {value}"]
        return [f"{indent}{key}: {original_value}"]

    result = ['{']
    for change in changelog:
        if change['type'] == 'unchanged' and isinstance(change['original_value'], dict):
            # Handle nested unchanged structures
            nested = format_to_string(change['original_value'], change['level'] + 1)
            result.append(f"{' ' * (change['level'] * 4)}{change['key']}: {nested}")
        else:
            result.extend(generate_line(change))
    result.append('}')
    return "\n".join(result)



print(format_changelog(make_changelog(original_file1, changed_file1)))


