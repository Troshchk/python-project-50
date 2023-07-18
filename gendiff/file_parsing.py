import json
import yaml


def jsonify(v):
    if isinstance(v, bool):
        return json.dumps(v)
    if v is None:
        return json.dumps(v)
    return v


class NotSet:
    """A class to distinguish null from jsom/yaml from None meaning the value
    does not exist in the input """
    isset = False


def create_dict_structure(input_dict, indent):
        else:
            out_str += f"  - {k}: {v0}\n  + {k}: {v1}\n"
    out_str += "}"
    return out_str


def load_file(file_path):
    extension = file_path.split(".")[-1].strip()
    if extension == "json":
        return json.load(open(file_path))
    if extension in ["yaml", "yml"]:
        return yaml.safe_load(open(file_path))


def compare_data(data1, data2):
    diff_dict = {}
    for k1, v1 in data1.items():
        diff_dict[k1] = (v1, data2.get(k1, None))
    for k2, v2 in data2.items():
        if k2 not in diff_dict.keys():
            diff_dict[k2] = (data1.get(k2, None), v2)
    return dict(sorted(diff_dict.items()))


def generate_diff(file1, file2):
    f1, f2 = map(load_file, [file1, file2])
    diff_dict = compare_data(f1, f2)
    out_str = create_string(diff_dict)
    return out_str.rstrip()
