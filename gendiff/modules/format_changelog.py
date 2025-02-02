from gendiff.modules.make_changelog import make_changelog

def make_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    return str(value)

def format_to_string(data, level=0, shift=4, left_shift=2):
    lines = []
    indent = ' ' * (level * shift)

    if isinstance(data, dict):
        lines.append(f"{indent}{{")
        for key, value in data.items():
            if isinstance(value, dict):
                nested = format_to_string(value, level + 1, shift, left_shift)
                lines.append(f"{' ' * ((level + 1) * shift)}{key}: {nested}")
            else:
                lines.append(f"{' ' * ((level + 1) * shift)}{key}: {value}")
        lines.append(f"{' ' * (level * shift)}}}")
    else:
        lines.append(f"{' ' * ((level + 1) * shift)}{data}")

    return "\n".join(lines)

def format_changelog(changelog):
    formatted = {}

    for change in changelog:
        key = change['key']
        change_type = change['type']
        level = change['level']
        original_value = make_string(change['original_value'])
        changed_value = make_string(change['changed_value'])

        # Traverse or create nested structure based on key
        current = formatted
        for _ in range(level):
            current = current.setdefault('nested', {})

        # Add change to the appropriate level
        if change_type == 'added':
            current[f'+ {key}'] = changed_value
        elif change_type == 'deleted':
            current[f'- {key}'] = original_value
        elif change_type == 'changed':
            current[f'- {key}'] = original_value
            current[f'+ {key}'] = changed_value
        else:
            current[key] = original_value

    return format_to_string(formatted, level=0)
