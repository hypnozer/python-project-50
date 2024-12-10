from gendiff.modules.build_diff import build_diff
from gendiff.modules.parse_file_formats import load_file


def generate_diff(file_path1, file_path2):
    original_file = load_file(file_path1)
    changed_file = load_file(file_path2)
    return build_diff(original_file, changed_file)
