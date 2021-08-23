import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="config_parser",
    version="0.0.1",
    author="configParser Team",
    author_email="adriano.franci@uni.lu",
    description="This package allows to pass config file or strings to a python program",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UL-SnT-Serval/python-config-parser",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "config_parser"},
    packages=setuptools.find_packages(where="config_parser"),
    python_requires=">=3.6",
)
