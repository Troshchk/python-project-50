#!/usr/bin/env python3
from ..generate_diff import generate_diff
from ..cli import parse_inputs


def main():
    args = parse_inputs()
    if args.first_file and args.second_file:
        output = generate_diff(args.first_file,
                               args.second_file,
                               format=args.format)
        print(output)
    return


if __name__ == '__main__':
    main()
