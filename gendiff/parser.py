import json
import os

import yaml


def parse_json(filepath):
    with open(filepath, encoding="utf-8") as file:
        return json.load(file)


def parse_yaml(filepath):
    with open(filepath, encoding="utf-8") as file:
        return yaml.safe_load(file)


def parse_data(filepath):
    _, ext = os.path.splitext(filepath)
    if ext == '.json':
        return parse_json(filepath)
    if ext in ('.yml', '.yaml'):
        return parse_yaml(filepath)

    raise ValueError(f"Unsupported file format: {ext}")





