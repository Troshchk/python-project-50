import gendiff.scripts.gendiff as gendiff
import pytest


@pytest.fixture
def get_file1_json_path():
    return "./tests/fixtures/file1.json"


@pytest.fixture
def get_file2_json_path():
    return "./tests/fixtures/file2.json"


@pytest.fixture
def get_file1_nested_json_path():
    return "./tests/fixtures/file1_nested.json"


@pytest.fixture
def get_file2_nested_json_path():
    return "./tests/fixtures/file2_nested.json"


@pytest.fixture
def get_file1_yaml_path():
    return "./tests/fixtures/file1.yaml"


@pytest.fixture
def get_file2_yaml_path():
    return "./tests/fixtures/file2.yaml"


@pytest.fixture
def get_file1_nested_yaml_path():
    return "./tests/fixtures/file1_nested.yaml"


@pytest.fixture
def get_file2_nested_yaml_path():
    return "./tests/fixtures/file2_nested.yaml"


@pytest.fixture
def get_res_diff():
    f = open("./tests/fixtures/output_flat", "r")
    test_output = f.read()
    f.close()
    return test_output


@pytest.fixture
def get_res_diff_nested():
    f = open("./tests/fixtures/output_nested", "r")
    test_output = f.read()
    f.close()
    return test_output


@pytest.fixture
def get_res_diff_nested_plain():
    f = open("./tests/fixtures/output_nested_plain", "r")
    test_output = f.read()
    f.close()
    return test_output


@pytest.fixture
def get_json_nested_output():
    f = open("./tests/fixtures/output_json_nested", "r")
    test_output = f.read()
    f.close()
    return test_output


@pytest.fixture
def get_file3():
    return "./tests/fixtures/file3.json"


@pytest.fixture
def get_file4():
    return "./tests/fixtures/file4.json"


@pytest.fixture
def get_hex_out():
    f = open("./tests/fixtures/output_hexlet_tests", "r")
    test_output = f.read()
    f.close()
    return test_output


def test_simple_case_jsons(
    get_file1_json_path, get_file2_json_path, get_res_diff
):
    out = gendiff.generate_diff(get_file1_json_path, get_file2_json_path)
    assert out == get_res_diff


def test_simple_case_yamls(
    get_file1_yaml_path, get_file2_yaml_path, get_res_diff
):
    out = gendiff.generate_diff(get_file1_yaml_path, get_file2_yaml_path)
    assert out == get_res_diff


def test_simple_case_json_and_yamls(
    get_file1_json_path, get_file2_yaml_path, get_res_diff
):
    out = gendiff.generate_diff(get_file1_json_path, get_file2_yaml_path)
    assert out == get_res_diff


def test_nested_case_jsons(
    get_file1_nested_json_path, get_file2_nested_json_path, get_res_diff_nested
):
    out = gendiff.generate_diff(
        get_file1_nested_json_path, get_file2_nested_json_path
    )
    assert out == get_res_diff_nested


def test_nested_case_json_and_yaml(
    get_file1_nested_json_path, get_file2_nested_yaml_path, get_res_diff_nested
):
    out = gendiff.generate_diff(
        get_file1_nested_json_path, get_file2_nested_yaml_path
    )
    assert out == get_res_diff_nested


def test_nested_case_yamls(
    get_file1_nested_yaml_path, get_file2_nested_yaml_path, get_res_diff_nested
):
    out = gendiff.generate_diff(
        get_file1_nested_yaml_path, get_file2_nested_yaml_path
    )
    assert out == get_res_diff_nested


def test_nested_case_plain(
    get_file1_nested_json_path,
    get_file2_nested_json_path,
    get_res_diff_nested_plain,
):
    out = gendiff.generate_diff(
        get_file1_nested_json_path, get_file2_nested_json_path, format="plain"
    )
    assert out == get_res_diff_nested_plain


def test_nested_case_json(
    get_file1_nested_json_path,
    get_file2_nested_json_path,
    get_json_nested_output,
):
    out = gendiff.generate_diff(
        get_file1_nested_json_path, get_file2_nested_json_path, format="json"
    )
    assert out == get_json_nested_output


def test_hex_case_stylish(get_file3, get_file4, get_hex_out):
    out = gendiff.generate_diff(get_file3, get_file4)
    assert out == get_hex_out
