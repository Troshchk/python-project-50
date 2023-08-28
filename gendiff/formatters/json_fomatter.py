import json


def json_parser(diff_dict, indent=4):
    return json.dumps(diff_dict, indent=indent)
