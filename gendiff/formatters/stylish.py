from .helpers import format_value, get_diff_indentation, get_indentation


def render_stylish(diff, depth=1):
    lines = ['{']

    def line(prefix, key, value):
        return (
            f'{get_diff_indentation(depth)}{prefix}'
            f'{key}: {format_value(value, depth + 1)}'
        )

    for node in diff:
        node_type = node['type']
        key = node['key']
        if node_type == 'unchanged':
            lines.append(line('  ', key, node['value']))
        elif node_type == 'removed':
            lines.append(line('- ', key, node['value']))
        elif node_type == 'added':
            lines.append(line('+ ', key, node['value']))
        elif node_type == 'changed':
            lines.append(line('- ', key, node['old']))
            lines.append(line('+ ', key, node['new']))
        elif node_type == 'nested':
            children = render_stylish(node['children'], depth + 1)
            lines.append(
                f'{get_diff_indentation(depth)}  {key}: {children}'
            )
    lines.append(f'{get_indentation(depth - 1)}}}')
    return '\n'.join(lines)
