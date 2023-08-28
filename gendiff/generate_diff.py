from .comparer import compare_data
from .formatters.formatters import FORMATTERS
from .parsers import PARSERS
import pathlib


def generate_diff(file1_path, file2_path, format="stylish"):
    file1_data, file2_data = map(
        lambda file: PARSERS.get(pathlib.Path(file).suffix)(file),
        [file1_path, file2_path],
    )
    diff_dict = compare_data(file1_data, file2_data)
    return FORMATTERS.get(format)(diff_dict)
