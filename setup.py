# -*- coding: utf-8 -*-

# Learn more:https://github.com/MaximeMohandi/MSQBitsReporter2.0/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='MSQBitsReporter',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Maxime Mohandi',
    author_email='contact@maximemohandi.fr',
    url='https://github.com/MaximeMohandi/MSQBitsReporter2.0',
    license=license,
    packages=find_packages(exclude=('test', 'docs'))
)
