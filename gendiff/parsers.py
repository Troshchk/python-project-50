import json
import yaml
import pathlib


def load_json(file_path):
    return json.load(open(file_path))


def load_yaml(file_path):
    return yaml.safe_load(open(file_path))


PARSERS = {".json": load_json, ".yaml": load_yaml, ".yml": load_yaml}


def parse_file(filepath):
    extension = pathlib.Path(filepath).suffix
    parser = PARSERS.get(extension)
    return parser(filepath)
