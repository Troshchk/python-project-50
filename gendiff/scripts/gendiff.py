#!/usr/bin/env python3
import argparse
import sys
import json


def main():
    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='''Compares two configuration files and shows
                                a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('--format', '-f', help="set format of output")
    args = parser.parse_args(None if sys.argv[1:] else ['-h'])
    if args.first_file and args.second_file:
        return generate_diff(args.first_file, args.second_file)
    return args


def create_sring(diff_dict):
    out_str = ""
    for k, v in diff_dict.items():
        if v[0] == v[1]:
            out_str += f"{k}: {v[0]}\n"
        elif v[0] is None:
            out_str += f"+ {k}: {v[1]}\n"
        elif v[1] is None:
            out_str += f"- {k}: {v[1]}\n"
        else:
            out_str += f"- {k}: {v[0]}\n+ {k}: {v[1]}\n"
    return out_str


def generate_diff(file1, file2):
    f1 = json.load(open(file1))
    f2 = json.load(open(file2))
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
