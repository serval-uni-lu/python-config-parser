import pytest

from configutils.utils import get_config, get_dict_hash, merge_parameters


def test_get_dict_hash_sample():
    assert (
        get_dict_hash({"a": 1, "b": 2}) == "8aacdb17187e6acf2b175d4aa08d7213"
    )


def test_get_dict_hash_order():
    assert get_dict_hash({"a": 1, "b": 2}) == get_dict_hash({"b": 2, "a": 1})


def test_get_config():
    _ = get_config()
    assert True


@pytest.mark.parametrize(
    "dict_a,dict_b,dict_out",
    [
        ({"a": 1, "b": 2}, {"b": 3}, {"a": 1, "b": 3}),
    ],
)
def test_merge_parameters(dict_a, dict_b, dict_out):
    assert dict_out == merge_parameters(dict_a, dict_b)
