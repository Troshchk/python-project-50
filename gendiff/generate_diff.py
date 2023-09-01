from .comparer import compare_data
from .formatters.formatters import format_output
from .parsers import parse_file


def generate_diff(file1_path, file2_path, format="stylish"):
    file1_data = parse_file(file1_path)
    file2_data = parse_file(file2_path)
    diff_dict = compare_data(file1_data, file2_data)
    return format_output(format, diff_dict)
