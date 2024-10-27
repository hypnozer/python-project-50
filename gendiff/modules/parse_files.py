def make_changelog(original_file, changed_file):
    changelog = []
    all_keys = sorted(set(original_file.keys()).union(changed_file.keys()))
    for key in all_keys:
        if key in original_file and key in changed_file:
            change_type = (
                "unchanged" if original_file[key] == changed_file[key]
                else "changed"
            )
        elif key in original_file:
            change_type = "deleted"
        else:
            change_type = "added"
        change_entry = {"key": key, "type": change_type}
        changelog.append(change_entry)
    return changelog
