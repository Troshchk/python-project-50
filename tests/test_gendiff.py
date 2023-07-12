import gendiff.scripts.gendiff as gendiff
import pytest

@pytest.fixture
def get_file1_path():
    return "./tests/fixtures/file1.json"


@pytest.fixture
def get_file2_path():
    return "./tests/fixtures/file2.json"


@pytest.fixture
def get_res_diff():
    f = open(
        "./tests/fixtures/test_output1",
        "r")
    test_output = f.read()
    f.close()
    return test_output


def test_simple_case(get_file1_path, get_file2_path, get_res_diff):
    out = gendiff.generate_diff(get_file1_path, get_file2_path)
    print(out)
    print(get_res_diff)
    assert out == get_res_diff
