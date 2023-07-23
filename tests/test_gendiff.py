import gendiff.scripts.gendiff as gendiff
import pytest

FILE1_JSON = "./tests/fixtures/file1.json"
FILE2_JSON = "./tests/fixtures/file2.json"
FILE3_JSON = "./tests/fixtures/file3.json"
FILE4_JSON = "./tests/fixtures/file4.json"
FILE1_YAML = "./tests/fixtures/file1.yaml"
FILE2_YAML = "./tests/fixtures/file2.yaml"
FILE1_JSON_NESTED = "./tests/fixtures/file1_nested.json"
FILE2_JSON_NESTED = "./tests/fixtures/file2_nested.json"
FILE1_YAML_NESTED = "./tests/fixtures/file1_nested.yaml"
FILE2_YAML_NESTED = "./tests/fixtures/file2_nested.yaml"
OUTPUT_FLAT = "./tests/fixtures/output_flat"
OUTPUT_NESTED = "./tests/fixtures/output_nested"
OUTPUT_NESTED_PLAIN = "./tests/fixtures/output_nested_plain"
OUTPUT_NESTED_JSON = "./tests/fixtures/output_nested_json"
OUTPUT_HEXLET_TESTS = "./tests/fixtures/output_hexlet_tests"


def get_test_output(output_file):
    f = open(output_file, "r")
    test_output = f.read()
    f.close()
    return test_output


@pytest.mark.parametrize(
    "file1,file2,expected",
    [
        (FILE1_JSON, FILE2_JSON, OUTPUT_FLAT),
        (FILE1_YAML, FILE2_YAML, OUTPUT_FLAT),
        (FILE1_JSON, FILE2_YAML, OUTPUT_FLAT),
        (FILE1_JSON_NESTED, FILE2_JSON_NESTED, OUTPUT_NESTED),
        (FILE1_YAML_NESTED, FILE2_YAML_NESTED, OUTPUT_NESTED),
        (FILE1_JSON_NESTED, FILE2_YAML_NESTED, OUTPUT_NESTED),
        (FILE3_JSON, FILE4_JSON, OUTPUT_HEXLET_TESTS),
    ],
)
def test_standard_format(file1, file2, expected):
    assert gendiff.generate_diff(file1, file2) == get_test_output(expected)


@pytest.mark.parametrize(
    "format,expected",
    [("plain", OUTPUT_NESTED_PLAIN), ("json", OUTPUT_NESTED_JSON)],
)
def test_other_formats(format, expected):
    assert gendiff.generate_diff(
        FILE1_JSON_NESTED, FILE2_JSON_NESTED, format=format
    ) == get_test_output(expected)
