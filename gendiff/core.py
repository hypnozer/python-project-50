from .formatters.json import render_json
from .formatters.plain import render_plain
from .formatters.stylish import render_stylish
from .parser import parse_data


def build_diff(data1, data2):
    diff = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in all_keys:
        if key not in data1:
            diff.append({'key': key, 'type': 'added', 'value': data2[key]})
        elif key not in data2:
            diff.append({'key': key, 'type': 'removed', 'value': data1[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(data1[key], data2[key])
                })
        elif data1[key] == data2[key]:
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': data1[key]
                })
        else:
            diff.append({
                'key': key,
                'type': 'changed',
                'old': data1[key],
                'new': data2[key]
                })
    return diff


def generate_diff(filepath1, filepath2, format_name='stylish'):
    formatters = {
        'stylish': render_stylish,
        'plain': render_plain,
        'json': render_json
        }
    formatter = formatters.get(format_name)
    if formatter is None:
        raise ValueError(f'Unsupported format: {format_name}')
    data1 = parse_data(filepath1)
    data2 = parse_data(filepath2)
    diff = build_diff(data1, data2)
    return formatter(diff)
