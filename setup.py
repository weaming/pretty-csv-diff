#!/usr/bin/env python

from setuptools import setup
from os.path import dirname, abspath, join

long_description_path = join(dirname(abspath(__file__)), 'README.md')
long_description = open(long_description_path, encoding='utf-8').read()

setup(
    name='pretty-csv-diff',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/telnet23/pretty-csv-diff',
    license='Apache License 2.0',
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm',
    ],
    packages=[
        'pretty_csv_diff',
    ],
    entry_points={
        'console_scripts': [
            'pretty-csv-diff = pretty_csv_diff.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
    ],
)
