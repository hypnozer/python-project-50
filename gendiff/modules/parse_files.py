def make_changelog(original_file, changed_file):
    changelog = []

    all_keys = sorted(set(original_file.keys()).union(set(changed_file.keys()))
                      )

    for key in all_keys:
        if key in original_file and key in changed_file:
            if original_file[key] == changed_file[key]:
                changelog.append({'key': key, 'type': 'unchanged'})
            else:
                changelog.append({'key': key, 'type': 'changed'})
        elif key in original_file:
            changelog.append({'key': key, 'type': 'deleted'})
        elif key in changed_file:
            changelog.append({'key': key, 'type': 'added'})

    return changelog
