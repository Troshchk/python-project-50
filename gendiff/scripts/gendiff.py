#!/usr/bin/env python3
import argparse
import sys
from ..generate_diff import generate_diff


def main():
    parser = create_parser()
    args = parser.parse_args(None if sys.argv[1:] else ['-h'])
    if args.first_file and args.second_file:
        return generate_diff(args.first_file,
                             args.second_file,
                             format=args.format)
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


if __name__ == '__main__':
    main()
