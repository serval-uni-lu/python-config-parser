from config_parser.parser import StrParser, InlineJsonParser
import pytest


@pytest.mark.parametrize("str_input,dic_out", [
    ("key1=abc", {"key1": "abc"}),
    ("key1.key2=3", {"key1": {"key2": 3}}),
    ("key1=", None)])
def test_str_parser(str_input, dic_out):
    str_parser = StrParser()
    res = str_parser.do(f"{str_input}")
    assert res == dic_out


@pytest.mark.parametrize("inline_input, dic_out", [
    ('{' + f"\"key1\":3,\"key2\":3" + '}', {"key1": 3, "key2": 3}),
    ('{' + f"\"key1\":,\"key2\":3" + '}', None),
])
def test_inline_parser(inline_input, dic_out):
    inline_parser = InlineJsonParser()
    res = inline_parser.do(inline_input)
    assert res == dic_out
