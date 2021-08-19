import argparse
import hashlib
import json
import yaml
from mergedeep import merge, Strategy
import re
from config_parser.parser import InlineJsonParser, ConfigFileParser, StrParser


def value_parser(value):
    SPECIAL_KEY = "SPECIAL_KEY"
    if re.match("^[-+]?[0-9]*\\.?[0-9]+(e[-+]?[0-9]+)?$", value) is None:
        return str(value)
    else:
        return yaml.safe_load(f"{SPECIAL_KEY}: {value}")[SPECIAL_KEY]


def merge_parameters(a, b):
    return merge(a, b, strategy=Strategy.REPLACE)


def get_config():
    parser = argparse.ArgumentParser(allow_abbrev=False)

    parser_actions = {
        parser.add_argument(
            "-c",
            help="Provide config file in yaml or json.",
            action="append",
        ).dest: ConfigFileParser(),
        parser.add_argument(
            "-j",
            help="Inline json.",
            action="append",
        ).dest: InlineJsonParser(),
        parser.add_argument(
            "-p",
            help="Provide extra parameters on the form key1.key2[key3]=value.",
            action="append",
        ).dest: StrParser(),
    }
    arguments, unknown_args = parser.parse_known_args()
    args = vars(arguments)
    current_parameters = {}

    for key in args:
        parser_action = parser_actions[key]
        if args[key] is not None:
            for value in args[key]:
                merge_parameters(current_parameters, parser_action.do(value))

    return current_parameters


def get_config_hash():
    return get_dict_hash(get_config())


def get_dict_hash(dictionary):
    dictionary_str = json.dumps(dictionary, sort_keys=True)
    dictionary_hash = hashlib.md5(dictionary_str.encode("utf-8")).hexdigest()
    return dictionary_hash


def save_config(pre_path):
    with open(f"{pre_path}{get_config_hash()}.yaml", "w") as f:
        yaml.dump(get_config(), f)
