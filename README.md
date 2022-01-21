# SerVal-Config-Utils

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 [![test](https://github.com/UL-SnT-Serval/python-config-parser/actions/workflows/build.yaml/badge.svg)](https://github.com/UL-SnT-Serval/python-config-parser/actions/workflows/build.yaml)

[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=python-config-parser&metric=bugs)](https://sonarcloud.io/summary/new_code?id=python-config-parser)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=python-config-parser&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=python-config-parser)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=python-config-parser&metric=coverage)](https://sonarcloud.io/summary/new_code?id=python-config-parser)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=python-config-parser&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=python-config-parser)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=python-config-parser&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=python-config-parser)

## Description

SerVal-Config-Utils automatically parse configurations from multiple sources into a single python dictionary.

## Installation

### Dependencies

serval-config-utils requires:
- PyYAML (^6.0)
- mergedeep (^1.3.4)

### User installation
The easiest way to install serval-config-parser is using `pip`

```
pip install -U serval-config-utils
```

## Usage

In the python main file, use:
```
import configutils
config = configutils.get_config()
```

Call the main file with parameters
```
python main.py  -c ./path/to/config.yaml \
                -c ./path/to/config.json \
                -p my.nested.parameter=value \
                -j {"json_formatted":{"nested_parameter":"value"}} \
```
Access the merged config in the `config` dictionary.
### Example
This simple examples merge the config from `examples/basic_config.yaml` and `examples/basic_config.json` and prints it in the standard output.
```
python examples/basic_example.py -c examples/basic_config.yaml -c examples/basic_config.json
```

## Development

We welcome new contributors of all experience levels.
Use pre-commit to ensure your code follows standards.

### Source code
```
git clone https://github.com/serval-uni-lu/python-config-parser
```

<!-- ### Test
After installation, you can launch the test suite from outside the source directory (you will need to have pytest >= 5.0.1 installed):
```
pytest configutils
``` -->
