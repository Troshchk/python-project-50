#!/usr/bin/env python3
import argparse
import sys
import json
import yaml


def main():
    parser = create_parser()
    args = parser.parse_args(None if sys.argv[1:] else ['-h'])
    if args.first_file and args.second_file:
        return generate_diff(args.first_file, args.second_file)
    return args


def create_parser():
    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='''Compares two configuration files and shows
                                a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('--format', '-f', help="set format of output")
    return parser


def jsonify(v):
    if isinstance(v, bool):
        return json.dumps(v)
    return v


def create_sring(diff_dict):
    out_str = "{\n"
    for k, v in diff_dict.items():
        v0, v1 = v
        print(v0, v1)
        v0 = jsonify(v0)
        v1 = jsonify(v1)
        print(v0, v1)
        if v0 == v1:
            out_str += f"    {k}: {v0}\n"
        elif v0 is None:
            out_str += f"  + {k}: {v1}\n"
        elif v1 is None:
            out_str += f"  - {k}: {v0}\n"
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


def generate_diff(file1, file2):
    f1 = load_file(file1)
    f2 = load_file(file2)
    diff_dict = {}
    for k1, v1 in f1.items():
        diff_dict[k1] = (v1, f2.get(k1, None))
    for k2, v2 in f2.items():
        if k2 not in diff_dict.keys():
            diff_dict[k2] = (f1.get(k2, None), v2)
    diff_dict = dict(sorted(diff_dict.items()))
    return create_sring(diff_dict)


if __name__ == '__main__':
    main()
