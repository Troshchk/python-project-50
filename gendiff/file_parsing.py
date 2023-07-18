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
    out_str_from_dict = "{\n"
    for k, v in input_dict.items():
        if not isinstance(v, dict):
            value = v
        else:
            value = create_dict_structure(v, indent+NEW_LEVEL)
        addition = "  "
        out_str_from_dict += PATTERN2.format(indent, addition, k, value)
        out_str_from_dict += "\n"
    out_str_from_dict += f"{indent.replace('  ', '', 1)}"
    out_str_from_dict += "}"
    return out_str_from_dict
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
        if k1 in data2.keys():
            if isinstance(data2[k1], dict):
                diff_dict[k1] = compare_data(data1[k1], data2[k1])
            else:
                diff_dict[k1] = (v1, data2[k1])
        else:
            diff_dict[k1] = (v1, data2.get(k1, NotSet()))
    for k2, v2 in data2.items():
        if k2 not in diff_dict.keys():
            diff_dict[k2] = (data1.get(k2, NotSet()), v2)
    return dict(sorted(diff_dict.items()))


def generate_diff(file1, file2):
    f1, f2 = map(load_file, [file1, file2])
    diff_dict = compare_data(f1, f2)
    out_str = create_string(diff_dict)
    return out_str.rstrip()
