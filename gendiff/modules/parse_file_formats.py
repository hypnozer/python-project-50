import yaml
import json


def load_file(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(file) or {}
        else:
            raise ValueError(f"Unsupported file format: {file_path}")
