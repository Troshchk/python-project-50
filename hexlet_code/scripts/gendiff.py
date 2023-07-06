#!/usr/bin/env python3
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args(None if sys.argv[2:] else ['-h'])
    return args


if __name__ == '__main__':
    main()
