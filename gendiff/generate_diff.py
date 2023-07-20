import json
import yaml
from .parsers.stylish_parser import stylish
from .parsers.plain_parser import plain
from .parsers.json_parser import json_parser


def load_file(file_path):
    extension = file_path.split(".")[-1].strip()
    if extension == "json":
        return json.load(open(file_path))
    if extension in ["yaml", "yml"]:
        return yaml.safe_load(open(file_path))


def compare_data(data1, data2, key_above=None):
    """Output contains values and info whether the value was set in the input.
    This is necessary to distinguish None from input and values,
    which are not set"""
    diff_dict = {}
    if isinstance(data1, dict):
        if isinstance(data2, dict):
            for k1, v1 in data1.items():
                if k1 in data2.keys():
                    if isinstance(data2[k1], dict):
                        diff_dict[k1] = compare_data(data1[k1], data2[k1], key_above=k1)
                    else:
                        diff_dict[k1] = (v1, data2[k1], True, True)
                else:
                    diff_dict[k1] = (v1, None, True, False)
            for k2, v2 in data2.items():
                if k2 not in diff_dict.keys():
                    diff_dict[k2] = (None, v2, False, True)
        else:
            diff_dict[k1] = (data1, data2, True, True)
    elif isinstance(data2, dict):
        return (data1, data2, True, True)
    return dict(sorted(diff_dict.items()))


def generate_diff(file1, file2, format=None):
    f1, f2 = map(load_file, [file1, file2])
    print(f1)
    print(f2)
    diff_dict = compare_data(f1, f2)
    if format in [None, "stylish"]:
        out_str = stylish(diff_dict).rstrip()
    elif format == "plain":
        out_str = plain(diff_dict).rstrip()
    elif format == "json":
        return json_parser(diff_dict)
    return out_str
