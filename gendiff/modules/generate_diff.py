import json
from gendiff.modules.build_diff import build_diff


def generate_diff(file_path1, file_path2):
    original_file = json.load(open(file_path1))
    changed_file = json.load(open(file_path2))
    return build_diff(original_file, changed_file)
