import gendiff.scripts.gendiff as gendiff
import pytest


def get_path_to_file(filename, path="./tests/fixtures/"):
    return f"{path}{filename}"


def get_test_output(output_file):
    f = open(output_file, "r")
    test_output = f.read()
    f.close()
    return test_output


FILE1_JSON_NESTED = get_path_to_file("file1_nested.json")
FILE2_JSON_NESTED = get_path_to_file("file2_nested.json")
FILE1_YAML_NESTED = get_path_to_file("file1_nested.yaml")
FILE2_YAML_NESTED = get_path_to_file("file2_nested.yaml")
OUTPUT_NESTED = get_path_to_file("output_nested")
OUTPUT_NESTED_PLAIN = get_path_to_file("output_nested_plain")
OUTPUT_NESTED_JSON = get_path_to_file("output_nested_json")


@pytest.mark.parametrize(
    "file1,file2,expected",
    [
        (FILE1_JSON_NESTED, FILE2_JSON_NESTED, OUTPUT_NESTED),
        (FILE1_YAML_NESTED, FILE2_YAML_NESTED, OUTPUT_NESTED),
        (FILE1_JSON_NESTED, FILE2_YAML_NESTED, OUTPUT_NESTED),
    ],
)
def test_standard_format(file1, file2, expected):
    assert gendiff.generate_diff(file1, file2, "stylish") == get_test_output(
        expected
    )


@pytest.mark.parametrize(
    "format,expected",
    [("plain", OUTPUT_NESTED_PLAIN), ("json", OUTPUT_NESTED_JSON)],
)
def test_other_formats(format, expected):
    assert gendiff.generate_diff(
        FILE1_JSON_NESTED, FILE2_JSON_NESTED, format=format
    ) == get_test_output(expected)
