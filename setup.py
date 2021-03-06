#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import pip
from pip.req import parse_requirements
from setuptools import setup

import wpparser

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


packages = [
    "wpparser"
]

# Handle requirements
requires = parse_requirements("requirements/install.txt",
                              session=pip.download.PipSession())
install_requires = [str(ir.req) for ir in requires]

requires = parse_requirements("requirements/tests.txt",
                              session=pip.download.PipSession())
tests_require = [str(ir.req) for ir in requires]

# Convert markdown to rst
try:
    from pypandoc import convert
    long_description = convert("README.md", "rst")
except:
    long_description = ""

setup(
    name="wpparser",
    version=wpparser.__version__,
    description="Parse wordpress export files into a well formatted python dictionary",  # NOQA
    long_description=long_description,
    author="Martin Sandström",
    author_email="martin@marteinn.se",
    url="https://github.com/marteinn/wpparser",
    packages=packages,
    package_data={"": ["LICENSE", ], "wpparser": ["*.txt"]},
    package_dir={"wpparser": "wpparser"},
    include_package_data=True,
    install_requires=install_requires,
    license="MIT",
    zip_safe=False,
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4"
    ),
)
