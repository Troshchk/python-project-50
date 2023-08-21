import json
import yaml


def load_json(file_path):
    return json.load(open(file_path))


def load_yaml(file_path):
    return yaml.safe_load(open(file_path))


def get_extension(file_path):
    return file_path.split(".")[-1].strip()


LOADERS = {"json": load_json, "yaml": load_yaml, "yml": load_yaml}
