def get_indentation(depth):
    return ' ' * (depth * 4)


def get_diff_indentation(depth):
    return ' ' * max((depth * 4 - 2), 0)


def format_value(value, depth):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        if value:
            return 'true'
        else:
            return 'false'
    if not isinstance(value, dict):
        return str(value)
    lines = ['{']
    for key, nested_value in value.items():
        lines.append(
            f'{get_indentation(depth)}'
            f'{key}: {format_value(nested_value, depth + 1)}'
        )
    lines.append(f'{get_indentation(depth - 1)}}}')
    return '\n'.join(lines)
