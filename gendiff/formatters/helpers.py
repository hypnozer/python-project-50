def get_indentation(depth):
    return ' ' * (depth * 4)


def get_diff_indentation(depth):
    return ' ' * max((depth * 4 - 2), 0)


def format_value(value, depth):
    if isinstance(value, dict):
        lines = ['{']
        for key, nested_value in value.items():
            lines.append(
                f'{get_indentation(depth)}'
                f'{key}: {format_value(nested_value, depth + 1)}'
            )
        lines.append(f'{get_indentation(depth - 1)}}}')
        return '\n'.join(lines)
    return format_primitive(value)


def format_plain_value(value):
    if isinstance(value, dict) or isinstance(value, list):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return format_primitive(value)


def format_primitive(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return str(value)
