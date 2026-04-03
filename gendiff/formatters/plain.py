from .helpers import format_plain_value


def render_plain(diff):
    lines = walk_diff(diff)
    return '\n'.join(lines)


def walk_diff(diff, path=''):
    lines = []
    for node in diff:
        key = node['key']
        current_path = f'{path}.{key}' if path else key
        node_type = node['type']
        if node_type == 'unchanged':
            continue
        elif node_type == 'nested':
            lines.extend(walk_diff(node['children'], current_path))
        elif node_type == 'added':
            lines.append(f"Property '{current_path}' was added with value: "
                         f"{format_plain_value(node['value'])}"
            )
        elif node_type == 'removed':
            lines.append(
                f"Property '{current_path}' was removed"
            )
        elif node_type == 'changed':
            lines.append(
                f"Property '{current_path}' was updated. "
                f'From {format_plain_value(node["old"])} '
                f'to {format_plain_value(node["new"])}'
            )
    return lines
