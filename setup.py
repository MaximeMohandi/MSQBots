# -*- coding: utf-8 -*-

# Learn more:https://github.com/MaximeMohandi/MSQBitsReporter2.0/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='MSQBitsReporter',
    version='2.0.0',
    description='Package MSQBitsReporter',
    long_description=readme,
    author='Maxime Mohandi',
    author_email='contact@maximemohandi.fr',
    url='https://github.com/MaximeMohandi/MSQBitsReporter2.0',
    license=license,
    packages=find_packages(exclude=('test', 'docs'))
)
