def build_flat_diff(dic1, dic2):
    diff = []
    all_keys = sorted(set(dic1.keys()) | set(dic2.keys()))
    for key in all_keys:
        if key not in dic1:
            diff.append({"key": key, "type": "added", "value": dic2[key]})
        elif key not in dic2:
            diff.append({"key": key, "type": "removed", "value": dic1[key]})
        elif dic1[key] != dic2[key]:
            diff.append({
                "key": key,
                "type": "changed",
                "old": dic1[key],
                "new": dic2[key]
                })
        else:
            diff.append({"key": key, "type": "unchanged", "value": dic1[key]})
    return diff


def generate_diff(data1, data2):
    diff = build_flat_diff(data1, data2)
    return render_stylish(diff)


def fmt_value(value):
    if value is None:
        return "Null"
    if isinstance(value, bool):
        if value:
            return "true"
        else:
            return "false"
    return str(value)


def render_stylish(diff):
    lines = ["{"]

    def line(prefix, key, value):
        return f"  {prefix}{key}: {fmt_value(value)}"

    for node in diff:
        type = node["type"]
        key = node["key"]
        if type == "unchanged":
            lines.append(line("  ", key, node["value"]))
        elif type == "removed":
            lines.append(line("- ", key, node["value"]))
        elif type == "added":
            lines.append(line("+ ", key, node["value"]))
        elif type == "changed":
            lines.append(line("- ", key, node["old"]))
            lines.append(line("+ ", key, node["new"]))
    lines.append("}")
    return "\n".join(lines)
