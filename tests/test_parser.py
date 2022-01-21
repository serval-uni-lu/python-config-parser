import pytest

from configutils.parser import ConfigFileParser, InlineJsonParser, StrParser


@pytest.mark.parametrize(
    "str_input,dic_out",
    [
        ("key1=abc", {"key1": "abc"}),
        ("key1.key2=3", {"key1": {"key2": 3}}),
        ("key1=", None),
    ],
)
def test_str_parser(str_input, dic_out):
    str_parser = StrParser()
    res = str_parser.do(f"{str_input}")
    assert res == dic_out


@pytest.mark.parametrize(
    "inline_input, dic_out",
    [
        ("{" + '"key1":3,"key2":3' + "}", {"key1": 3, "key2": 3}),
        ("{" + '"key1":,"key2":3' + "}", None),
    ],
)
def test_inline_parser(inline_input, dic_out):
    inline_parser = InlineJsonParser()
    res = inline_parser.do(inline_input)
    assert res == dic_out


@pytest.mark.parametrize(
    "config_path,dic_out",
    [
        ("./tests/test_config.yaml", {"a": {"b": "c"}}),
        ("./tests/test_config.yml", {"a": {"b": "c"}}),
        ("./tests/test_config.json", {"a": {"b": "c"}}),
    ],
)
def test_yaml_file(config_path, dic_out):
    file_parser = ConfigFileParser()
    res = file_parser.do(config_path)
    assert res == dic_out
