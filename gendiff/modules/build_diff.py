from gendiff.modules.make_changelog import make_changelog


TYPES_OF_CHANGES = {
    "unchanged": "  ",
    "changed_old": "- ",
    "changed_new": "+ ",
    "deleted": "- ",
    "added": "+ ",
}


def make_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def build_diff(original_file, changed_file):
    changelog = make_changelog(original_file, changed_file)
    diff_lines = []
    diff_lines.append("{")
    for change in changelog:
        key = change["key"]
        change_type = change["type"]
        if change_type == "unchanged":
            value = make_string(original_file[key])
            diff_lines.append(
                f"  {TYPES_OF_CHANGES[change_type]}{key}: {value}")
        elif change_type == "changed":
            old_value = make_string(original_file[key])
            new_value = make_string(changed_file[key])
            diff_lines.append(
                f"  {TYPES_OF_CHANGES['changed_old']}{key}: {old_value}")
            diff_lines.append(
                f"  {TYPES_OF_CHANGES['changed_new']}{key}: {new_value}")

        elif change_type == "deleted":
            value = make_string(original_file[key])
            diff_lines.append(
                f"  {TYPES_OF_CHANGES[change_type]}{key}: {value}")
        elif change_type == "added":
            value = make_string(changed_file[key])
            diff_lines.append(
                f"  {TYPES_OF_CHANGES[change_type]}{key}: {value}")
    diff_lines.append("}")
    diff = "\n".join(diff_lines)
    return diff
