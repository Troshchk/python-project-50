import json
import yaml
from .parsers.stylish_parser import stylish
from .parsers.plain_parser import plain
from .parsers.json_parser import json_parser


def load_json(file_path):
    return json.load(open(file_path))


def load_yaml(file_path):
    return yaml.safe_load(open(file_path))


def get_extension(file_path):
    return file_path.split(".")[-1].strip()


LOADERS = {"json": load_json, "yaml": load_yaml, "yml": load_yaml}


def compare_data(data1, data2):
    """Output format:
    (val_1st_input, val_2nd_input, val_is_in_1st_input, val_is_in_2nd_input)
    First two fields are field values from the input.
    Second two fields contain info whether the field values exist in the input.
    This is necessary to distinguish None coming from input and None specifying,
    that the field value does not exist in the input"""
    diff_dict = {}
    if isinstance(data1, dict) and isinstance(data2, dict):
        for k1, v1 in data1.items():
            if k1 in data2.keys():
                if isinstance(data2[k1], dict):
                    diff_dict[k1] = compare_data(data1[k1], data2[k1])
                    continue
                diff_dict[k1] = (v1, data2[k1], True, True)
            else:
                diff_dict[k1] = (v1, None, True, False)
        for k2, v2 in data2.items():
            if k2 not in diff_dict.keys():
                diff_dict[k2] = (None, v2, False, True)
    else:
        return (data1, data2, True, True)
    return dict(sorted(diff_dict.items()))


def generate_diff(file1_path, file2_path, format="stylish"):
    file1_data, file2_data = map(
        lambda file: LOADERS.get(get_extension(file))(file),
        [file1_path, file2_path],
    )
    diff_dict = compare_data(file1_data, file2_data)
    if format == "stylish":
        return stylish(diff_dict).rstrip("\n")
    if format == "plain":
        return plain(diff_dict)
    if format == "json":
        return json_parser(diff_dict)
