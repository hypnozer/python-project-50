from gendiff.modules.format_changelog import format_changelog
from gendiff.modules.make_changelog import make_changelog
from gendiff.modules.parse_file_formats import load_file


def generate_diff(file_path1, file_path2):
    original_file = load_file(file_path1)
    changed_file = load_file(file_path2)
    return format_changelog(make_changelog(original_file, changed_file))
