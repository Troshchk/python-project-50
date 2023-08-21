from .comparer import compare_data
from .parsers.stylish_parser import stylish
from .parsers.plain_parser import plain
from .parsers.json_parser import json_parser
from .loaders import get_extension, LOADERS


def generate_diff(file1_path, file2_path, format="stylish"):
    file1_data, file2_data = map(
        lambda file: LOADERS.get(get_extension(file))(file),
        [file1_path, file2_path],
    )
    diff_dict = compare_data(file1_data, file2_data)
    if format == "stylish":
        return stylish(diff_dict)
    if format == "plain":
        return plain(diff_dict)
    if format == "json":
        return json_parser(diff_dict)
