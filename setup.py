#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

long_description = """This library provides access to the OCTP server API"""

setup(
    name='python-octp',
    version='0.0.1',
    description='API to communicate with OCTP servers',
    author='eyJhb',
    author_email='eyjhbb@gmail.com',
    url='https://github.com/eyjhb/python-octp',
    packages=['octp'],
    install_requires=['requests'],
    # test_suite='digitalocean.tests',
    # license='',
    long_description=long_description
)
