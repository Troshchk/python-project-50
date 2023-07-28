import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='''Compares two configuration files and shows
        a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '--format', '-f', help="set format of output", default="stylish"
    )
    return parser


def parse_inputs():
    parser = create_parser()
    args = parser.parse_args(None if sys.argv[1:] else ['-h'])
    return args
