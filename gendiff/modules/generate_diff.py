import json


def generate_diff(file_path1, file_path2):
    original_file = json.load(open(file_path1))
    changed_file = json.load(open(file_path2))
    return original_file, changed_file
